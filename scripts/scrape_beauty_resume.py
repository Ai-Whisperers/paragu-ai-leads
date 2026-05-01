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

from src.config import GOOGLE_MAPS_API_KEY, ASUNCION_CENTER
from src.api_client import PlacesClient
from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter
from src.models import Business

import pandas as pd

console = Console()
logging.basicConfig(level=logging.WARNING)

CHECKPOINT = "data/beauty_checkpoint.json"


def load_checkpoint():
    if Path(CHECKPOINT).exists():
        with open(CHECKPOINT) as f:
            data = json.load(f)
        return set(data.get("ids", [])), data.get("businesses_raw", {})
    return set(), {}


def save_checkpoint(existing_ids, all_businesses):
    raw = {}
    for pid, b in all_businesses.items():
        raw[pid] = {
            "place_id": b.place_id,
            "name": b.name,
            "status": b.status,
            "address": b.address,
            "street_number": b.street_number,
            "street_name": b.street_name,
            "neighborhood": b.neighborhood,
            "city": b.city,
            "state": b.state,
            "postal_code": b.postal_code,
            "country": b.country,
            "lat": b.lat,
            "lng": b.lng,
            "phone": b.phone,
            "international_phone": b.international_phone,
            "website": b.website,
            "google_maps_url": b.google_maps_url,
            "types": b.types,
            "primary_type": b.primary_type,
            "rating": b.rating,
            "total_reviews": b.total_reviews,
            "has_website": b.has_website,
            "website_status": b.website_status,
            "lead_score": b.lead_score,
            "lead_priority": b.lead_priority,
            "scraped_at": b.scraped_at,
        }
    with open(CHECKPOINT, "w") as f:
        json.dump({"ids": list(existing_ids), "businesses_raw": raw}, f)


def raw_to_business(raw):
    r = raw
    b = Business(
        place_id=r["place_id"],
        name=r.get("name", ""),
        status=r.get("status", ""),
        address=r.get("address", ""),
        lat=r.get("lat", 0),
        lng=r.get("lng", 0),
        phone=r.get("phone", ""),
        website=r.get("website", ""),
        types=r.get("types", []),
        primary_type=r.get("primary_type", ""),
        rating=r.get("rating", 0),
        total_reviews=r.get("total_reviews", 0),
        has_website=r.get("has_website", False),
        website_status=r.get("website_status", ""),
        lead_score=r.get("lead_score", 0),
        lead_priority=r.get("lead_priority", ""),
        scraped_at=r.get("scraped_at", ""),
    )
    b.neighborhood = r.get("neighborhood", "")
    b.vertical = "Beauty & Wellness"
    return b


existing_ids, raw_data = load_checkpoint()
all_businesses = {}
for pid, raw in raw_data.items():
    all_businesses[pid] = raw_to_business(raw)

console.print(f"Loaded checkpoint: [green]{len(all_businesses)}[/green] businesses")

client = PlacesClient(GOOGLE_MAPS_API_KEY)


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


def save():
    save_checkpoint(existing_ids, all_businesses)
    console.print(f"  [dim]Checkpoint saved: {len(all_businesses)} businesses[/dim]")


# Resume keywords from where we left off
REMAINING_KEYWORDS = [
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
    "gimnasio Asuncion",
    "yoga Asuncion",
    "pilates Asuncion",
    "crossfit Asuncion",
    "gym Asuncion",
    "entrenador personal Asuncion",
    "centro wellness Asuncion",
    "tattoo Asuncion",
    "tatuaje Asuncion",
]

console.print(f"\n[bold]Phase 1:[/bold] Remaining keywords ({len(REMAINING_KEYWORDS)})")

for kw in REMAINING_KEYWORDS:
    results = client.text_search(query=kw, location=ASUNCION_CENTER, radius=50000)
    found = 0
    for p in results:
        if fetch_details(p.get("place_id", "")):
            found += 1
    console.print(
        f"  '{kw[:45]}' → +{found} | total: {len(all_businesses)}", highlight=False
    )

save()

# Grid search - coarse only
console.print(f"\n[bold]Phase 2:[/bold] Coarse grid nearby search")

step = 0.025
lat = -25.50
points = []
while lat <= -25.10:
    lng = -57.80
    while lng <= -57.35:
        points.append((round(lat, 4), round(lng, 4)))
        lng += step
    lat += step

console.print(f"  {len(points)} grid points × 3 types")

grid_new = 0
with Progress(
    SpinnerColumn(),
    TextColumn("{task.description}"),
    BarColumn(),
    TextColumn("{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    t = progress.add_task("Grid...", total=len(points))
    for lat, lng in points:
        for ptype in ["beauty_salon", "hair_care", "spa"]:
            places, _ = client.nearby_search(
                lat=lat, lng=lng, radius=3000, place_type=ptype
            )
            for p in places:
                if fetch_details(p.get("place_id", "")):
                    grid_new += 1
        progress.advance(t)
        # Save every 50 points
        if grid_new > 0 and progress.tasks[0].completed % 50 == 0:
            save()
            grid_new = 0

save()

console.print(f"\n{'=' * 60}")
console.print(f"FINAL: {len(all_businesses)} unique beauty businesses", highlight=False)
console.print(f"API requests: {client.requests_count}")
console.print(f"{'=' * 60}")

console.print(f"\n[bold]Analyzing + exporting...")
businesses = list(all_businesses.values())
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
    f"  HIGH: {leads['high_priority']} | MEDIUM: {leads['medium_priority']} | Total leads: {leads['total_potential_leads']}"
)

if summary.get("by_neighborhood"):
    console.print(f"\n  Top neighborhoods:")
    for n, c in sorted(summary["by_neighborhood"].items(), key=lambda x: -x[1])[:20]:
        console.print(f"    {n}: {c}", highlight=False)

exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="beauty_complete")
console.print(f"\n[bold green]Exported:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")

console.print(f"\nDone! API: {client.requests_count}")
