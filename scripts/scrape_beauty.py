#!/usr/bin/env python3
import time
import logging
import json
from datetime import datetime
from collections import Counter

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.table import Table
from rich.panel import Panel

from src.config import GOOGLE_MAPS_API_KEY, ASUNCION_CENTER, GREATER_ASUNCION_BOUNDS
from src.api_client import PlacesClient
from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter

console = Console()
logging.basicConfig(level=logging.WARNING)

BEAUTY_KEYWORDS = [
    "salon de belleza",
    "peluqueria",
    "barberia",
    "spa",
    "nails",
    "centro de estetica",
    "estetica facial",
    "manicura",
    "pedicura",
    "barber shop",
    "hair salon",
    "tatuajes",
    "depilacion",
    "masajes",
]

BEAUTY_TYPES = [
    "beauty_salon",
    "hair_care",
    "spa",
]

NEIGHBORHOODS = {
    "Asunción Centro": (-25.2637, -57.5759),
    "Carmelitas": (-25.2550, -57.5700),
    "Villa Morra": (-25.2480, -57.5650),
    "Mburicá": (-25.2500, -57.5550),
    "Recoleta": (-25.2670, -57.5630),
    "San Jorge": (-25.2530, -57.5900),
    "Sajonia": (-25.2700, -57.5850),
    "Chacarita": (-25.2680, -57.6100),
    "Pettirossi": (-25.2750, -57.6050),
    "Mcal. López": (-25.2550, -57.5800),
    "Luque": (-25.2500, -57.5000),
    "San Lorenzo": (-25.3400, -57.5200),
    "Fernando de la Mora": (-25.3300, -57.5200),
    "Lambaré": (-25.3400, -57.6300),
    "Capiatá": (-25.3500, -57.4400),
    "Mariano Roque Alonso": (-25.2100, -57.5500),
    "Limpio": (-25.1700, -57.4800),
    "Ñemby": (-25.3900, -57.5400),
    "Guaraní": (-25.3200, -57.5800),
    "Villa Elisa": (-25.3700, -57.5600),
}

console.print(
    Panel.fit(
        "[bold cyan]Beauty & Wellness Business Extractor - Asunción[/bold cyan]\n"
        "[dim]Targeted search for salons, barbers, spas, nails across Greater Asunción[/dim]",
        border_style="cyan",
    )
)

client = PlacesClient(GOOGLE_MAPS_API_KEY)
all_businesses = {}

console.print(f"\n[bold]Step 1:[/bold] Searching by keyword across Asunción...")
console.print(
    f"[dim]Keywords: {len(BEAUTY_KEYWORDS)} | Locations: {len(NEIGHBORHOODS)}[/dim]\n"
)

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeElapsedColumn(),
    console=console,
) as progress:
    task = progress.add_task("Searching...", total=len(BEAUTY_KEYWORDS))

    for keyword in BEAUTY_KEYWORDS:
        progress.console.print(f"  [cyan]Searching:[/cyan] '{keyword}'")

        results = client.text_search(
            query=f"{keyword} en Asunción Paraguay",
            location=ASUNCION_CENTER,
            radius=50000,
        )

        found_in_search = 0
        new_in_search = 0
        for place in results:
            pid = place.get("place_id", "")
            found_in_search += 1
            if pid not in all_businesses:
                new_in_search += 1
                details = client.get_place_details(pid)
                if details:
                    business = client.parse_place(details, include_reviews=True)
                    business.scraped_at = datetime.now().isoformat()
                    all_businesses[pid] = business

        progress.console.print(
            f"    Found: {found_in_search} results, {new_in_search} new unique → Total: [green]{len(all_businesses)}[/green]"
        )
        progress.advance(task)

console.print(f"\n[bold]Step 2:[/bold] Also searching by place type...")

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TimeElapsedColumn(),
    console=console,
) as progress:
    task2 = progress.add_task("Type search...", total=len(BEAUTY_TYPES) * 4)

    for ptype in BEAUTY_TYPES:
        progress.console.print(f"  [cyan]Type:[/cyan] {ptype}")
        for area_name, (lat, lng) in list(NEIGHBORHOODS.items())[:4]:
            results = client.text_search(
                query=f"{ptype}",
                location=(lat, lng),
                radius=10000,
            )
            for place in results:
                pid = place.get("place_id", "")
                if pid not in all_businesses:
                    details = client.get_place_details(pid)
                    if details:
                        business = client.parse_place(details, include_reviews=True)
                        business.scraped_at = datetime.now().isoformat()
                        all_businesses[pid] = business

            progress.advance(task2)

        progress.console.print(
            f"    Total unique so far: [green]{len(all_businesses)}[/green]"
        )

