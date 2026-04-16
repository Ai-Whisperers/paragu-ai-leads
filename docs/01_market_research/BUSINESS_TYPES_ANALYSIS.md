# Business Types Analysis — Paraguay Lead Data

Comprehensive audit of business types present in the Google Maps scrape, the taxonomy that maps them, coverage gaps, and opportunities for expansion.

**Data source:** `data/processed/paraguay_beauty_prioritized.csv` (7,463 businesses)
**Place types source:** Google Places Legacy API (`googlemaps==4.10.0`), 102 supported types.

---

## 1. The 4-Layer Taxonomy

Every business in the dataset flows through four classification layers:

```
Google Places Types  →  Vertical  →  Beauty Category  →  Subcategory
(raw type tags)         (16+)       (12)                 (keyword-derived)
```

1. **Google Places Types** — raw tags from Google (e.g. `hair_care`, `beauty_salon`, `establishment`). Every business has several. Defined in `src/config.py::GOOGLE_PLACE_TYPES` (102 legacy types).
2. **Verticals** — high-level industry grouping used for cross-sector analysis. 17 verticals in `VERTICAL_MAPPING`, assigned in `src/analyzer.py::_assign_vertical`.
3. **Beauty Categories** — 12 Spanish-language beauty & wellness classes assigned via keyword matching in `scripts/deep_analysis.py::categorize_business`. Only populated for businesses in the "Beauty & Wellness" vertical.
4. **Subcategories** — finer distinctions (e.g. "barberia_moderna" vs "barberia_tradicional") also from keyword rules.

---

## 2. Google Places Types Coverage

### 2.1 Types currently in the scraped data

57 distinct Google place types appear in the 7,463-row CSV. Top 20 by frequency:

| Type | Count | Share of rows |
|---|---:|---:|
| establishment | 7,460 | 100% |
| point_of_interest | 7,460 | 100% |
| health | 2,395 | 32.1% |
| hair_care | 2,272 | 30.4% |
| beauty_salon | 2,060 | 27.6% |
| gym | 1,075 | 14.4% |
| store | 732 | 9.8% |
| spa | 671 | 9.0% |
| lodging | 112 | 1.5% |
| food | 77 | 1.0% |
| doctor | 70 | 0.9% |
| clothing_store | 54 | 0.7% |
| shopping_mall | 51 | 0.7% |
| physiotherapist | 46 | 0.6% |
| grocery_or_supermarket | 35 | 0.5% |
| hospital | 33 | 0.4% |
| supermarket | 29 | 0.4% |
| restaurant | 26 | 0.3% |
| bar | 18 | 0.2% |
| jewelry_store | 15 | 0.2% |

A further 37 types (dentist, pharmacy, night_club, park, cafe, etc.) appear in smaller counts. Full distribution is in section 8.

### 2.2 Meta types (always present, not a business classifier)

Google tags every place with `establishment` and `point_of_interest`. These are not useful for vertical classification and are now captured in `src/config.py::META_TYPES` so `analyzer.py` can skip them.

### 2.3 Coverage fixes applied

Before this audit, 10 types from the data and 3 defined types had **no vertical mapping**. They now do:

| Type | Occurrences in data | New vertical |
|---|---:|---|
| health | 2,395 | Health & Medical |
| food | 77 | Food & Beverage |
| grocery_or_supermarket | 35 | Food Retail |
| park | 10 | Recreation (new vertical) |
| place_of_worship | 4 | Religious |
| general_contractor | 1 | Home Services |
| finance | 1 | Finance |
| aquarium | 0 | Recreation |
| zoo | 0 | Recreation |

Meta types (`establishment`, `point_of_interest`, `locality`, `political`) now live in `META_TYPES` and are intentionally not mapped to a vertical.

**Result:** All 102 legacy place types are mapped. All 57 types in production data resolve to a real vertical (or are correctly ignored as meta tags).

---

## 3. The 17 Verticals

Defined in `src/config.py::VERTICAL_MAPPING`. Every legacy Google place type now belongs to exactly one vertical.

