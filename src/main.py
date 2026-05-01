#!/usr/bin/env python3
import argparse
import logging
import sys

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from src.config import (
    GOOGLE_MAPS_API_KEY,
    ASUNCION_BOUNDS,
    SEARCH_RADIUS,
    GOOGLE_PLACE_TYPES,
    VERTICAL_MAPPING,
    NEIGHBORHOODS_ASUNCION,
)
from src.api_client import PlacesClient
from src.scraper import GridScraper
from src.analyzer import BusinessAnalyzer
from src.exporter import Exporter

console = Console()


def print_banner():
    console.print(
        Panel.fit(
            "[bold cyan]Google Maps Business Extractor - Asunción[/bold cyan]\n"
            "[dim]Extract, analyze & find leads from Google Maps businesses[/dim]",
            border_style="cyan",
        )
    )


def print_summary(summary: dict):
    console.print("\n")
    console.print(Panel("[bold]Extraction Summary[/bold]", border_style="green"))

    console.print(
        f"  [bold]Total businesses found:[/bold] {summary['total_businesses']}"
    )
    console.print(f"  [bold]Average rating:[/bold] {summary['avg_rating']}")
    console.print(f"  [bold]Total reviews:[/bold] {summary['total_reviews_sum']:,}")

    wa = summary["website_analysis"]
    console.print(f"\n  [bold yellow]Website Analysis:[/bold yellow]")
    console.print(f"    No website: {wa['no_website']} ({wa['pct_no_website']}%)")
    console.print(f"    Social media only: {wa['social_media_only']}")
    console.print(f"    Free builder (Wix, etc): {wa['free_builder_site']}")
    console.print(f"    Unreachable/broken: {wa['unreachable_or_broken']}")
    console.print(f"    Redirects to social: {wa['redirects_to_social']}")

    leads = summary["leads"]
    console.print(f"\n  [bold green]Lead Generation:[/bold green]")
    console.print(f"    HIGH priority leads: {leads['high_priority']}")
    console.print(f"    MEDIUM priority leads: {leads['medium_priority']}")
    console.print(f"    Total potential leads: {leads['total_potential_leads']}")

    if summary.get("by_vertical"):
        console.print(f"\n  [bold]By Vertical:[/bold]")
        for vert, count in list(summary["by_vertical"].items())[:15]:
            console.print(f"    {vert}: {count}")

    if summary.get("by_neighborhood"):
        console.print(f"\n  [bold]Top Neighborhoods:[/bold]")
        for neigh, count in list(summary["by_neighborhood"].items())[:10]:
            console.print(f"    {neigh}: {count}")


def print_lead_table(businesses, limit=20):
    table = Table(title="Top Leads (No Website / Outdated)", show_lines=True)
    table.add_column("Name", style="bold", max_width=30)
    table.add_column("Vertical", style="cyan", max_width=18)
    table.add_column("Neighborhood", max_width=15)
    table.add_column("Rating", justify="center")
    table.add_column("Reviews", justify="right")
    table.add_column("Website Status", style="red", max_width=18)
    table.add_column("Score", justify="center", style="bold green")
    table.add_column("Phone", max_width=18)

    for b in businesses[:limit]:
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
            b.name[:30],
            b.vertical,
            b.neighborhood,
            f"{b.rating:.1f}" if b.rating else "-",
            str(b.total_reviews),
            ws_style,
            str(b.lead_score),
            b.phone or "-",
        )

    console.print(table)


def cmd_full_scrape(args):
    console.print("[bold]Mode:[/bold] Full grid scrape of Asunción")
    client = PlacesClient(GOOGLE_MAPS_API_KEY)
    scraper = GridScraper(client, greater_area=args.greater_area)

    place_types = None
    if args.types:
        place_types = [t.strip() for t in args.types.split(",")]
        console.print(f"[bold]Filtering types:[/bold] {place_types}")

    businesses = scraper.scrape_all(
        place_types=place_types,
        include_reviews=not args.no_reviews,
        max_pages=args.max_pages,
    )

    analyzer = BusinessAnalyzer(businesses)
    analyzer.analyze_all(check_websites=not args.skip_website_check)

    summary = analyzer.get_summary()
    print_summary(summary)

    if args.show_leads:
        print_lead_table(analyzer.get_high_priority_leads())

    exporter = Exporter(output_dir=args.output)
    files = exporter.export_all(businesses, summary, tag="full")
    console.print("\n[bold green]Exported files:[/bold green]")
    for label, path in files.items():
        console.print(f"  {label}: {path}")


def cmd_neighborhood(args):
    console.print(f"[bold]Mode:[/bold] Neighborhood scrape")
    client = PlacesClient(GOOGLE_MAPS_API_KEY)
    scraper = GridScraper(client)

    if args.neighborhood not in NEIGHBORHOODS_ASUNCION:
        console.print(f"[red]Unknown neighborhood. Available:[/red]")
        for name, coords in NEIGHBORHOODS_ASUNCION.items():
            console.print(f"  {name}: {coords}")
        return

    center = NEIGHBORHOODS_ASUNCION[args.neighborhood]
    businesses = scraper.scrape_neighborhood(
        neighborhood_name=args.neighborhood,
        center=center,
        radius=args.radius,
        include_reviews=not args.no_reviews,
    )

    analyzer = BusinessAnalyzer(businesses)
    analyzer.analyze_all(check_websites=not args.skip_website_check)

    summary = analyzer.get_summary()
    print_summary(summary)

    if args.show_leads:
        print_lead_table(analyzer.get_high_priority_leads())

    exporter = Exporter(output_dir=args.output)
    tag = args.neighborhood.lower().replace(" ", "_")
    files = exporter.export_all(businesses, summary, tag=tag)
    console.print("\n[bold green]Exported files:[/bold green]")
    for label, path in files.items():
        console.print(f"  {label}: {path}")