businesses = list(all_businesses.values())
console.print(f"\nTotal unique beauty businesses found: {len(businesses)}")
console.print(f"API requests used: {client.requests_count}")

console.print(f"\n[bold]Step 3:[/bold] Analyzing businesses & websites...")
analyzer = BusinessAnalyzer(businesses)
analyzer.analyze_all(check_websites=True)

summary = analyzer.get_summary()

console.print(f"\n")
console.print(
    Panel("[bold]Beauty & Wellness - Asunción Summary[/bold]", border_style="green")
)
console.print(f"  [bold]Total businesses:[/bold] {summary['total_businesses']}")
console.print(f"  [bold]Average rating:[/bold] {summary['avg_rating']}")
console.print(f"  [bold]Total reviews:[/bold] {summary['total_reviews_sum']:,}")

wa = summary["website_analysis"]
console.print(f"\n  [bold yellow]Website Analysis:[/bold yellow]")
console.print(f"    No website: {wa['no_website']} ({wa['pct_no_website']}%)")
console.print(f"    Social media only: {wa['social_media_only']}")
console.print(f"    Free builder (Wix, etc): {wa['free_builder_site']}")
console.print(f"    Unreachable/broken: {wa['unreachable_or_broken']}")
console.print(f"    Has working website: {wa['has_working_website']}")

leads = summary["leads"]
console.print(f"\n  [bold green]Lead Generation:[/bold green]")
console.print(f"    HIGH priority leads: {leads['high_priority']}")
console.print(f"    MEDIUM priority leads: {leads['medium_priority']}")
console.print(f"    Total potential leads: {leads['total_potential_leads']}")

if summary.get("by_neighborhood"):
    console.print(f"\n  [bold]By Neighborhood:[/bold]")
    for neigh, count in list(summary["by_neighborhood"].items())[:15]:
        console.print(f"    {neigh}: {count}", highlight=False)

table = Table(title="Top Beauty Leads (No Website / Outdated)", show_lines=True)
table.add_column("Name", style="bold", max_width=35)
table.add_column("Type", style="cyan", max_width=22)
table.add_column("Neighborhood", max_width=18)
table.add_column("Rating", justify="center")
table.add_column("Reviews", justify="right")
table.add_column("Website Status", style="red", max_width=18)
table.add_column("Score", justify="center", style="bold green")
table.add_column("Phone", max_width=18)

high_leads = analyzer.get_high_priority_leads()
for b in high_leads[:30]:
    ws = b.website_status
    if ws == "no_website":
        ws_style = "[red]NO WEBSITE[/red]"
    elif ws == "social_media_only":
        ws_style = "[yellow]Social Only[/yellow]"
    elif ws in ("unreachable", "ssl_error", "timeout"):
        ws_style = f"[red]{ws}[/red]"
    elif ws == "free_builder":
        ws_style = "[yellow]Free Builder[/yellow]"
    else:
        ws_style = ws

    table.add_row(
        b.name[:35].replace("[", "(").replace("]", ")"),
        ", ".join(b.types[:2])[:22].replace("[", "(").replace("]", ")"),
        b.neighborhood[:18].replace("[", "(").replace("]", ")"),
        f"{b.rating:.1f}" if b.rating else "-",
        str(b.total_reviews),
        ws_style,
        str(b.lead_score),
        b.phone[:18] if b.phone else "-",
    )

console.print(table)

console.print(f"\n[bold]Step 4:[/bold] Exporting data...")
exporter = Exporter(output_dir="data")
files = exporter.export_all(businesses, summary, tag="beauty")
console.print(f"\n[bold green]Exported files:[/bold green]")
for label, path in files.items():
    console.print(f"  {label}: {path}")

console.print(f"\n[bold]Done! API requests used: {client.requests_count}[/bold]")
