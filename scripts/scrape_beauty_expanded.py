#!/usr/bin/env python3
import time
import json
import csv
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

EXPANDED_KEYWORDS = [
    "salon de belleza Asuncion",
    "peluqueria Asuncion",
    "barberia Asuncion",
    "spa Asuncion",
    "nails Asuncion",
    "centro de estetica Asuncion",
    "estetica facial Asuncion",
    "manicura Asuncion",
    "pedicura Asuncion",
    "barber shop Asuncion",
    "hair salon Asuncion",
    "tatuajes Asuncion",
    "depilacion Asuncion",
    "masajes Asuncion",
    "maquillaje Asuncion",
    "extensiones de cabello Asuncion",
    "tinte de cabello Asuncion",
    "cortes de pelo Asuncion",
    "cejas pestañas Asuncion",
    "lifting de pestañas Asuncion",
    "microblading Asuncion",
    "uñas esculpidas Asuncion",
    "uñas gel Asuncion",
    "uñas acrilicas Asuncion",
    "tratamiento capilar Asuncion",
    "alisado Asuncion",
    "keratina Asuncion",
    "balayage Asuncion",
    "mechas Asuncion",
    "peinados novia Asuncion",
    "maquillaje social Asuncion",
    "belleza integral Asuncion",
    "cosmiatra Asuncion",
    "limpieza facial Asuncion",
    "radiofrecuencia Asuncion",
    "criolipolisis Asuncion",
    "cavitacion Asuncion",
    "massage terapeutico Asuncion",
    "masaje relajante Asuncion",
    "spa corporal Asuncion",
    "tratamiento reductor Asuncion",
    "bronceado Asuncion",
    "piercing Asuncion",
    "estetica canina Asuncion",
    "peluqueria unisex Asuncion",
    "barberia moderna Asuncion",
    "nail art Asuncion",
    "estudio de belleza Asuncion",
    "centro de belleza Asuncion",
    "salon de uñas Asuncion",
    "beauty salon",
    "hair care",
    "beauty parlor",
    "grooming Asuncion",
    "estilista Asuncion",
    "colorista Asuncion",
    "barber Asuncion",
    "belleza y salud Asuncion",
    "salon de belleza Fernando de la Mora",
    "peluqueria San Lorenzo",
    "barberia Luque",
    "spa Lambare",
    "nails Capiata",
    "salon de belleza Nemby",
    "peluqueria Mariano Roque Alonso",
    "barberia Limpio",
    "spa Villa Elisa",
    "salon de belleza Minga Guazu",
    "peluqueria Cnel Oviedo",
    "beauty salon Fernando de la Mora",
    "barber shop San Lorenzo",
    "nail spa Luque",
    "tattoo Asuncion",
    "tattoo studio Asuncion",
    "body art Asuncion",
    "permanent makeup Asuncion",
]

SEARCH_AREAS = [
    ("Asunción Centro", (-25.2637, -57.5759), 25000),
    ("Villa Morra/Carmelitas", (-25.2510, -57.5670), 15000),
    ("Recoleta/Sajonia", (-25.2680, -57.5740), 12000),
    ("Canógrafa/Pettirossi", (-25.2750, -57.5900), 15000),
    ("Santa Ana/Tte Fariña", (-25.2830, -57.6270), 15000),
    ("San Jorge", (-25.2530, -57.5900), 8000),
    ("Luque", (-25.2500, -57.5000), 15000),
    ("San Lorenzo", (-25.3400, -57.5200), 15000),
    ("Fernando de la Mora", (-25.3300, -57.5200), 12000),
    ("Lambaré", (-25.3400, -57.6300), 12000),
    ("Capiatá", (-25.3600, -57.4400), 15000),
    ("Ñemby", (-25.3900, -57.5400), 12000),
    ("Mariano Roque Alonso", (-25.2100, -57.5500), 15000),
    ("Limpio", (-25.1700, -57.4800), 15000),
    ("Villa Elisa", (-25.3700, -57.5600), 10000),
    ("Guaraní", (-25.3200, -57.5800), 8000),
    ("Ypane", (-25.4200, -57.5500), 12000),
    ("Itauguá", (-25.3800, -57.3500), 15000),
]

console.print(
    Panel.fit(
        "[bold cyan]Expanded Beauty Scraper - Greater Asunción[/bold cyan]\n"
        "[dim]Skip existing · More keywords · Wider area coverage[/dim]",
        border_style="cyan",
    )
)