def cmd_analyze_existing(args):
    import pandas as pd
    from pathlib import Path

    csv_path = Path(args.csv_file)
    if not csv_path.exists():
        console.print(f"[red]File not found: {csv_path}[/red]")
        return

    df = pd.read_csv(csv_path)
    console.print(f"Loaded {len(df)} businesses from {csv_path}")

    businesses = []
    for _, row in df.iterrows():
        b = Business(
            place_id=row.get("place_id", ""),
            name=row.get("name", ""),
            status=row.get("status", ""),
            address=row.get("address", ""),
            lat=row.get("lat", 0.0),
            lng=row.get("lng", 0.0),
            phone=row.get("phone", ""),
            website=row.get("website", ""),
            types=str(row.get("types", "")).split("|"),
            primary_type=row.get("primary_type", ""),
            rating=row.get("rating", 0.0),
            total_reviews=int(row.get("total_reviews", 0)),
            has_website=bool(row.get("has_website", False)),
        )
        businesses.append(b)

    analyzer = BusinessAnalyzer(businesses)
    analyzer.analyze_all(check_websites=not args.skip_website_check)

    summary = analyzer.get_summary()
    print_summary(summary)

    if args.show_leads:
        print_lead_table(analyzer.get_high_priority_leads())

    exporter = Exporter(output_dir=args.output)
    files = exporter.export_all(businesses, summary, tag="reanalyzed")
    console.print("\n[bold green]Exported files:[/bold green]")
    for label, path in files.items():
        console.print(f"  {label}: {path}")


def cmd_list_types(args):
    console.print("[bold]Available Google Maps Place Types:[/bold]\n")
    for t in sorted(GOOGLE_PLACE_TYPES):
        console.print(f"  {t}")

    console.print(f"\n[bold]Vertical Mappings:[/bold]\n")
    for vertical, types in VERTICAL_MAPPING.items():
        console.print(f"  [cyan]{vertical}[/cyan]: {', '.join(types)}")


def cmd_list_neighborhoods(args):
    console.print("[bold]Asunción Neighborhoods:[/bold]\n")
    table = Table()
    table.add_column("Neighborhood", style="bold")
    table.add_column("Latitude", justify="right")
    table.add_column("Longitude", justify="right")
    for name, (lat, lng) in NEIGHBORHOODS_ASUNCION.items():
        table.add_row(name, f"{lat:.4f}", f"{lng:.4f}")
    console.print(table)


def main():
    parser = argparse.ArgumentParser(
        description="Google Maps Business Extractor for Asunción"
    )
    parser.add_argument("--output", default="data", help="Output directory")
    parser.add_argument("--no-reviews", action="store_true", help="Skip reviews")
    parser.add_argument(
        "--skip-website-check", action="store_true", help="Skip website checks"
    )
    parser.add_argument("--show-leads", action="store_true", help="Show lead table")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    subparsers = parser.add_subparsers(dest="command")

    scrape_parser = subparsers.add_parser("scrape", help="Full grid scrape of Asunción")
    scrape_parser.add_argument(
        "--greater-area",
        action="store_true",
        help="Include Greater Asunción (Luque, San Lorenzo, etc.)",
    )
    scrape_parser.add_argument(
        "--types", type=str, default=None, help="Comma-separated place types to filter"
    )
    scrape_parser.add_argument(
        "--max-pages", type=int, default=3, help="Max pages per grid point (default 3)"
    )

    neigh_parser = subparsers.add_parser(
        "neighborhood", help="Scrape a specific neighborhood"
    )
    neigh_parser.add_argument("neighborhood", help="Neighborhood name")
    neigh_parser.add_argument(
        "--radius", type=int, default=1500, help="Radius in meters"
    )

    analyze_parser = subparsers.add_parser("analyze", help="Analyze existing CSV data")
    analyze_parser.add_argument("csv_file", help="Path to CSV file")

    subparsers.add_parser("list-types", help="List available place types and verticals")
    subparsers.add_parser("list-neighborhoods", help="List available neighborhoods")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    print_banner()

    if not GOOGLE_MAPS_API_KEY and args.command not in (
        "list-types",
        "list-neighborhoods",
        "analyze",
    ):
        console.print("[bold red]Error: GOOGLE_MAPS_API_KEY not set in .env[/bold red]")
        console.print("Copy .env.example to .env and add your API key.")
        sys.exit(1)

    if args.command == "scrape":
        cmd_full_scrape(args)
    elif args.command == "neighborhood":
        cmd_neighborhood(args)
    elif args.command == "analyze":
        cmd_analyze_existing(args)
    elif args.command == "list-types":
        cmd_list_types(args)
    elif args.command == "list-neighborhoods":
        cmd_list_neighborhoods(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
