#!/usr/bin/env python3
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter
from src.models import Business

console = Console()

cp = "data/py_beauty_checkpoint.json"
all_businesses = {}

if Path(cp).exists():
    with open(cp) as f:
        data = json.load(f)
    raw = data.get("businesses", {})
    for pid, r in raw.items():
        b = Business(
            place_id=r.get("place_id", ""),
            name=r.get("name", ""),
            address=r.get("address", ""),
            lat=r.get("lat", 0) or 0,
            lng=r.get("lng", 0) or 0,
            phone=r.get("phone", ""),
            website=r.get("website", ""),
            types=r.get("types", []),
            primary_type=r.get("primary_type", ""),
            rating=r.get("rating", 0) or 0,
            total_reviews=r.get("total_reviews", 0) or 0,
            has_website=bool(r.get("has_website", r.get("website"))),
            website_status="active" if r.get("website") else "no_website",
            scraped_at=r.get("scraped_at", ""),
        )
        b.city = r.get("city", "")
        b.neighborhood = r.get("neighborhood", "")
        b.vertical = r.get("vertical", "Beauty & Wellness")
        b.status = r.get("status", "")
        all_businesses[pid] = b

businesses = list(all_businesses.values())
console.print(f"\n[cyan]Loaded {len(businesses)} businesses[/cyan]")

# Quick analysis - NO website checks (too slow)
no_web = sum(1 for b in businesses if not b.has_website)
social = sum(
    1
    for b in businesses
    if b.website
    and any(x in b.website.lower() for x in ["facebook", "instagram", "wa.me"])
)
with_phone = sum(1 for b in businesses if b.phone)

# Lead score without website checks
for b in businesses:
    score = 0
    if not b.has_website:
        score += 40
    elif (
        "facebook" in (b.website or "").lower()
        or "instagram" in (b.website or "").lower()
    ):
        score += 35

    if b.total_reviews >= 50:
        score += 20
    elif b.total_reviews >= 20:
        score += 15
    elif b.total_reviews >= 5:
        score += 10

    if b.rating >= 4.0:
        score += 15
    elif b.rating >= 3.5:
        score += 10

    b.lead_score = min(score, 100)
    b.lead_priority = "HIGH" if score >= 60 else "MEDIUM" if score >= 35 else "LOW"

high_leads = [b for b in businesses if b.lead_priority == "HIGH"]
high_with_phone = sum(1 for b in high_leads if b.phone)

console.print(f"\n{'=' * 60}")
console.print(f"[bold]TOTAL: {len(businesses)} businesses[/bold]")
console.print(f"  No website: {no_web} ({no_web / len(businesses) * 100:.0f}%)")
console.print(f"  Social media: {social}")
console.print(f"  With phone: {with_phone}")
console.print(f"  HIGH leads: {len(high_leads)} (with phone: {high_with_phone})")
console.print(f"{'=' * 60}")

# City breakdown
city_counts = {}
for b in businesses:
    city = b.city or b.neighborhood or "Unknown"
    city_counts[city] = city_counts.get(city, 0) + 1

console.print(f"\n[bold]Top Cities:[/bold]")
for c, n in sorted(city_counts.items(), key=lambda x: -x[1])[:25]:
    console.print(f"  {c}: {n}", highlight=False)

# Top leads table
table = Table(title="Top 50 Leads Nationwide", show_lines=True)
table.add_column("#", justify="right", width=3)
table.add_column("Name", style="bold", max_width=30)
table.add_column("City", max_width=18)
table.add_column("Rat", justify="center", width=4)
table.add_column("Rev", justify="right", width=5)
table.add_column("Website", max_width=14)
table.add_column("Score", justify="center", style="bold green", width=5)
table.add_column("Phone", max_width=16)

high_leads_sorted = sorted(high_leads, key=lambda b: (-b.lead_score, -b.total_reviews))
for i, b in enumerate(high_leads_sorted[:50], 1):
    ws = (
        "NO WEB"
        if not b.has_website
        else "SOCIAL"
        if b.website and any(x in b.website.lower() for x in ["facebook", "instagram"])
        else "WEB"
    )
    area = b.city or b.neighborhood or "N/A"
    table.add_row(
        str(i),
        b.name[:30].replace("[", "(").replace("]", ")"),
        area[:18],
        f"{b.rating:.1f}" if b.rating else "-",
        str(b.total_reviews),
        ws,
        str(b.lead_score),
        (b.phone or "-")[:16],
    )
console.print(table)

# Export
summary = {
    "total_businesses": len(businesses),
    "website_analysis": {
        "no_website": no_web,
        "social_media_only": social,
        "has_working_website": len(businesses) - no_web - social,
        "pct_no_website": round(no_web / len(businesses) * 100, 1),
    },
    "leads": {
        "high_priority": len(high_leads),
        "medium_priority": sum(1 for b in businesses if b.lead_priority == "MEDIUM"),
        "total_potential_leads": len(high_leads)
        + sum(1 for b in businesses if b.lead_priority == "MEDIUM"),
    },
    "by_neighborhood": city_counts,
    "avg_rating": sum(b.rating for b in businesses if b.rating)
    / max(1, sum(1 for b in businesses if b.rating)),
    "total_reviews_sum": sum(b.total_reviews for b in businesses),
}

exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="paraguay_beauty_nationwide")
console.print(f"\n[bold green]Exported:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")