| Vertical | Example types | Purpose |
|---|---|---|
| Food & Beverage | restaurant, cafe, bar, bakery, food | Core F&B operators |
| Food Retail | bakery, supermarket, grocery_or_supermarket, liquor_store | Food product stores |
| Health & Medical | hospital, doctor, dentist, pharmacy, health, physiotherapist | Clinical providers |
| **Beauty & Wellness** | beauty_salon, hair_care, spa, gym | **Current primary target** |
| Retail & Shopping | clothing_store, jewelry_store, store, shopping_mall | General retail |
| Automotive | car_dealer, car_repair, car_wash, gas_station | Vehicle services |
| Professional Services | lawyer, accounting, real_estate_agency | B2B services |
| Home Services | electrician, plumber, painter, general_contractor | Residential trades |
| Lodging & Tourism | lodging, campground, tourist_attraction | Hospitality |
| Entertainment & Nightlife | night_club, movie_theater, casino, stadium | Leisure venues |
| Education | school, university, library | Learning institutions |
| Finance | bank, atm, finance | Banking |
| Government & Public | city_hall, police, post_office, embassy | Public sector |
| Transportation | airport, bus_station, taxi_stand, parking | Transit |
| Religious | church, mosque, synagogue, place_of_worship | Places of worship |
| Arts & Culture | museum, art_gallery | Cultural venues |
| Recreation | park, aquarium, zoo | Outdoor / leisure |
| Funeral | funeral_home | End-of-life services |

Analyzer falls back to `DEFAULT_VERTICAL = "Other"` if a business has no recognized type after meta filtering.

---

## 4. The 12 Beauty Categories — Current Target Market

Assigned by `scripts/deep_analysis.py::categorize_business` using Spanish/English keyword matching against the business name, with the Google type as a tiebreaker.

| # | Category (ES) | Count | Share | % with website |
|---:|---|---:|---:|---:|
| 1 | Peluquería (hair salons) | 1,293 | 17.3% | 15.5% |
| 2 | Salón de Belleza (beauty salons) | 1,210 | 16.2% | 25.5% |
| 3 | Gimnasio/Fitness | 1,073 | 14.4% | 28.3% |
| 4 | Otros (uncategorized) | 963 | 12.9% | 34.6% |
| 5 | Spa/Wellness | 864 | 11.6% | 24.4% |
| 6 | Barbería | 778 | 10.4% | 21.1% |
| 7 | Uñas/Nails | 595 | 8.0% | 24.5% |
| 8 | Tatuajes/Piercing | 275 | 3.7% | 29.8% |
| 9 | Maquillaje (makeup) | 174 | 2.3% | 26.4% |
| 10 | Estética/Facial | 169 | 2.3% | 25.4% |
| 11 | Pestañas/Cejas (lashes/brows) | 49 | 0.7% | 36.7% |
| 12 | Depilación (hair removal) | 20 | 0.3% | 25.0% |
| | **Total** | **7,463** | **100%** | **~24%** |

**Takeaway:** Peluquería has the lowest web adoption (15.5%), making it the single largest underserved segment — 1,092 businesses without a website.

### 4.1 Category profiles

Each profile lists the keyword triggers used by the categorizer, typical services, and Vete-platform fit.

**Peluquería** — 1,293 | hair cuts, coloring, treatments. Keywords: `peluqueria`, `peluqueria`, `hair salon`. Unisex by default. **Fit:** booking + Instagram feed templates.

**Salón de Belleza** — 1,210 | multi-service (hair, nails, makeup). Keywords: `salon`, `belleza`, `salón`. **Fit:** service catalog + tiered pricing templates.

**Gimnasio/Fitness** — 1,073 | gyms, crossfit boxes, yoga/pilates studios. Keywords: `gym`, `gimnasio`, `fitness`, `crossfit`, `yoga`, `pilates`. **Fit:** class schedule + recurring membership templates.

**Otros** — 963 | businesses whose names don't trip any keyword (often wellness-adjacent: therapy, aesthetics, holistic). Needs either manual review or additional keywords.

**Spa/Wellness** — 864 | massage, relaxation, holistic. Keywords: `spa`, `masaje`, `wellness`, `relax`. **Fit:** service booking + package pricing.

**Barbería** — 778 | male grooming specialists. Keywords: `barber`, `barberia`, `barbería`. **Fit:** quick-booking + walk-in slot templates.

