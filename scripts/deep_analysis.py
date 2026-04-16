#!/usr/bin/env python3
"""
Deep Analysis of Paraguay Beauty & Wellness Data
Categorize, score, and prioritize leads for Vete outreach
"""

import json
from pathlib import Path
from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns

console = Console()

# Load data
cp = "data/py_beauty_checkpoint.json"
all_businesses = {}

with open(cp) as f:
    data = json.load(f)
raw = data.get("businesses", {})

for pid, r in raw.items():
    from src.models import Business

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
        has_website=bool(r.get("website")),
        scraped_at=r.get("scraped_at", ""),
    )
    b.city = r.get("city", "")
    b.neighborhood = r.get("neighborhood", "")
    b.status = r.get("status", "")
    all_businesses[pid] = b

businesses = list(all_businesses.values())
total = len(businesses)

console.print(
    Panel.fit(
        f"[bold cyan]DEEP ANALYSIS: Paraguay Beauty & Wellness[/bold cyan]\n"
        f"[dim]{total:,} businesses across {len(set(b.city for b in businesses if b.city))} cities[/dim]",
        border_style="cyan",
    )
)

# ====== CATEGORIZATION ======
categories = {
    "Salon de Belleza": [
        "salon de belleza",
        "beauty salon",
        "salon",
        "centro de belleza",
    ],
    "Peluqueria": [
        "peluqueria",
        "hair salon",
        "hair",
        "pelu",
        "color",
        "tinte",
        "mecha",
        "balayage",
        "alisado",
        "keratina",
    ],
    "Barberia": ["barber", "barberia", "barbershop", "barber shop"],
    "Spa/Wellness": [
        "spa",
        "wellness",
        "masaje",
        "massage",
        "sauna",
        "hidro",
        "criolipolisis",
        "cavitacion",
    ],
    "Uñas/Nails": [
        "uñas",
        "nails",
        "nail",
        "manicura",
        "pedicura",
        "esculpidas",
        "gel",
        "acrilicas",
    ],
    "Estetica/Facial": [
        "estetica",
        "facial",
        "cosmet",
        "tratamiento facial",
        "limpieza",
        "botox",
        "acido",
    ],
    "Tatuajes/Piercing": ["tattoo", "tatu", "piercing", "body art"],
    "Gimnasio/Fitness": [
        "gym",
        "gimnasio",
        "fitness",
        "crossfit",
        "yoga",
        "pilates",
        "entrenador",
        "sport",
        "academia",
    ],
    "Depilacion": ["depilacion", "depilacion laser", "laser"],
    "Maquillaje": ["makeup", "maquillaje", "make up", "novia", "social"],
    "Pestañas/Cejas": ["pestañas", "cejas", "lifting", "microblading", "permanente"],
    "Otros": [],
}


def categorize_business(b):
    name_lower = b.name.lower() if b.name else ""
    addr_lower = b.address.lower() if b.address else ""
    text = name_lower + " " + addr_lower

    for cat, keywords in categories.items():
        if cat == "Otros":
            continue
        for kw in keywords:
            if kw in text:
                return cat

    # Check types
    for t in b.types:
        t_lower = t.lower()
        if "beauty_salon" in t_lower or "hair_care" in t_lower:
            return "Salon de Belleza" if "beauty" in t_lower else "Peluqueria"
        if "spa" in t_lower:
            return "Spa/Wellness"
        if "gym" in t_lower or "fitness" in t_lower:
            return "Gimnasio/Fitness"

    return "Otros"


for b in businesses:
    b.category = categorize_business(b)

cat_counts = Counter(b.category for b in businesses)

