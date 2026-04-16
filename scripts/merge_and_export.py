#!/usr/bin/env python3
import json
import logging
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter
from src.models import Business

import pandas as pd

console = Console()

all_businesses = {}
existing_ids = set()

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

# Load all CSV files
for csvf in Path("data").glob("asuncion_beauty_*_all_businesses_*.csv"):
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
            lat=float(row.get("lat", 0) or 0),
            lng=float(row.get("lng", 0) or 0),
            phone=str(row.get("phone", "") or ""),
            website=str(row.get("website", "") or ""),
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
        )
        b.neighborhood = str(row.get("neighborhood", "") or "")
        b.international_phone = str(row.get("international_phone", "") or "")
        b.google_maps_url = str(row.get("google_maps_url", "") or "")
        b.city = str(row.get("city", "") or "")
        b.state = str(row.get("state", "") or "")
        b.country = str(row.get("country", "") or "")
        b.vertical = str(row.get("vertical", "") or "Beauty & Wellness")
        all_businesses[pid] = b

businesses = list(all_businesses.values())
console.print(
    Panel.fit(
        f"[bold cyan]Beauty & Wellness - Complete Asuncion Data[/bold cyan]\n"
        f"[dim]{len(businesses)} unique businesses loaded[/dim]",
        border_style="cyan",
    )
)

analyzer = BusinessAnalyzer(businesses)
analyzer.analyze_all(check_websites=True)
summary = analyzer.get_summary()

wa = summary["website_analysis"]
leads = summary["leads"]

console.print(f"\n  [bold]Total businesses:[/bold] {summary['total_businesses']}")
console.print(f"  [bold]Average rating:[/bold] {summary['avg_rating']}")
console.print(f"  [bold]Total reviews:[/bold] {summary['total_reviews_sum']:,}")
console.print(f"\n  [bold yellow]Website Analysis:[/bold yellow]")
console.print(f"    No website: {wa['no_website']} ({wa['pct_no_website']}%)")
console.print(f"    Social media only: {wa['social_media_only']}")
console.print(f"    Free builder: {wa['free_builder_site']}")
console.print(f"    Unreachable/broken: {wa['unreachable_or_broken']}")
console.print(f"    Has working website: {wa['has_working_website']}")
console.print(f"\n  [bold green]Lead Generation:[/bold green]")
console.print(
    f"    HIGH: {leads['high_priority']} | MEDIUM: {leads['medium_priority']} | Total: {leads['total_potential_leads']}"
)

if summary.get("by_neighborhood"):
    console.print(f"\n  [bold]By Neighborhood:[/bold]")
    for n, c in sorted(summary["by_neighborhood"].items(), key=lambda x: -x[1])[:25]:
        console.print(f"    {n}: {c}", highlight=False)

if summary.get("by_vertical"):
    console.print(f"\n  [bold]By Vertical:[/bold]")
    for v, c in sorted(summary["by_vertical"].items(), key=lambda x: -x[1]):
        console.print(f"    {v}: {c}", highlight=False)

table = Table(title="Top 30 Leads (Score 85+)", show_lines=True)
table.add_column("#", justify="right", width=3)
table.add_column("Name", style="bold", max_width=32)
table.add_column("Neighborhood", max_width=16)
table.add_column("Rat", justify="center", width=4)
table.add_column("Rev", justify="right", width=5)
table.add_column("Website", max_width=16)
table.add_column("Score", justify="center", style="bold green", width=5)
table.add_column("Phone", max_width=16)

high_leads = sorted(
    [b for b in businesses if b.lead_priority == "HIGH"],
    key=lambda b: (-b.lead_score, -b.total_reviews),
)
for i, b in enumerate(high_leads[:30], 1):
    ws = "NO WEBSITE" if b.website_status == "no_website" else b.website_status[:16]
    table.add_row(
        str(i),
        b.name[:32].replace("[", "(").replace("]", ")"),
        b.neighborhood[:16].replace("[", "(").replace("]", ")"),
        f"{b.rating:.1f}" if b.rating else "-",
        str(b.total_reviews),
        ws,
        str(b.lead_score),
        (b.phone or "-")[:16],
    )
console.print(table)

# Count businesses with phone (contactable)
with_phone = sum(1 for b in businesses if b.phone and b.phone.strip())
high_with_phone = sum(1 for b in high_leads if b.phone and b.phone.strip())
console.print(f"\n  Contactable (have phone): {with_phone}/{len(businesses)}")
console.print(f"  HIGH leads with phone: {high_with_phone}/{len(high_leads)}")

exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="beauty_complete")
console.print(f"\n[bold green]Exported:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")