**Uñas/Nails** — 595 | manicure, pedicure, acrylics. Keywords: `nail`, `uñas`, `unas`, `manicure`. **Fit:** service + portfolio gallery.

**Tatuajes/Piercing** — 275 | tattoo + piercing studios. Keywords: `tattoo`, `tatuaje`, `piercing`, `ink`. **Fit:** artist portfolio + consultation booking.

**Maquillaje** — 174 | makeup artists (often mobile/event). Keywords: `maquillaje`, `makeup`, `make up`. **Fit:** portfolio + quote request templates.

**Estética/Facial** — 169 | facial treatments, dermo-aesthetics. Keywords: `estetica`, `estética`, `facial`. **Fit:** treatment catalog + consultation booking.

**Pestañas/Cejas** — 49 | lash extensions, microblading, brow lamination. Keywords: `pestanas`, `pestañas`, `cejas`, `lashes`, `brows`. **Fit:** before/after gallery templates.

**Depilación** — 20 | waxing, laser hair removal. Keywords: `depilacion`, `depilación`, `waxing`, `laser`. **Fit:** zone-pricing booking templates.

---

## 5. Secondary Tags — Expansion Signal

Google attaches multiple type tags to a single business. Beauty & wellness places in our data also carry non-beauty tags that reveal expansion targets:

| Secondary tag | Count | Why it appears | Expansion signal |
|---|---:|---|---|
| store | 732 | Business also sells products | Retail vertical — sell online store templates |
| lodging | 112 | Spa/salon inside a hotel | Hotel & resort wellness partnerships |
| doctor | 70 | Medical aesthetics clinics | Health & Medical lead pool |
| clothing_store | 54 | Boutique + salon hybrid | Fashion vertical |
| shopping_mall | 51 | Located in a mall | Mall-tenant directory play |
| physiotherapist | 46 | Wellness + rehab | Health & Medical |
| hospital | 33 | Medical aesthetics inside hospitals | Health & Medical |
| restaurant / bar / cafe | 49 | Juice bar / spa café / beauty-café | Food & Beverage vertical |
| night_club | 11 | Tattoo studios near nightlife | Entertainment adjacency |
| jewelry_store | 15 | Adjacent to salon | Retail & Shopping |

These signals are already captured by the full vertical mapping — they just need a scrape pass that doesn't filter by `beauty_salon|hair_care|spa|gym` to surface new leads.

---

## 6. Dataset Metrics

- **Total businesses:** 7,463
- **Average rating:** 3.92
- **Total reviews across dataset:** 357,898
- **With phone number:** 6,079 (81.5%)
- **With any website:** 1,861 (24.9%)
- **Without any website:** 5,602 (75.1%)

**Lead implication:** 3 out of every 4 businesses have no website at all. Combined with categories showing 15–37% web adoption, the addressable gap is very wide.

---

## 7. Expansion Roadmap

### 7.1 Immediate — within Beauty & Wellness
- **Peluquerías (1,092 no-web)** — highest-volume underserved segment
- **Barberías (614 no-web)** — fastest-growing male grooming segment, low web adoption

### 7.2 Short-term — adjacent verticals already partially in data
- **Health & Medical:** 2,395 rows tagged `health`, plus doctor (70), dentist (8), physiotherapist (46), pharmacy (15). Rescraping with medical query terms would multiply this.
- **Food & Beverage:** restaurant (26), cafe (5), bar (18), plus 77 generic `food`. Core vertical waiting for a dedicated scrape.
- **Retail & Shopping:** store (732) + clothing_store (54) + jewelry_store (15). Many are already in the dataset as salon-adjacent businesses.

### 7.3 Medium-term — new scrape campaigns
Run the existing pipeline with different query types:

```python
# src/scraper.py, change SEARCH_TYPES
SEARCH_TYPES = ["restaurant", "cafe", "bar"]          # F&B
SEARCH_TYPES = ["doctor", "dentist", "physiotherapist"]  # Health
SEARCH_TYPES = ["clothing_store", "jewelry_store"]    # Retail
```

The vertical mapping now covers every type these scrapes will return.

### 7.4 Long-term — migrate to the new Places API