client = PlacesClient(GOOGLE_MAPS_API_KEY)
all_businesses = {}

# Load existing data
existing_path = Path(EXISTING_DATA)
if existing_path.exists():
    import pandas as pd

    df_existing = pd.read_csv(existing_path)
    existing_ids = set(df_existing["place_id"].tolist())
    console.print(
        f"\nLoaded [green]{len(existing_ids)}[/green] existing businesses to skip"
    )
else:
    existing_ids = set()
    console.print("\n[yellow]No existing data found - starting fresh[/yellow]")

# Load existing into all_businesses so they get included in final export
if existing_path.exists():
    from src.models import Business

    for _, row in df_existing.iterrows():
        b = Business(
            place_id=row.get("place_id", ""),
            name=row.get("name", ""),
            status=row.get("status", ""),
            address=row.get("address", ""),
            street_number=row.get("street_number", ""),
            street_name=row.get("street_name", ""),
            neighborhood=row.get("neighborhood", ""),
            city=row.get("city", ""),
            state=row.get("state", ""),
            postal_code=row.get("postal_code", ""),
            country=row.get("country", ""),
            lat=float(row.get("lat", 0) or 0),
            lng=float(row.get("lng", 0) or 0),
            phone=str(row.get("phone", "") or ""),
            international_phone=str(row.get("international_phone", "") or ""),
            website=str(row.get("website", "") or ""),
            google_maps_url=str(row.get("google_maps_url", "") or ""),
            google_maps_direction_url=str(
                row.get("google_maps_direction_url", "") or ""
            ),
            types=str(row.get("types", "")).split("|")
            if pd.notna(row.get("types"))
            else [],
            primary_type=str(row.get("primary_type", "") or ""),
            rating=float(row.get("rating", 0) or 0),
            total_reviews=int(row.get("total_reviews", 0) or 0),
            has_website=bool(row.get("has_website", False)),
            website_status=str(row.get("website_status", "") or ""),
            website_is_social_only=bool(row.get("website_is_social_only", False)),
            website_is_free_builder=bool(row.get("website_is_free_builder", False)),
            website_uses_https=bool(row.get("website_uses_https", False)),
            website_redirects_to_social=bool(
                row.get("website_redirects_to_social", False)
            ),
            lead_score=int(row.get("lead_score", 0) or 0),
            lead_priority=str(row.get("lead_priority", "") or ""),
            scraped_at=str(row.get("scraped_at", "") or ""),
        )
        b.vertical = str(row.get("vertical", "") or "")
        all_businesses[b.place_id] = b

console.print(
    f"Starting with [green]{len(all_businesses)}[/green] total businesses loaded"
)

new_count = 0
skipped_count = 0
total_searched = 0

console.print(
    f"\n[bold]Step 1:[/bold] Keyword search ({len(EXPANDED_KEYWORDS)} keywords)"
)

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    task = progress.add_task("Keywords...", total=len(EXPANDED_KEYWORDS))

    for keyword in EXPANDED_KEYWORDS:
        results = client.text_search(
            query=keyword,
            location=ASUNCION_CENTER,
            radius=50000,
        )
        total_searched += len(results)

        for place in results:
            pid = place.get("place_id", "")
            if pid in all_businesses or pid in existing_ids:
                skipped_count += 1
                continue

            details = client.get_place_details(pid)
            if details:
                business = client.parse_place(details, include_reviews=True)
                business.scraped_at = datetime.now().isoformat()
                all_businesses[pid] = business
                new_count += 1
                existing_ids.add(pid)

        progress.advance(task)

console.print(
    f"  After keywords: [green]{new_count}[/green] new, {skipped_count} skipped → Total: {len(all_businesses)}"
)

console.print(
    f"\n[bold]Step 2:[/bold] Area-specific search ({len(SEARCH_AREAS)} areas)"
)

area_new = 0
with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    task2 = progress.add_task("Areas...", total=len(SEARCH_AREAS))

    for area_name, (lat, lng), radius in SEARCH_AREAS:
        area_queries = [
            "salon de belleza",
            "peluqueria",
            "barberia",
            "spa",
            "nails",
            "estetica",
            "uñas",
            "tatuajes",
            "masajes",
            "beauty salon",
        ]

        for query in area_queries:
            results = client.text_search(
                query=f"{query}",
                location=(lat, lng),
                radius=radius,
            )
            total_searched += len(results)

            for place in results:
                pid = place.get("place_id", "")
                if pid in all_businesses or pid in existing_ids:
                    skipped_count += 1
                    continue

                details = client.get_place_details(pid)
                if details:
                    business = client.parse_place(details, include_reviews=True)
                    business.scraped_at = datetime.now().isoformat()
                    all_businesses[pid] = business
                    area_new += 1
                    new_count += 1
                    existing_ids.add(pid)

        progress.console.print(
            f"  {area_name}: total now [green]{len(all_businesses)}[/green]"
        )
        progress.advance(task2)

