#!/usr/bin/env python3
"""
Paraguay-wide Beauty & Wellness scraper.
Covers all major cities. Auto-saves checkpoint every batch.
Run multiple times - it resumes from where it stopped.
"""

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from time import sleep

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.panel import Panel

from src.config import GOOGLE_MAPS_API_KEY
from src.api_client import PlacesClient
from src.models import Business

console = Console()
logging.basicConfig(level=logging.WARNING)

CHECKPOINT = "data/py_beauty_checkpoint.json"

CITIES = {
    "Asuncion": (-25.2637, -57.5759),
    "San Lorenzo": (-25.3395, -57.5088),
    "Luque": (-25.2492, -57.4925),
    "Capiata": (-25.3620, -57.4438),
    "Lambare": (-25.3438, -57.6310),
    "Fernando de la Mora": (-25.3265, -57.5260),
    "Nemby": (-25.3948, -57.5485),
    "Limpio": (-25.1663, -57.4846),
    "Mariano Roque Alonso": (-25.2111, -57.5553),
    "Villa Elisa": (-25.3708, -57.5607),
    "Itaugua": (-25.3895, -57.3377),
    "Ypane": (-25.4142, -57.5604),
    "Guaruani": (-25.3195, -57.5780),
    "Ciudad del Este": (-25.5097, -54.6108),
    "Hernandarias": (-25.3847, -54.6308),
    "Minga Guazu": (-25.4210, -54.6805),
    "Presidente Franco": (-25.5622, -54.5908),
    "Encarnacion": (-27.3306, -55.8667),
    "Coronel Oviedo": (-25.4408, -56.4558),
    "Pedro Juan Caballero": (-22.5438, -55.7319),
    "Villarrica": (-25.7536, -56.4361),
    "Caaguazu": (-25.4594, -56.0197),
    "Concepcion": (-23.3986, -57.4269),
    "Pilar": (-26.8667, -58.3167),
    "Caacupe": (-25.3864, -57.1419),
    "San Ignacio Guazu": (-26.8681, -57.0019),
    "Paraguari": (-25.6306, -57.1486),
    "San Estanislao": (-24.6669, -56.4475),
    "Villa Hayes": (-25.0939, -57.5983),
    "Aregua": (-25.2964, -57.3758),
    "Atyra": (-25.3050, -57.1936),
    "Altos": (-25.2625, -57.2056),
    "San Bernardino": (-25.2822, -57.3175),
    "Ita": (-25.3486, -57.4189),
    "Yaguaron": (-25.4706, -57.2922),
    "Piribebuy": (-25.4878, -56.9917),
    "Santa Rita": (-25.6883, -54.9211),
    "J. E. Estigarribia": (-25.5267, -55.7950),
    "Coronel Bogado": (-26.4058, -56.9883),
    "Obligado": (-26.8131, -55.7264),
    "Hohenau": (-26.9314, -55.6381),
    "Bella Vista": (-25.4869, -54.7792),
    "Naranjal": (-25.6081, -54.7864),
    "Wanda": (-25.6025, -54.5431),
    "Puerto Iguazu area": (-25.5956, -54.5850),
    "Ayolas": (-27.3861, -56.8919),
    "San Cosme y Damian": (-27.2931, -56.7761),
    "San Pedro de Ycuamandiyu": (-24.1269, -57.0911),
    "Villa del Rosario": (-24.0550, -57.1883),
}

KEYWORDS_PER_CITY = [
    "salon de belleza",
    "peluqueria",
    "barberia",
    "spa",
    "nails",
    "estetica",
    "uñas",
    "tatuajes",
    "masajes",
    "depilacion",
    "gimnasio",
    "barber shop",
    "centro de estetica",
    "hair salon",
    "beauty salon",
    "maquillaje",
]

KEYWORDS_EXTRA = [
    "microblading",
    "keratina",
    "alisado",
    "balayage",
    "mechas",
    "extensiones cabello",
    "lifting pestañas",
    "criolipolisis",
    "cavitacion",
    "tratamiento facial",
    "tratamiento corporal",
    "botox",
    "acido hialuronico",
    "piercing",
    "gym",
    "yoga",
    "crossfit",
    "pilates",
]


def load_checkpoint():
    if Path(CHECKPOINT).exists():
        with open(CHECKPOINT) as f:
            data = json.load(f)
        ids = set(data.get("ids", []))
        raw = data.get("businesses", {})
        done = set(data.get("done_queries", []))
        return ids, raw, done
    return set(), {}, set()


def save_checkpoint(ids, raw, done):
    Path("data").mkdir(exist_ok=True)
    tmp = CHECKPOINT + ".tmp"
    with open(tmp, "w") as f:
        json.dump({"ids": list(ids), "businesses": raw, "done_queries": list(done)}, f)
    Path(tmp).rename(CHECKPOINT)


def raw_to_biz(r):
    b = Business(
        place_id=r["place_id"],
        name=r.get("name", ""),
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
        "status",
        "icon",
        "editorial_summary",
        "vertical",
        "website_is_social_only",
        "website_is_free_builder",
        "website_uses_https",
        "website_redirects_to_social",
    ]:
        setattr(b, k, r.get(k, "") or "")
    b.saturday_hours = r.get("saturday_hours", "")
    b.sunday_hours = r.get("sunday_hours", "")
    b.is_open_now = r.get("is_open_now")
    b.price_level = r.get("price_level")
    b.photo_count = r.get("photo_count", 0)
    b.reviews = []
    return b