The legacy API supports ~102 types. The **New Places API (v1)** supports ~180+ types with much finer granularity:

- `barber_shop`, `nail_salon`, `hair_salon`, `beauty_salon` — direct replacement for keyword heuristics
- `yoga_studio`, `athletic_field`, `fitness_center` — splits today's `gym` into 3
- `dental_clinic`, `medical_lab`, `optician` — splits today's `doctor`
- `american_restaurant`, `chinese_restaurant`, `brazilian_restaurant` … (~30 cuisine-specific)
- `ev_charging_station`, `dog_park`, `ice_cream_shop` — modern amenities

Migration would:
1. Replace the keyword-based `categorize_business` with direct Google types for most beauty categories.
2. Increase scrape efficiency (more targeted search).
3. Require changing the client from `googlemaps==4.10.0` to the new REST endpoint.

---

## 8. Appendix — Full Type Distribution (all 57 types seen in data)

| Type | Count | Vertical |
|---|---:|---|
| establishment | 7,460 | (meta) |
| point_of_interest | 7,460 | (meta) |
| health | 2,395 | Health & Medical |
| hair_care | 2,272 | Beauty & Wellness |
| beauty_salon | 2,060 | Beauty & Wellness |
| gym | 1,075 | Beauty & Wellness |
| store | 732 | Retail & Shopping |
| spa | 671 | Beauty & Wellness |
| lodging | 112 | Lodging & Tourism |
| food | 77 | Food & Beverage |
| doctor | 70 | Health & Medical |
| clothing_store | 54 | Retail & Shopping |
| shopping_mall | 51 | Retail & Shopping |
| physiotherapist | 46 | Health & Medical |
| grocery_or_supermarket | 35 | Food Retail |
| hospital | 33 | Health & Medical |
| supermarket | 29 | Food Retail |
| restaurant | 26 | Food & Beverage |
| bar | 18 | Food & Beverage |
| jewelry_store | 15 | Retail & Shopping |
| pharmacy | 15 | Health & Medical |
| night_club | 11 | Entertainment & Nightlife |
| park | 10 | Recreation |
| tourist_attraction | 8 | Lodging & Tourism |
| dentist | 8 | Health & Medical |
| home_goods_store | 7 | Retail & Shopping |
| cafe | 5 | Food & Beverage |
| place_of_worship | 4 | Religious |
| church | 3 | Religious |
| car_wash | 3 | Automotive |
| electronics_store | 3 | Retail & Shopping |
| drugstore | 3 | Health & Medical |
| car_repair | 3 | Automotive |
| locality | 3 | (meta) |
| political | 3 | (meta) |
| campground | 2 | Lodging & Tourism |
| hardware_store | 2 | Retail & Shopping |
| stadium | 2 | Entertainment & Nightlife |
| veterinary_care | 2 | Health & Medical |
| art_gallery | 2 | Arts & Culture |
| convenience_store | 1 | Food Retail |
| travel_agency | 1 | Professional Services |
| museum | 1 | Arts & Culture |
| department_store | 1 | Retail & Shopping |
| laundry | 1 | Home Services |
| parking | 1 | Transportation |
| school | 1 | Education |
| university | 1 | Education |
| rv_park | 1 | Lodging & Tourism |
| gas_station | 1 | Automotive |
| general_contractor | 1 | Home Services |
| liquor_store | 1 | Food & Beverage |
| finance | 1 | Finance |
| casino | 1 | Entertainment & Nightlife |
| insurance_agency | 1 | Professional Services |
| florist | 1 | Retail & Shopping |
| furniture_store | 1 | Retail & Shopping |

---

## 9. Code References

- `src/config.py:27` — `GOOGLE_PLACE_TYPES` (102 legacy types)
- `src/config.py:132` — `META_TYPES` (12 generic tags to skip)
- `src/config.py:147` — `VERTICAL_MAPPING` (17 verticals)
- `src/config.py:291` — `DEFAULT_VERTICAL = "Other"`
- `src/analyzer.py` — `_TYPE_TO_VERTICAL` lookup and `_assign_vertical` (skips meta types, uses primary-type order)
- `scripts/deep_analysis.py` — `categorize_business` (12-category keyword classifier)
