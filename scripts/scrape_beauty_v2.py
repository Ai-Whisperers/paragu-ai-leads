#!/usr/bin/env python3
import json
import logging
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.panel import Panel

from src.config import GOOGLE_MAPS_API_KEY, ASUNCION_CENTER
from src.api_client import PlacesClient
from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter

console = Console()
logging.basicConfig(level=logging.WARNING)

EXISTING_DATA = "data/asuncion_beauty_all_businesses_20260414_185314.csv"

console.print(
    Panel.fit(
        "[bold cyan]Expanded Beauty Scraper v2 - Greater Asuncion[/bold cyan]\n"
        "[dim]Dedup existing · Broader keywords · Grid search[/dim]",
        border_style="cyan",
    )
)

client = PlacesClient(GOOGLE_MAPS_API_KEY)
all_businesses = {}
existing_ids = set()

# Load existing
import pandas as pd
from src.models import Business

if Path(EXISTING_DATA).exists():
    df_existing = pd.read_csv(EXISTING_DATA)
    for _, row in df_existing.iterrows():
        pid = str(row.get("place_id", ""))
        if not pid:
            continue
        existing_ids.add(pid)
        b = Business(
            place_id=pid,
            name=str(row.get("name", "") or ""),
            status=str(row.get("status", "") or ""),
            address=str(row.get("address", "") or ""),
            street_number=str(row.get("street_number", "") or ""),
            street_name=str(row.get("street_name", "") or ""),
            neighborhood=str(row.get("neighborhood", "") or ""),
            city=str(row.get("city", "") or ""),
            state=str(row.get("state", "") or ""),
            postal_code=str(row.get("postal_code", "") or ""),
            country=str(row.get("country", "") or ""),
            lat=float(row.get("lat", 0) or 0),
            lng=float(row.get("lng", 0) or 0),
            phone=str(row.get("phone", "") or ""),
            international_phone=str(row.get("international_phone", "") or ""),
            website=str(row.get("website", "") or ""),
            google_maps_url=str(row.get("google_maps_url", "") or ""),
            types=str(row.get("types", "")).split("|")
            if pd.notna(row.get("types"))
            else [],
            primary_type=str(row.get("primary_type", "") or ""),
            rating=float(row.get("rating", 0) or 0),
            total_reviews=int(row.get("total_reviews", 0) or 0),
            has_website=bool(row.get("has_website", False)),
            website_status=str(row.get("website_status", "") or ""),
            lead_score=int(row.get("lead_score", 0) or 0),
            lead_priority=str(row.get("lead_priority", "") or ""),
            scraped_at=str(row.get("scraped_at", "") or ""),
        )
        b.vertical = str(row.get("vertical", "") or "")
        all_businesses[pid] = b
    console.print(f"Loaded [green]{len(existing_ids)}[/green] existing businesses")

new_total = 0


def fetch_details(pid):
    if pid in all_businesses or pid in existing_ids:
        return False
    details = client.get_place_details(pid)
    if details:
        b = client.parse_place(details, include_reviews=True)
        b.scraped_at = datetime.now().isoformat()
        all_businesses[pid] = b
        existing_ids.add(pid)
        return True
    return False


# Phase 1: Extended keyword searches (focused, high-yield)
KEYWORDS = [
    "maquillaje social Asuncion",
    "extensiones cabello Asuncion",
    "microblading Asuncion",
    "uñas gel Asuncion",
    "uñas acrilicas Asuncion",
    "keratina Asuncion",
    "balayage Asuncion",
    "peinados novia Asuncion",
    "lifting pestañas Asuncion",
    "cejas pestañas Asuncion",
    "cosmiatra Asuncion",
    "criolipolisis Asuncion",
    "cavitacion Asuncion",
    "tratamiento reductor Asuncion",
    "bronceado Asuncion",
    "piercing Asuncion",
    "estudio belleza Asuncion",
    "salon uñas Asuncion",
    "colorista Asuncion",
    "estilista Asuncion",
    "peluqueria unisex Asuncion",
    "beauty parlor Asuncion",
    "salon de belleza Fernando de la Mora",
    "peluqueria San Lorenzo",
    "barberia Luque",
    "spa Lambare",
    "nails Capiata",
    "salon belleza Nemby",
    "barberia Mariano Roque Alonso",
    "peluqueria Limpio",
    "tattoo studio Asuncion",
    "body art Asuncion",
    "permanent makeup Asuncion",
    "alisado definitivo Asuncion",
    "botox Asuncion",
    "acido hialuronico Asuncion",
    "tratamiento facial Asuncion",
    "radiofrecuencia Asuncion",
    "masaje terapeutico Asuncion",
    "depilacion laser Asuncion",
    "salon de belleza Villa Elisa",
    "barber shop Luque",
    "nail spa San Lorenzo",
    "peluqueria Itaugua",
    "estetica Ypane",
]

console.print(
    f"\n[bold]Phase 1:[/bold] Extended keyword search ({len(KEYWORDS)} queries)"
)