# ====== SUB-CATEGORIES ======
sub_cats = {
    "Spa": ["spa", "spa corporal", "spa facial", "spa agua"],
    "Centro Estetica": ["centro de estetica", "estetica integral", "centro belleza"],
    "Salon Uñas": ["salon de uñas", "uñas", "nails", "manicura", "pedicura"],
    "Peluqueria Unisex": ["peluqueria unisex", "salon unisex"],
    "Barberia Moderna": ["barberia moderna", "barber shop", "barberia contempor"],
    "Tattoo Studio": ["tattoo studio", "estudio tattoo", "tattoo &"],
    "Piercing Studio": ["piercing", "body piercing"],
    "Gimnasio": ["gimnasio", "gym", "fitness center"],
    "CrossFit": ["crossfit", "box"],
    "Yoga/Pilates": ["yoga", "pilates", "estudio yoga"],
    "Depilacion Laser": ["depilacion laser", "laser", "laser estetico"],
    "Clinica Estetica": ["clinica estetica", "clinica beleza", "centro medico"],
    "Perfumeria": ["perfumeria", "cosmeticos", "mega cosmeticos"],
}


def get_subcategory(b):
    name_lower = b.name.lower() if b.name else ""
    for sub, keywords in sub_cats.items():
        for kw in keywords:
            if kw in name_lower:
                return sub
    return "General"


for b in businesses:
    b.subcategory = get_subcategory(b)

sub_counts = Counter(b.subcategory for b in businesses)


# ====== SCORING ======
def compute_deep_score(b):
    score = 0

    # Website score (max 40)
    if not b.has_website:
        score += 40
    elif b.website:
        ws = b.website.lower()
        if "facebook" in ws or "instagram" in ws or "wa.me" in ws:
            score += 30  # social only
        elif any(
            x in ws
            for x in ["wix", "godaddy", "wordpress.com", "weebly", "sites.google"]
        ):
            score += 20  # free builder
        else:
            score += 10  # has real website

    # Popularity score (max 30)
    if b.total_reviews >= 200:
        score += 30
    elif b.total_reviews >= 100:
        score += 25
    elif b.total_reviews >= 50:
        score += 20
    elif b.total_reviews >= 20:
        score += 15
    elif b.total_reviews >= 10:
        score += 10
    elif b.total_reviews >= 5:
        score += 5

    # Rating score (max 15)
    if b.rating >= 4.5:
        score += 15
    elif b.rating >= 4.0:
        score += 12
    elif b.rating >= 3.5:
        score += 8
    elif b.rating >= 3.0:
        score += 5

    # Contactability (max 10)
    if b.phone:
        score += 10

    # Category bonus (max 10) - prioritize certain types
    high_value_cats = ["Spa/Wellness", "Gimnasio/Fitness", "Clinica Estetica"]
    if b.category in high_value_cats:
        score += 10
    elif b.category in ["Salon de Belleza", "Peluqueria"]:
        score += 7
    elif b.category == "Barberia":
        score += 5

    # Size indicator (based on reviews + rating = likely bigger business)
    if b.total_reviews >= 50 and b.rating >= 4.0:
        score += 5

    b.deep_score = min(score, 100)

    if score >= 70:
        b.priority = "A"
    elif score >= 50:
        b.priority = "B"
    elif score >= 30:
        b.priority = "C"
    else:
        b.priority = "D"


for b in businesses:
    compute_deep_score(b)

# Priority breakdown
priority_a = [b for b in businesses if b.priority == "A"]
priority_b = [b for b in businesses if b.priority == "B"]
priority_c = [b for b in businesses if b.priority == "C"]
priority_d = [b for b in businesses if b.priority == "D"]

a_with_phone = sum(1 for b in priority_a if b.phone)
b_with_phone = sum(1 for b in priority_b if b.phone)
c_with_phone = sum(1 for b in priority_c if b.phone)

# ====== OUTPUT ======
console.print(f"\n{'=' * 70}")
console.print(f"[bold cyan]1. BUSINESS CATEGORIES[/bold cyan]")
console.print(f"{'=' * 70}")
for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
    pct = count / total * 100
    bar = "█" * int(pct / 2)
    console.print(f"  {cat:25} | {count:5} ({pct:5.1f}%) {bar}", highlight=False)