def biz_to_raw(b):
    d = {}
    for attr in [
        "place_id",
        "name",
        "status",
        "address",
        "street_number",
        "street_name",
        "neighborhood",
        "city",
        "state",
        "postal_code",
        "country",
        "lat",
        "lng",
        "phone",
        "international_phone",
        "website",
        "google_maps_url",
        "types",
        "primary_type",
        "rating",
        "total_reviews",
        "price_level",
        "is_open_now",
        "saturday_hours",
        "sunday_hours",
        "photo_count",
        "editorial_summary",
        "has_website",
        "website_status",
        "website_is_social_only",
        "website_is_free_builder",
        "website_uses_https",
        "website_redirects_to_social",
        "lead_score",
        "lead_priority",
        "scraped_at",
        "vertical",
    ]:
        d[attr] = getattr(b, attr, "")
    return d


def main():
    console.print(
        Panel.fit(
            "[bold cyan]Paraguay Nationwide Beauty Scraper[/bold cyan]\n"
            "[dim]46 cities · 17 keywords per city · auto-resume[/dim]",
            border_style="cyan",
        )
    )

    client = PlacesClient(GOOGLE_MAPS_API_KEY)
    existing_ids, raw_businesses, done_queries = load_checkpoint()
    all_businesses = {pid: raw_to_biz(r) for pid, r in raw_businesses.items()}

    console.print(
        f"Resumed: [green]{len(all_businesses)}[/green] businesses, {len(done_queries)} queries done"
    )

    # Build all queries
    queries = []
    for city, (lat, lng) in CITIES.items():
        for kw in KEYWORDS_PER_CITY:
            qkey = f"{kw}|{city}"
            queries.append((qkey, f"{kw} {city} Paraguay", (lat, lng), 30000))
        for kw in KEYWORDS_EXTRA:
            qkey = f"{kw}|{city}"
            queries.append((qkey, f"{kw} {city} Paraguay", (lat, lng), 20000))

    # Filter out done
    remaining = [(qk, q, loc, r) for qk, q, loc, r in queries if qk not in done_queries]
    console.print(
        f"Remaining queries: [yellow]{len(remaining)}[/yellow] / {len(queries)}"
    )
    console.print(
        f"Target: [bold]1000+ new businesses[/bold] (currently have {len(all_businesses)})"
    )

    if len(remaining) == 0:
        console.print("[green]All queries done![/green]")
        return all_businesses

    BATCH = 25
    new_total = 0
    batches = [remaining[i : i + BATCH] for i in range(0, len(remaining), BATCH)]

    console.print(f"\n[bold]Running in {len(batches)} batches of {BATCH}...[/bold]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        TextColumn("({task.completed}/{task.total})"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Scraping Paraguay...", total=len(remaining))

        for batch_idx, batch in enumerate(batches):
            batch_new = 0
            for qkey, query, (lat, lng), radius in batch:
                if qkey in done_queries:
                    progress.advance(task)
                    continue

                try:
                    results = client.text_search(
                        query=query, location=(lat, lng), radius=radius
                    )
                except Exception as e:
                    console.print(f"  [red]Error: {e}[/red]")
                    sleep(5)
                    continue

                for place in results:
                    pid = place.get("place_id", "")
                    if pid in existing_ids:
                        continue

                    details = client.get_place_details(pid)
                    if details:
                        b = client.parse_place(details, include_reviews=False)
                        b.scraped_at = datetime.now().isoformat()
                        all_businesses[pid] = b
                        existing_ids.add(pid)
                        raw_businesses[pid] = biz_to_raw(b)
                        batch_new += 1
                        new_total += 1

                done_queries.add(qkey)
                progress.advance(task)

            # Save checkpoint after each batch
            save_checkpoint(existing_ids, raw_businesses, done_queries)
            progress.console.print(
                f"  Batch {batch_idx + 1}/{len(batches)}: +{batch_new} new | "
                f"total: {len(all_businesses)} | API: {client.requests_count}",
                highlight=False,
            )

            if len(all_businesses) >= len(raw_businesses) + 0 and new_total >= 1000:
                # Keep going until we have enough
                pass

    console.print(f"\n{'=' * 60}")
    console.print(
        f"[bold green]DONE! {len(all_businesses)} businesses ({new_total} new)[/bold green]"
    )
    console.print(f"API requests: {client.requests_count}")
    console.print(f"{'=' * 60}")

    return all_businesses


if __name__ == "__main__":
    all_businesses = main()

    if not all_businesses:
        console.print("[yellow]No data to export[/yellow]")
        sys.exit(0)

    # Quick summary
    businesses = list(all_businesses.values())
    no_web = sum(1 for b in businesses if not b.has_website)
    social = sum(1 for b in businesses if getattr(b, "website_is_social_only", False))
    high = sum(1 for b in businesses if b.lead_priority == "HIGH")
    with_phone = sum(1 for b in businesses if b.phone)

    console.print(f"\n  Total: {len(businesses)}")
    console.print(
        f"  No website: {no_web} ({no_web / len(businesses) * 100:.0f}%)",
        highlight=False,
    )
    console.print(f"  Social only: {social}")
    console.print(f"  HIGH leads: {high}")
    console.print(f"  With phone: {with_phone}")
    console.print(
        f"\n  [dim]Run merge_nationwide.py to analyze and export full report[/dim]"
    )
