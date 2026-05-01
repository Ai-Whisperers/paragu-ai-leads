#!/usr/bin/env python3
import json
import logging
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from src.config import GOOGLE_MAPS_API_KEY
from src.api_client import PlacesClient
from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter
from src.models import Business

import pandas as pd

console = Console()
logging.basicConfig(level=logging.WARNING)

client = PlacesClient(GOOGLE_MAPS_API_KEY)

all_businesses = {}
existing_ids = set()

# Load all CSV files we have
csv_files = [
    "data/asuncion_beauty_all_businesses_20260414_185314.csv",
]

# Load checkpoint
checkpoint = "data/beauty_checkpoint.json"
if Path(checkpoint).exists():
    with open(checkpoint) as f:
        data = json.load(f)
    raw = data.get("businesses_raw", {})
    for pid, r in raw.items():
        existing_ids.add(pid)
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
        b.international_phone = r.get("international_phone", "")
        b.google_maps_url = r.get("google_maps_url", "")
        b.street_number = r.get("street_number", "")
        b.street_name = r.get("street_name", "")
        b.city = r.get("city", "")
        b.state = r.get("state", "")
        b.country = r.get("country", "")
        b.vertical = "Beauty & Wellness"
        all_businesses[pid] = b

# Load CSV files
for csvf in csv_files:
    if not Path(csvf).exists():
        continue
    df = pd.read_csv(csvf)
    for _, row in df.iterrows():
        pid = str(row.get("place_id", ""))
        if not pid or pid in existing_ids:
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

console.print(
    f"Loaded: [green]{len(all_businesses)}[/green] businesses total from existing data"
)

# Now do targeted deep dives in areas we haven't covered well
DEEP_KEYWORDS = [
    "salon de belleza Lambaré",
    "peluqueria Capiata",
    "barberia Nemby",
    "spa Mariano Roque Alonso",
    "estetica Limpio",
    "uñas Villa Elisa",
    "peluqueria Luque centro",
    "barberia San Lorenzo centro",
    "salon belleza Ypane",
    "depilacion Fernando de la Mora",
    "maquillaje San Lorenzo",
    "tatuajes Capiata",
    "masajes Luque",
    "belleza Itaugua",
    "nails Lambare",
    "peluqueria Villa Elisa",
    "spa Fernando de la Mora",
    "barberia Asuncion centro",
    "salon uñas San Lorenzo",
    "estetica corporal Asuncion",
    "tratamiento capilar Asuncion",
    "corte de cabello Asuncion",
    "alisado Asuncion",
    "tinte Asuncion",
    "mechas Asuncion",
    "extensiones Asuncion",
    "cejas microblading Asuncion",
    "uñas pintadas Asuncion",
    "spa facial Asuncion",
    "masaje Asuncion",
    "sauna Asuncion",
    "tratamiento corporal Asuncion",
    "reduccion medidas Asuncion",
]

new_count = 0
console.print(f"\n[bold]Deep keyword dive:[/bold] {len(DEEP_KEYWORDS)} new queries")

for kw in DEEP_KEYWORDS:
    results = client.text_search(query=kw, location=(-25.2637, -57.5759), radius=50000)
    found = 0
    for p in results:
        pid = p.get("place_id", "")
        if pid in existing_ids:
            continue
        details = client.get_place_details(pid)
        if details:
            b = client.parse_place(details, include_reviews=True)
            b.scraped_at = datetime.now().isoformat()
            all_businesses[pid] = b
            existing_ids.add(pid)
            found += 1
            new_count += 1
    console.print(
        f"  '{kw[:45]}' → +{found} | total: {len(all_businesses)}", highlight=False
    )

console.print(f"\n[bold]New from this run: +{new_count}")

# Final: paginated nearby for top areas
console.print(f"\n[bold]Final pass:[/bold] Paginated nearby in dense zones")

DENSE = [
    ("Canógrafa deep", -25.2750, -57.5900),
    ("Centro deep", -25.2637, -57.5759),
    ("Recoleta deep", -25.2670, -57.5630),
    ("San Lorenzo", -25.3400, -57.5200),
    ("Luque", -25.2500, -57.5000),
    ("Fernando Mora", -25.3300, -57.5200),
    ("Lambaré", -25.3400, -57.6300),
    ("Capiatá", -25.3600, -57.4400),
    ("Ñemby", -25.3900, -57.5400),
]

dense_new = 0
for area_name, lat, lng in DENSE:
    for ptype in ["beauty_salon", "hair_care", "spa"]:
        page_token = None
        for _ in range(3):
            places, next_token = client.nearby_search(
                lat=lat,
                lng=lng,
                radius=2500,
                place_type=ptype,
                page_token=page_token,
            )
            for p in places:
                pid = p.get("place_id", "")
                if pid in existing_ids:
                    continue
                details = client.get_place_details(pid)
                if details:
                    b = client.parse_place(details, include_reviews=True)
                    b.scraped_at = datetime.now().isoformat()
                    all_businesses[pid] = b
                    existing_ids.add(pid)
                    dense_new += 1
                    new_count += 1
            page_token = next_token
            if not page_token:
                break
    console.print(f"  {area_name}: +{dense_new} new | total: {len(all_businesses)}")
    dense_new = 0

# Analyze & export
businesses = list(all_businesses.values())
console.print(f"\n{'=' * 60}")
console.print(
    f"FINAL TOTAL: {len(businesses)} unique beauty + wellness businesses",
    highlight=False,
)
console.print(f"API requests: {client.requests_count}")
console.print(f"{'=' * 60}")

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
    f"  Broken: {wa['unreachable_or_broken']} | Free builder: {wa['free_builder_site']}"
)
console.print(f"  Working sites: {wa['has_working_website']}")
console.print(
    f"  HIGH leads: {leads['high_priority']} | MEDIUM: {leads['medium_priority']} | Total: {leads['total_potential_leads']}"
)

if summary.get("by_neighborhood"):
    console.print(f"\n  Top neighborhoods:")
    for n, c in sorted(summary["by_neighborhood"].items(), key=lambda x: -x[1])[:20]:
        console.print(f"    {n}: {c}", highlight=False)

# Top leads table
from rich.table import Table

table = Table(title="Top 25 Leads", show_lines=True)
table.add_column("Name", style="bold", max_width=30)
table.add_column("Neighborhood", max_width=16)
table.add_column("Rating", justify="center")
table.add_column("Reviews", justify="right")
table.add_column("Website", max_width=16)
table.add_column("Score", justify="center", style="bold green")
table.add_column("Phone", max_width=16)

high_leads = sorted(
    [b for b in businesses if b.lead_priority == "HIGH"],
    key=lambda b: b.lead_score,
    reverse=True,
)
for b in high_leads[:25]:
    ws = "NO WEBSITE" if b.website_status == "no_website" else b.website_status[:16]
    table.add_row(
        b.name[:30].replace("[", "(").replace("]", ")"),
        b.neighborhood[:16].replace("[", "(").replace("]", ")"),
        f"{b.rating:.1f}" if b.rating else "-",
        str(b.total_reviews),
        ws,
        str(b.lead_score),
        (b.phone or "-")[:16],
    )
console.print(table)

exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="beauty_complete")
console.print(f"\n[bold green]Files:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")