console.print(f"\n{'=' * 70}")
console.print(f"[bold cyan]2. PRIORITY SEGMENTS (Deep Score)[/bold cyan]")
console.print(f"{'=' * 70}")
console.print(
    f"  [bold green]PRIORITY A (Score 70-100):[/bold green] {len(priority_a):,} businesses ({len(priority_a) / total * 100:.1f}%)"
)
console.print(f"    → With phone: {a_with_phone:,}")
console.print(
    f"  [bold yellow]PRIORITY B (Score 50-69):[/bold yellow] {len(priority_b):,} ({len(priority_b) / total * 100:.1f}%)"
)
console.print(f"    → With phone: {b_with_phone:,}")
console.print(
    f"  [bold]PRIORITY C (Score 30-49):[/bold] {len(priority_c):,} ({len(priority_c) / total * 100:.1f}%)"
)
console.print(f"    → With phone: {c_with_phone:,}")
console.print(f"  [dim]PRIORITY D (Score <30):[/dim] {len(priority_d):,}")

# Best category by priority
console.print(f"\n[bold]Priority A by Category:[/bold]")
a_by_cat = Counter(b.category for b in priority_a)
for cat, count in a_by_cat.most_common(10):
    console.print(f"  {cat}: {count}", highlight=False)

# City breakdown for Priority A
console.print(f"\n[bold]Top Cities - Priority A:[/bold]")
a_by_city = Counter(b.city for b in priority_a if b.city)
for city, count in a_by_city.most_common(15):
    console.print(f"  {city}: {count}", highlight=False)

# ====== TIER ANALYSIS ======
console.print(f"\n{'=' * 70}")
console.print(
    f"[bold cyan]3. BEST TARGETS FOR VETE (Priority A with phone)[/bold cyan]"
)
console.print(f"{'=' * 70}")

# Top Priority A
priority_a_sorted = sorted(priority_a, key=lambda b: (-b.deep_score, -b.total_reviews))

# Table
table = Table(title="TOP 50 PRIORITY A LEADS", show_lines=True)
table.add_column("#", justify="right", width=3)
table.add_column("Name", style="bold", max_width=28)
table.add_column("Category", max_width=16)
table.add_column("City", max_width=14)
table.add_column("Score", justify="center", style="bold green", width=5)
table.add_column("Reviews", justify="right", width=5)
table.add_column("Rating", justify="center", width=5)
table.add_column("Website", max_width=10)
table.add_column("Phone", max_width=14)

for i, b in enumerate(priority_a_sorted[:50], 1):
    ws = (
        "NO WEB"
        if not b.has_website
        else "SOCIAL"
        if b.phone
        and any(x in (b.website or "").lower() for x in ["facebook", "instagram"])
        else "WEB"
    )
    table.add_row(
        str(i),
        b.name[:28].replace("[", "(").replace("]", ")"),
        b.category[:16],
        b.city[:14] if b.city else "-",
        str(b.deep_score),
        str(b.total_reviews),
        f"{b.rating:.1f}" if b.rating else "-",
        ws,
        (b.phone or "-")[:14],
    )
console.print(table)

# ====== BY CATEGORY BEST ======
console.print(f"\n{'=' * 70}")
console.print(f"[bold cyan]4. BEST BY CATEGORY (Top 5 each)[/bold cyan]")
for cat in [
    "Salon de Belleza",
    "Peluqueria",
    "Barberia",
    "Spa/Wellness",
    "Gimnasio/Fitness",
    "Estetica/Facial",
    "Tatuajes/Piercing",
]:
    cat_biz = [b for b in businesses if b.category == cat]
    if not cat_biz:
        continue
    cat_biz_sorted = sorted(cat_biz, key=lambda b: (-b.deep_score, -b.total_reviews))[
        :5
    ]

    table = Table(title=f"{cat} - Top 5", show_lines=True)
    table.add_column("Name", style="bold", max_width=32)
    table.add_column("City", max_width=16)
    table.add_column("Score", justify="center", style="bold green", width=5)
    table.add_column("Reviews", justify="right", width=5)
    table.add_column("Phone", max_width=14)

    for b in cat_biz_sorted:
        table.add_row(
            b.name[:32].replace("[", "(").replace("]", ")"),
            b.city[:16] if b.city else "-",
            str(b.deep_score),
            str(b.total_reviews),
            (b.phone or "-")[:14],
        )
    console.print(table)

