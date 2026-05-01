#!/usr/bin/env python3
import json
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from src.api_client import PlacesClient
from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter
from src.models import Business

import pandas as pd

console = Console()

all_businesses = {}
existing_ids = set()

# Load nationwide checkpoint
cp = "data/py_beauty_checkpoint.json"
if Path(cp).exists():
    with open(cp) as f:
        data = json.load(f)
    raw = data.get("businesses", {})
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
        for k in [
            "neighborhood",
            "city",
            "state",
            "country",
            "international_phone",
            "google_maps_url",
            "street_number",
            "street_name",
            "postal_code",
            "vertical",
            "website_is_social_only",
            "website_is_free_builder",
            "website_uses_https",
            "website_redirects_to_social",
            "icon",
            "editorial_summary",
            "saturday_hours",
            "sunday_hours",
        ]:
            setattr(b, k, r.get(k, "") or "")
        b.is_open_now = r.get("is_open_now")
        b.price_level = r.get("price_level")
        b.photo_count = r.get("photo_count", 0)
        all_businesses[pid] = b

# Load all existing CSV files
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
        b.city = str(row.get("city", "") or "")
        b.neighborhood = str(row.get("neighborhood", "") or "")
        b.state = str(row.get("state", "") or "")
        b.country = str(row.get("country", "") or "")
        b.international_phone = str(row.get("international_phone", "") or "")
        b.google_maps_url = str(row.get("google_maps_url", "") or "")
        b.vertical = str(row.get("vertical", "") or "Beauty & Wellness")
        all_businesses[pid] = b

businesses = list(all_businesses.values())

console.print(
    Panel.fit(
        f"[bold cyan]Paraguay Nationwide Beauty & Wellness[/bold cyan]\n"
        f"[dim]{len(businesses)} unique businesses loaded[/dim]",
        border_style="cyan",
    )
)

console.print(f"\n[bold]Analyzing {len(businesses)} businesses (website checks)...")
analyzer = BusinessAnalyzer(businesses)
analyzer.analyze_all(check_websites=True)
summary = analyzer.get_summary()

wa = summary["website_analysis"]
leads = summary["leads"]

console.print(f"\n{'=' * 60}")
console.print(f"  [bold]TOTAL:[/bold] {summary['total_businesses']} businesses")
console.print(
    f"  [bold]Avg rating:[/bold] {summary['avg_rating']} | Reviews: {summary['total_reviews_sum']:,}"
)
console.print(f"{'=' * 60}")
console.print(f"\n  [bold yellow]Website:[/bold yellow]")
console.print(f"    No website: {wa['no_website']} ({wa['pct_no_website']}%)")
console.print(f"    Social media only: {wa['social_media_only']}")
console.print(f"    Free builder: {wa['free_builder_site']}")
console.print(f"    Unreachable: {wa['unreachable_or_broken']}")
console.print(f"    Working website: {wa['has_working_website']}")
console.print(f"\n  [bold green]Leads:[/bold green]")
console.print(f"    HIGH: {leads['high_priority']}")
console.print(f"    MEDIUM: {leads['medium_priority']}")
console.print(f"    Total leads: {leads['total_potential_leads']}")

with_phone = sum(
    1 for b in businesses if b.phone and str(b.phone).strip() not in ("nan", "", "None")
)
high_phone = sum(
    1
    for b in businesses
    if b.lead_priority == "HIGH"
    and b.phone
    and str(b.phone).strip() not in ("nan", "", "None")
)
console.print(f"\n  With phone: {with_phone} | HIGH+phone: {high_phone}")

if summary.get("by_neighborhood"):
    console.print(f"\n  [bold]Top Areas:[/bold]")
    for n, c in sorted(summary["by_neighborhood"].items(), key=lambda x: -x[1])[:25]:
        console.print(f"    {n}: {c}", highlight=False)

# Extract city from address or neighborhood
city_counts = {}
for b in businesses:
    city = b.city or b.neighborhood or "Unknown"
    city_counts[city] = city_counts.get(city, 0) + 1

console.print(f"\n  [bold]By City:[/bold]")
for c, n in sorted(city_counts.items(), key=lambda x: -x[1])[:25]:
    console.print(f"    {c}: {n}", highlight=False)

# Top leads table
table = Table(title="Top 50 Leads Nationwide", show_lines=True)
table.add_column("#", justify="right", width=3)
table.add_column("Name", style="bold", max_width=30)
table.add_column("City/Area", max_width=18)
table.add_column("Rat", justify="center", width=4)
table.add_column("Rev", justify="right", width=5)
table.add_column("Website", max_width=14)
table.add_column("Score", justify="center", style="bold green", width=5)
table.add_column("Phone", max_width=16)

high_leads = sorted(
    [b for b in businesses if b.lead_priority == "HIGH"],
    key=lambda b: (-b.lead_score, -b.total_reviews),
)
for i, b in enumerate(high_leads[:50], 1):
    ws = "NO WEBSITE" if b.website_status == "no_website" else b.website_status[:14]
    area = b.city or b.neighborhood or "N/A"
    table.add_row(
        str(i),
        b.name[:30].replace("[", "(").replace("]", ")"),
        area[:18].replace("[", "(").replace("]", ")"),
        f"{b.rating:.1f}" if b.rating else "-",
        str(b.total_reviews),
        ws,
        str(b.lead_score),
        (b.phone or "-")[:16],
    )
console.print(table)

console.print(f"\n[bold]Exporting full report...")
exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="paraguay_beauty")
console.print(f"\n[bold green]Exported:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")