console.print(
    f"\n  After areas: [green]{area_new}[/green] new from area search → Total: {len(all_businesses)}"
)

console.print(f"\n[bold]Step 3:[/bold] Nearby grid search for missed spots")

GRID_AREAS = [
    ("Asunción full", -25.40, -57.72, -25.16, -57.55),
    ("Greater Asunción", -25.50, -57.80, -25.10, -57.35),
]

grid_new = 0
for area_name, south, west, north, east in GRID_AREAS:
    step = 0.015
    points = []
    lat = south
    while lat <= north:
        lng = west
        while lng <= east:
            points.append((lat, lng))
            lng += step
        lat += step

    console.print(f"  {area_name}: {len(points)} grid points")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task3 = progress.add_task(f"Grid {area_name}...", total=len(points))

        for lat, lng in points:
            for ptype in ["beauty_salon", "hair_care", "spa"]:
                places, _ = client.nearby_search(
                    lat=lat,
                    lng=lng,
                    radius=1500,
                    place_type=ptype,
                )
                total_searched += len(places)

                for place in places:
                    pid = place.get("place_id", "")
                    if pid in all_businesses or pid in existing_ids:
                        skipped_count += 1
                        continue

                    details = client.get_place_details(pid)
                    if details:
                        business = client.parse_place(details, include_reviews=True)
                        business.scraped_at = datetime.now().isoformat()
                        all_businesses[pid] = business
                        grid_new += 1
                        new_count += 1
                        existing_ids.add(pid)

            progress.advance(task3)

console.print(
    f"  After grid: [green]{grid_new}[/green] new → Total: {len(all_businesses)}"
)

businesses = list(all_businesses.values())
console.print(f"\n{'=' * 60}")
console.print(
    f"[bold green]FINAL TOTAL: {len(businesses)} unique beauty businesses[/bold green]"
)
console.print(f"  New in this run: {new_count}")
console.print(f"  From previous run: {len(all_businesses) - new_count}")
console.print(f"  API requests used: {client.requests_count}")
console.print(f"  Total results scanned: {total_searched}")
console.print(f"{'=' * 60}")

console.print(f"\n[bold]Analyzing all businesses...")
analyzer = BusinessAnalyzer(businesses)
analyzer.analyze_all(check_websites=True)
summary = analyzer.get_summary()

console.print(f"\n")
console.print(
    Panel(
        "[bold]Beauty & Wellness - FULL Asunción Results[/bold]", border_style="green"
    )
)
console.print(f"  Total businesses: {summary['total_businesses']}")
console.print(f"  Average rating: {summary['avg_rating']}")
console.print(f"  Total reviews: {summary['total_reviews_sum']:,}")

wa = summary["website_analysis"]
console.print(f"\n  Website Analysis:")
console.print(f"    No website: {wa['no_website']} ({wa['pct_no_website']}%)")
console.print(f"    Social media only: {wa['social_media_only']}")
console.print(f"    Free builder: {wa['free_builder_site']}")
console.print(f"    Unreachable/broken: {wa['unreachable_or_broken']}")
console.print(f"    Has working website: {wa['has_working_website']}")

leads = summary["leads"]
console.print(f"\n  Lead Generation:")
console.print(f"    HIGH priority: {leads['high_priority']}")
console.print(f"    MEDIUM priority: {leads['medium_priority']}")
console.print(f"    Total potential leads: {leads['total_potential_leads']}")

if summary.get("by_neighborhood"):
    console.print(f"\n  By Neighborhood:")
    for neigh, count in sorted(summary["by_neighborhood"].items(), key=lambda x: -x[1])[
        :20
    ]:
        console.print(f"    {neigh}: {count}", highlight=False)

console.print(f"\n[bold]Exporting...")
exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="beauty_full")
console.print(f"\n[bold green]Exported files:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")

console.print(f"\n[bold]Done! Total API requests: {client.requests_count}[/bold]")