# ====== CITY ANALYSIS ======
console.print(f"\n{'=' * 70}")
console.print(f"[bold cyan]5. CITY ANALYSIS (Potential by City)[/bold cyan]")
console.print(f"{'=' * 70}")

city_analysis = {}
for b in businesses:
    city = b.city or "Unknown"
    if city not in city_analysis:
        city_analysis[city] = {
            "total": 0,
            "no_web": 0,
            "priority_a": 0,
            "with_phone": 0,
            "reviews": 0,
        }
    city_analysis[city]["total"] += 1
    if not b.has_website:
        city_analysis[city]["no_web"] += 1
    if b.priority == "A":
        city_analysis[city]["priority_a"] += 1
    if b.phone:
        city_analysis[city]["with_phone"] += 1
    city_analysis[city]["reviews"] += b.total_reviews

city_table = Table(title="Cities Ranked by Priority A Leads", show_lines=True)
city_table.add_column("City", style="bold", max_width=20)
city_table.add_column("Total", justify="right", width=6)
city_table.add_column("No Web", justify="right", width=6)
city_table.add_column("Priority A", justify="right", style="bold green", width=8)
city_table.add_column("With Phone", justify="right", width=8)
city_table.add_column("Reviews", justify="right", width=7)
city_table.add_column("Score", justify="right", style="bold", width=6)

for city, data in sorted(city_analysis.items(), key=lambda x: -x[1]["priority_a"])[:20]:
    score = data["priority_a"] * 100 / max(1, data["total"])
    city_table.add_row(
        city[:20],
        str(data["total"]),
        str(data["no_web"]),
        str(data["priority_a"]),
        str(data["with_phone"]),
        str(data["reviews"]),
        f"{score:.0f}%" if score > 0 else "-",
    )
console.print(city_table)

# ====== EXPORT PRIORITY LISTS ======
console.print(f"\n[bold]Exporting prioritized lists...[/bold]")

import pandas as pd
from src.exporter import Exporter

rows = []
for b in businesses:
    rows.append(
        {
            "name": b.name,
            "category": b.category,
            "subcategory": b.subcategory,
            "city": b.city,
            "neighborhood": b.neighborhood,
            "address": b.address,
            "lat": b.lat,
            "lng": b.lng,
            "phone": b.phone,
            "website": b.website,
            "rating": b.rating,
            "total_reviews": b.total_reviews,
            "has_website": b.has_website,
            "deep_score": b.deep_score,
            "priority": b.priority,
            "types": "|".join(b.types) if b.types else "",
        }
    )

df = pd.DataFrame(rows)
df = df.sort_values("deep_score", ascending=False)

Path("data").mkdir(exist_ok=True)
df.to_csv("data/paraguay_beauty_prioritized.csv", index=False, encoding="utf-8-sig")

# Separate exports
df_a = df[df["priority"] == "A"]
df_a.to_csv("data/paraguay_priority_a.csv", index=False, encoding="utf-8-sig")

df_b = df[df["priority"] == "B"]
df_b.to_csv("data/paraguay_priority_b.csv", index=False, encoding="utf-8-sig")

console.print(f"\n[bold green]Files exported:[/bold green]")
console.print(
    f"  paraguay_beauty_prioritized.csv - All {total:,} businesses sorted by score"
)
console.print(f"  paraguay_priority_a.csv - {len(df_a)} Priority A businesses")
console.print(f"  paraguay_priority_b.csv - {len(df_b)} Priority B businesses")

# Summary stats
summary = {
    "total_businesses": total,
    "categories": dict(cat_counts),
    "priority_a_count": len(priority_a),
    "priority_b_count": len(priority_b),
    "with_phone": sum(1 for b in businesses if b.phone),
    "no_website": sum(1 for b in businesses if not b.has_website),
    "city_analysis": {k: dict(v) for k, v in city_analysis.items()},
}

with open("data/deep_analysis_summary.json", "w") as f:
    json.dump(summary, f, indent=2, default=str)

console.print(f"\n[bold]Deep analysis complete![/bold]")