with Progress(
    SpinnerColumn(),
    TextColumn("{task.description}"),
    BarColumn(),
    TextColumn("{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    t = progress.add_task("Keywords...", total=len(KEYWORDS))
    for kw in KEYWORDS:
        results = client.text_search(query=kw, location=ASUNCION_CENTER, radius=50000)
        found = 0
        for p in results:
            if fetch_details(p.get("place_id", "")):
                found += 1
                new_total += 1
        progress.console.print(
            f"  '{kw[:45]}' → {found} new | total: {len(all_businesses)}",
            highlight=False,
        )
        progress.advance(t)

console.print(
    f"After keywords: [green]+{new_total}[/green] new → Total: {len(all_businesses)}"
)

# Phase 2: Nearby search grid - broader, using place types
console.print(
    f"\n[bold]Phase 2:[/bold] Grid nearby search (beauty_salon, hair_care, spa)"
)

GRID_BOUNDS = (-25.50, -57.80, -25.10, -57.35)
step = 0.02
points = []
lat = GRID_BOUNDS[0]
while lat <= GRID_BOUNDS[2]:
    lng = GRID_BOUNDS[1]
    while lng <= GRID_BOUNDS[3]:
        points.append((round(lat, 4), round(lng, 4)))
        lng += step
    lat += step

console.print(f"  Grid: {len(points)} points × 3 types")

grid_new = 0
with Progress(
    SpinnerColumn(),
    TextColumn("{task.description}"),
    BarColumn(),
    TextColumn("{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    t2 = progress.add_task("Grid...", total=len(points))
    for lat, lng in points:
        for ptype in ["beauty_salon", "hair_care", "spa"]:
            places, _ = client.nearby_search(
                lat=lat, lng=lng, radius=2000, place_type=ptype
            )
            for p in places:
                if fetch_details(p.get("place_id", "")):
                    grid_new += 1
                    new_total += 1
        progress.advance(t2)

console.print(
    f"After grid: [green]+{grid_new}[/green] new → Total: {len(all_businesses)}"
)

# Phase 3: Paginated nearby for dense areas
console.print(f"\n[bold]Phase 3:[/bold] Deep paginated search in dense areas")

DENSE_AREAS = [
    ("Centro", -25.2637, -57.5759),
    ("Villa Morra", -25.2480, -57.5650),
    ("Recoleta", -25.2670, -57.5630),
    ("Canógrafa", -25.2750, -57.5750),
    ("Santa Ana", -25.2850, -57.6350),
    ("San Lorenzo", -25.3400, -57.5200),
    ("Fernando Mora", -25.3300, -57.5200),
    ("Luque", -25.2500, -57.5000),
]

deep_new = 0
for area_name, lat, lng in DENSE_AREAS:
    for ptype in ["beauty_salon", "hair_care"]:
        page_token = None
        pages = 0
        while pages < 3:
            places, next_token = client.nearby_search(
                lat=lat,
                lng=lng,
                radius=2000,
                place_type=ptype,
                page_token=page_token,
            )
            for p in places:
                if fetch_details(p.get("place_id", "")):
                    deep_new += 1
                    new_total += 1
            page_token = next_token
            pages += 1
            if not page_token:
                break
    console.print(f"  {area_name}: total now {len(all_businesses)}")

console.print(
    f"After deep search: [green]+{deep_new}[/green] new → Total: {len(all_businesses)}"
)

# Final analysis + export
businesses = list(all_businesses.values())
console.print(f"\n{'=' * 60}")
console.print(
    f"FINAL TOTAL: {len(businesses)} unique beauty businesses", highlight=False
)
console.print(f"New this run: +{new_total}")
console.print(f"API requests: {client.requests_count}")
console.print(f"{'=' * 60}")

console.print(f"\n[bold]Analyzing...")
analyzer = BusinessAnalyzer(businesses)
analyzer.analyze_all(check_websites=True)
summary = analyzer.get_summary()

wa = summary["website_analysis"]
leads = summary["leads"]
console.print(
    f"\n  Total: {summary['total_businesses']} | Avg rating: {summary['avg_rating']} | Reviews: {summary['total_reviews_sum']:,}"
)
console.print(
    f"  No website: {wa['no_website']} ({wa['pct_no_website']}%) | Social only: {wa['social_media_only']}"
)
console.print(
    f"  HIGH leads: {leads['high_priority']} | MEDIUM: {leads['medium_priority']} | Total leads: {leads['total_potential_leads']}"
)

if summary.get("by_neighborhood"):
    console.print(f"\n  Top neighborhoods:")
    for n, c in sorted(summary["by_neighborhood"].items(), key=lambda x: -x[1])[:15]:
        console.print(f"    {n}: {c}", highlight=False)

console.print(f"\n[bold]Exporting...")
exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="beauty_complete")
console.print(f"\n[bold green]Files:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")
console.print(f"\nDone! API requests: {client.requests_count}")
