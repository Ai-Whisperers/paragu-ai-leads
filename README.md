# Paraguay Beauty & Wellness Business Data

Comprehensive dataset of beauty, wellness, and fitness businesses across Paraguay, extracted from Google Maps. Built for lead generation and market analysis for [Vete/Paragu-AI](https://github.com/Ai-Whisperers/Vete).

## 📊 Dataset Overview

| Metric | Value |
|---|---|
| Total Businesses | **7,463** |
| Cities Covered | **209** |
| No Website | **75%** (5,602) |
| Social Media Only | **17%** (1,298) |
| Has Website | **8%** (563) |
| With Phone Number | **81%** (6,079) |
| Priority A Leads | **3,960** (53%) |
| Priority B Leads | **2,836** (38%) |

## 🎯 Lead Priority Segmentation

### Priority A (Score 70-100): 3,960 businesses
Best targets — high review count, good ratings, no website, contactable
- With phone: 3,682
- Average rating: 4.2+
- 50+ reviews

### Priority B (Score 50-69): 2,836 businesses
Secondary targets — decent potential, may need follow-up
- With phone: 2,067
- 20-50 reviews

### Priority C (Score 30-49): 625 businesses
Low priority — fewer reviews or has website

## 📂 Data Files

### Prioritized Leads (Recommended)
- `paraguay_priority_a.csv` — 3,960 Priority A leads (START HERE)
- `paraguay_priority_b.csv` — 2,836 Priority B leads
- `paraguay_beauty_prioritized.csv` — All 7,463 sorted by score

### By Scope
- `asuncion_paraguay_beauty_nationwide_all_businesses_*.csv` — Full nationwide dataset
- `asuncion_beauty_complete_all_businesses_*.csv` — Greater Asunción only

### Analysis Files
- `paraguay_beauty_nationwide_full_report_*.xlsx` — Excel with multiple sheets
- `paraguay_priority_a.csv` — The gold list for outreach

## 📋 CSV Columns

| Column | Description |
|---|---|
| name | Business name |
| category | Peluqueria, Salon, Spa, Gimnasio, Barberia, etc. |
| subcategory | More specific: Spa, Centro Estetica, etc. |
| city | City name |
| neighborhood | Area within city |
| address | Full address |
| lat/lng | GPS coordinates |
| phone | Contact phone |
| website | Website URL |
| rating | Google rating (0-5) |
| total_reviews | Number of reviews |
| has_website | Boolean |
| deep_score | Priority score (0-100) |
| priority | A/B/C/D |
| types | Google place types |

## 🏆 Top Categories

| Category | Count | Priority A |
|---|---|---|
| Peluqueria | 1,293 | 794 |
| Salon de Belleza | 1,210 | 677 |
| Gimnasio/Fitness | 1,073 | 743 |
| Spa/Wellness | 864 | 528 |
| Barberia | 778 | 469 |
| Uñas/Nails | 595 | 126 |
| Tatuajes/Piercing | 275 | 95 |

## 🗺️ Top Cities

| City | Priority A | Total |
|---|---|---|
| Asunción | 348 | 492 |
| Fernando de la Mora | 206 | 277 |
| Ciudad del Este | 196 | 348 |
| San Lorenzo | 182 | 278 |
| Lambaré | 168 | 237 |
| Luque | 156 | 247 |
| Ñemby | 134 | 229 |
| Capiatá | 134 | 227 |

## 🔬 Deep Score Methodology

Score (0-100) based on:

| Factor | Max Points |
|---|---|
| No website | +40 |
| Social media only | +30 |
| 200+ reviews | +30 |
| 100+ reviews | +25 |
| 50+ reviews | +20 |
| Rating 4.5+ | +15 |
| Rating 4.0+ | +12 |
| Has phone | +10 |
| High-value category (Spa/Gimnasio) | +10 |
| Large business indicator | +5 |

### Priority Assignments
- **A**: Score 70-100 (3,960)
- **B**: Score 50-69 (2,836)
- **C**: Score 30-49 (625)
- **D**: Score <30 (42)

## 🚀 Recommended Outreach Strategy

### Phase 1: Asunción Launch (348 Priority A)
Start with Asunción — highest concentration, best conversion potential
- All have 50+ reviews, 4.0+ ratings, no website
- Easy pitch: "Sitio web gratis + reservas por WhatsApp"

### Phase 2: Best Categories
Priority order:
1. **Peluquerías** — 794 targets, repeat clients, perfect for Vete booking
2. **Gimnasios** — 743 targets, memberships need management
3. **Salones de Belleza** — 677 targets, services + retail

### Phase 3: Secondary Cities
- Fernando de la Mora (206)
- San Lorenzo (182)
- Lambaré (168)

## 📈 Data Quality Notes

- 75% have NO website — huge opportunity
- 81% have phone numbers — contactable
- Average rating: 4.2 (high quality businesses)
- Most businesses are established (have reviews)

## 🔗 Source

- Google Maps Places API
- 46 cities searched across Paraguay
- 1,666 keyword queries
- Checkpoint-based scraping for reliability

## 📅 Data Collection Dates

- Initial scrape: April 14-15, 2026
- Full nationwide: 7,463 businesses

## 📝 License

This data is for lead generation and market research purposes. Ensure compliance with Google's Terms of Service when using.

## 🔧 Related Tools

- [maps-extractor](https://github.com/Ai-Whisperers/maps-extractor) — Google Maps scraping tool
- [Vete](https://github.com/Ai-Whisperers/Vete) — SaaS platform for beauty/wellness businesses

---

**Generated for Vete/Paragu-AI market expansion**
