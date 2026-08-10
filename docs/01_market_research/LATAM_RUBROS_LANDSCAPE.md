# LATAM Rubros Landscape — Organization, Relationships, Relevance to Us

How business activities ("rubros" / "actividades económicas" / "giros" / "atividades") are classified across the 8 major LATAM markets, and what that means for the `paragu-ai-builder` multi-tenant website generator. This is the companion to `PARAGUAY_RUBROS_TAXONOMY.md` (Paraguay-specific) — extended to the region.

**Scope:** Paraguay, Argentina, Uruguay, Chile, Colombia, Peru, Mexico, Brazil.
**Purpose:** decide (a) which classification we normalize against internally, (b) which lead sources to scrape per country, (c) which rubros are universally regulated and need compliance templates, (d) where to expand first.

---

## 1. Three layers of classification

Every LATAM SME is classified against three taxonomies simultaneously. All three matter to us, but for different reasons.

| Layer | Owner | Why **we** care | Public access |
|---|---|---|---|
| **1. Statistical / fiscal** (CIIU Rev.4, SCIAN, CNAE) | National statistics office + tax authority | Authoritative list — every registered business maps here; best for bulk lead sourcing if registry is open | Varies widely (Brazil + Colombia open; Paraguay + Argentina restricted) |
| **2. Regulatory** (MSP, INAN, ANMAT, INVIMA, ANVISA, COFEPRIS…) | Sector ministries / agencies | Tells us which rubros **need compliance pages** on their website (medical, food, financial, legal, construction). Builder already has 5 PY compliance templates; this layer says "replicate per country × rubro". | License numbers publicly queryable per country |
| **3. Commercial / directory** (ClasiPar, MercadoLibre, Sección Amarilla, Páginas Amarillas, Google Business Profile) | Private marketplaces / directories | Where SMEs self-classify to get customers. **Where lead phone/Messaging data actually lives.** Scrape-friendly (most of the Amarillas family) or API-available (MercadoLibre). | Mixed — Amarillas is wide-open; MercadoLibre API is public unauthenticated |

> **The most useful layer for us is (3), cross-walked against (1) for completeness and flagged against (2) for compliance.**

---

## 2. Country-by-country snapshot

### 🇵🇾 Paraguay

| | |
|---|---|
| Official classification | **CNAEP 1.0** / **CAES-Paraguay** (CIIU Rev.4 adaptation) — 4-digit, ~420 classes |
| Issued by | INE (statistics); SET/DNIT adopts for RUC |
| Where encountered | RUC inscription, Marangatu, SUACE |
| Regulators triggering compliance pages | DINAVISA (pharma), INAN (food), BCP/SEPRELAD (finance), MOPC (construction), DINATRAN (transport), CONATEL (telecom) |
| Best lead source | **ClasiPar** (144 rubros, phone + Messaging exposed, no auth) — already mapped in `PARAGUAY_RUBROS_TAXONOMY.md` |
| Bulk public registry | SET consulta per-RUC only; no bulk dump — scraping = per-rubro crawling |
| Builder coverage | ✅ Full — 5 compliance templates (privacy-py, AML-Nexa, INAN-food, cookies, ToS) live |

### 🇦🇷 Argentina

| | |
|---|---|
| Official classification | **CLAE (F.883)** based on **ClaNAE 2010** — 6-digit, ~700+ codes |
| Issued by | ARCA (ex-AFIP) for tax; INDEC for statistics |
| Where encountered | CUIT/Monotributo, F.883 filing, Ingresos Brutos (provincial) |
| Regulators | ANMAT (pharma/food), BCRA + CNV (finance), colegios provinciales (abogacía), IERIC (construction), ENACOM (telecom) |
| Best lead source | **Amarillas/Guía-Senior** (thin post-Clarín), **MercadoLibre AR Servicios** (API: `https://api.mercadolibre.com/sites/MLA/categories`) — chat-only, no phone |
| Bulk public registry | AFIP per-CUIT only; harder to scrape than PY |
| Specific LATAM categories | Remisería, Mudanzas internacionales Mercosur, Tramitador/Gestoría |
| Builder coverage | ✅ Relocation vertical live (Nexa Paraguay targets AR market) |

### 🇺🇾 Uruguay

| | |
|---|---|
| Official classification | **CIIU Rev.4** (direct) + DGI/BPS sub-codes → ~600+ effective codes |
| Issued by | INE; adopted by DGI (tax) + BPS (social security) |
| Where encountered | RUT at DGI, BPS registration |
| Regulators | MSP (health), LATU + bromatología (food), BCU/SSF (finance), MTOP/DNT (transport) |
| Best lead source | **Gallito.com.uy** — phones exposed, strong Empleos/Servicios trees. **MercadoLibre UY** (`sites/MLU/categories`) |
| Bulk public registry | Limited |
| Builder coverage | ✅ Nexa Uruguay live (relocation) — first non-PY tenant |

### 🇨🇱 Chile

| | |
|---|---|
| Official classification | **CIIU4.CL 2012** — 6-digit, ~1,000 SII codes |
| Issued by | SII (tax) + INE |
| Where encountered | "Inicio de Actividades" at SII, boleta electrónica, patente municipal |
| Regulators | ISP (pharma), SEREMI Salud + SAG (food), CMF (finance), MINVU (construction), MTT (transport) |
| Best lead source | **Amarillas.cl** — Yellow Pages taxonomy, ~300–400 rubros, region-faceted (Arica → Santiago), phone + address on every listing. **Yapo.cl** still operational. **MercadoLibre CL** |
| Bulk public registry | SII + CBR scrape-accessible; "Empresa en un Día" portal |
| Builder coverage | ❌ No CL tenant yet — expansion candidate |

### 🇨🇴 Colombia

| | |
|---|---|
| Official classification | **CIIU Rev.4 AC 2022** — 4-digit, ~500 classes. **Open XLSX from DANE.** |
| Issued by | DANE (stats); DIAN adopts via Res. 000114/2020 |
| Where encountered | RUT at DIAN, Cámara de Comercio matrícula, ICA municipal |
| Regulators | INVIMA (pharma/food), Superfinanciera (finance), Consejo Superior Judicatura (legal), Curaduría + SIC (construction) |
| Best lead source | **Páginas Amarillas Colombia (Publicar)** — self-branded "largest commercial directory in LATAM", phone + Messaging public. **MercadoLibre CO**. **RUES** from Confecámaras is queryable. |
| Bulk public registry | **Best in class after Brazil** — RUES + DANE + DIAN all have public endpoints |
| Builder coverage | ❌ No CO tenant — **highest-ROI expansion market** (open data + big population + big SME base) |

### 🇵🇪 Peru

| | |
|---|---|
| Official classification | **CIIU Rev.4** (direct, no rebrand) — 4-digit, ~420 classes |
| Issued by | INEI (stats); SUNAT for RUC |
| Where encountered | RUC inscription, electronic invoicing, municipal license |
| Regulators | DIGEMID (pharma), DIGESA (food), SBS (finance), MINEM (mining — very regulated in PE) |
| Best lead source | **Páginas Amarillas Perú** (digital-only, phone public) — heavy on professional services. **MercadoLibre PE**. SUNAT "Consulta RUC" scrapable per-RUC |
| Bulk public registry | Limited — SUNAT per-RUC |
| Builder coverage | ❌ No PE tenant |

### 🇲🇽 Mexico

| | |
|---|---|
| Official classification | **SCIAN 2023** — **not CIIU-family**; aligned with NAICS (NAFTA). 6-digit, 5 levels, **1,084 classes** (largest in Spanish LATAM). SAT fiscal catalog is *distinct* from SCIAN (gotcha). |
| Issued by | INEGI |
| Where encountered | INEGI economic census, IMSS; SAT uses its own activity catalog at RFC registration |
| Regulators | COFEPRIS (pharma/food), CNBV (finance), SEP (professional licensing), SEDATU (construction), SICT (transport) |
| Best lead source | **Sección Amarilla** (~10M monthly visits, phone exposed, scrape-friendly). **INEGI DENUE** — free geolocated SME directory with API, excellent for leads. **MercadoLibre MX**. **Vivanuncios** (eBay, phone gated). |
| Bulk public registry | **DENUE is gold** — API + downloadable + geolocated, published by INEGI. SAT restricted. |
| Builder coverage | ❌ No MX tenant — biggest Spanish-speaking market; language + currency adaptations needed |

### 🇧🇷 Brazil

| | |
|---|---|
| Official classification | **CNAE 2.3** — 7-digit, 5 levels, **1,332 subclasses** (largest in LATAM) |
| Issued by | IBGE (Concla); Receita Federal adopts for CNPJ |
| Where encountered | CNPJ (primary + secondary CNAEs — drives ISS/ICMS, Simples Nacional eligibility, MEI restrictions — huge practical weight) |
| Regulators | **ANVISA** (pharma/food/cosmetics), BCB/CVM (finance), **OAB mandatory for lawyers**, CREA + CAU (construction/architecture), ANTT (transport) |
| Best lead source | **Receita Federal publishes full CNPJ bulk dump monthly (~60M records with CNAE).** Gold standard. **MercadoLibre MLB** |
| Bulk public registry | **Best in LATAM, no contest.** `https://servicodados.ibge.gov.br/api/docs/CNAE?versao=2` |
| Builder coverage | ❌ No BR tenant — Portuguese adds i18n cost but market is huge and data is public. Tier-1 candidate after CO/MX |

---

## 3. Cross-country rubro mapping (example: "Peluquería")

The same rubro has different codes/labels in each country. This matters because our builder needs **one internal canonical type**, mapped to each country's code for SEO + compliance + form validation.

| Country | Official code | Official label | Directory label | Builder slug |
|---|---|---|---|---|
| Paraguay | CIIU 9602 | Peluquería y otros tratamientos de belleza | Peluquería (ClasiPar 35) | `peluqueria` |
| Argentina | CLAE 960201 | Servicios de peluquería | Peluquería (MLA Servicios) | `peluqueria` |
| Uruguay | CIIU 9602 | Peluquería y otros tratamientos | Peluquería (Gallito) | `peluqueria` |
| Chile | SII 960201 | Peluquería y otros tratamientos de belleza | Peluquería y Barbería (Amarillas.cl) | `peluqueria` |
| Colombia | CIIU 9602 | Peluquería y otros tratamientos de belleza | Peluquería (Publicar) | `peluqueria` |
| Peru | CIIU 9602 | Peluquería y otros tratamientos de belleza | Peluquería (PA PE) | `peluqueria` |
| Mexico | **SCIAN 812110** | Salones y clínicas de belleza, peluquerías y establecimientos similares | Peluquería / Estética (Sección Amarilla) | `peluqueria` |
| Brazil | **CNAE 9602-5/01** | Cabeleireiros, manicure e pedicure | Cabeleireiros (MLB) | `peluqueria` (PT label needed) |

**Takeaway:** CIIU Rev.4 countries share the same 4-digit code (9602). Mexico and Brazil diverge — need country-specific lookup tables.

---

## 4. Universal rubro clusters × what they need from a website

Grouped by **website feature profile**, which is what actually matters to the builder. Each cluster maps to ≥1 of the 23 builder verticals.

### Cluster A — Appointment / Service Booking (highest value for our pitch)
**Examples:** peluquería, barbería, estética, depilación, manicuría, masajes, gimnasio/personal trainer, spa, consultorio odontológico, consultorio médico, veterinaria, peluquería canina, lavadero de autos, taller mecánico (con turno), tatuador.
**Needs:** online booking (Calendly/Cal.com/Fresha), Messaging float, hours widget, service menu with prices + durations, staff bios, gallery, Google reviews widget, Instagram feed.
**Builder verticals:** `beauty-personal-care`, `service-booking`, `pets-animals`, `health-wellness`, `automotive`.
**Regulated?** Health sub-cluster yes (COFEPRIS/ANMAT/ANVISA/INVIMA/DIGEMID/MSP/ISP/DINAVISA).

### Cluster B — Portfolio / Creative Professional
**Examples:** diseñadores gráficos, fotógrafos (bodas, eventos, producto), locutores, ilustradores, maquilladoras/peinadoras para eventos, branding, arquitectos, diseñadores de interiores, productoras audiovisuales, DJs.
**Needs:** large image galleries, case-studies/cases, testimonials, contact form → CRM, pricing packages, Instagram embed.
**Builder verticals:** `portfolio-professional`, `arts-entertainment-venues` (partial).
**Regulated?** Architecture yes (CREA/CAU in BR, colegios in SpAM).

### Cluster C — E-commerce / Catalog
**Examples:** ropa y moda (confección, bordados, estampados), retail local (cosmética, informática, electrodomésticos, ferretería, juguetería), food-beverage (pastelería, chocolatería, heladería, cervecería artesanal), catering con carta fija.
**Needs:** product catalog, Mercado Pago / Stripe / local gateways, shipping calculator, inventory, order tracking, currency selector (dollarized + local).
**Builder verticals:** `retail-local`, `food-beverage`.
**Regulated?** Food requires sanitary permits (INAN/ANMAT/ANVISA/COFEPRIS) — builder **already has INAN template**; replicate per country.

### Cluster D — Lead Generation / High-ACV Consultations
**Examples:** abogados, contadores, despachantes de aduana, gestores, tasadores, seguros (agentes), consultores (RRHH, TI, agronomía), inmobiliaria, corredor inmobiliario, desarrollador inmobiliario, servicios financieros, asesores de inversión, notarios/escribanos.
**Needs:** trust signals (years in business, logos of clients, certifications), practice areas/specialties, consultation form → CRM (HubSpot/Pipedrive), blog for SEO, compliance statements, Messaging for initial contact.
**Builder verticals:** `b2b-professional`, `finance-insurance`, `real-estate-relocation`.
**Regulated?** Almost always — bar associations (OAB, colegios), superfinanciera, BCP, ANMAT for compounded medicines etc.

### Cluster E — Trades / Home Services (emergency-pattern)
**Examples:** electricistas, plomeros, cerrajeros, carpinteros, albañiles, herreros, destapaciones, fumigación, aire acondicionado, pintores, jardinería, limpieza, mudanzas, servicio técnico electrodomésticos "línea blanca".
**Needs:** "call now" button everywhere, emergency indicator section, service area map, before/after gallery, pricing transparency, warranty/certification badges, Messaging.
**Builder verticals:** `trades-home-services`, `logistics-transport` (mudanzas).
**Regulated?** Construction obras mayores yes (municipal + CREA/CAU in BR); small trades mostly not.

### Cluster F — Event / Hospitality (seasonal, high-impact)
**Examples:** salones de fiestas, catering, bebidas, animación/alquiler de juegos, decoración y ambientación, vehículos para eventos, alquiler de carpas/escenarios/mobiliario/indumentaria, fotografía de eventos, DJs, hoteles, hostales, alquiler temporario, excursiones y paseos, agencias de viajes, paquetes turísticos.
**Needs:** availability calendar, booking widget, gallery (weddings/events), package pricing, map, Messaging, multi-locale (for tourism).
**Builder verticals:** `hospitality-tourism`, `arts-entertainment-venues`.
**Regulated?** Hotels register with tourism ministries (SENATUR PY, MINCETUR PE, etc.), food service same as cluster C.

### Cluster G — Education / Training
**Examples:** apoyo escolar, artes plásticas, canto/baile, cocina (academia), computación/informática, conducción (autoescuela), contabilidad, deportes (academias), fotografía, idiomas, instrumentos musicales, marketing digital, maquillaje, mecánica, tatuajes, tecnología.
**Needs:** course catalog, schedule/calendar, instructor bios, enrollment form with payment, testimonials, FAQ.
**Builder verticals:** `education-training`.
**Regulated?** Private schools register with Ministry of Education; technical institutes similar.

### Cluster H — Logistics / Transport
**Examples:** alquiler de autos, encomiendas/mensajerías, mudanzas (local + internacional Mercosur), pasajeros (colectivo/combi/trafic escolar), remolques, remisería, auxilio mecánico.
**Needs:** quote calculator, tracking (if applicable), route/coverage map, fleet photos, reservation form, Messaging.
**Builder verticals:** `logistics-transport`.
**Regulated?** High — DINATRAN (PY), ANTT (BR), MTT (CL), SICT (MX).

### Cluster I — Pets
**Examples:** veterinaria, peluquería canina, adiestramiento, paseadores, pensionados/guarderías, adopciones, traslados, cruza.
**Needs:** booking, pet profile forms, service menu, gallery (before/after grooming), testimonials, Messaging.
**Builder verticals:** `pets-animals`.
**Regulated?** Veterinary license required (colegios de veterinarios); others not.

### Cluster J — B2B Industrial / Manufacturing
**Examples:** imprenta (folletería, gran formato, láser), oficinas (fotocopiadoras, ascensores, dispensers), equipamiento industrial, proveedores agroindustriales, maquilas.
**Needs:** product catalog with spec sheets, RFQ form, client logos, ISO/certification badges, case studies.
**Builder verticals:** `b2b-professional`, `trades-industrial`, `agriculture-agribusiness`.

### Cluster K — Pharmacy / Medical Retail (very regulated)
**Examples:** farmacias, ópticas, ortopedia, prepagas, ambulancias, laboratorios clínicos.
**Needs:** catálogo + recetas + compliance notices ("receta obligatoria"), regulator license number prominent, delivery integration.
**Builder verticals:** `health-wellness`, `retail-local` (for farmacia retail side).
**Regulated?** Max — dedicated compliance page per country.

---

## 5. Universally regulated rubros (need compliance templates per country)

From layer 2. If we pitch any of these, the builder must inject a compliance page keyed by **country × rubro**. Builder already has the pattern for PY — replicate the data structure for 7 more countries.

| Rubro cluster | Regulator by country |
|---|---|
| Pharma / medicamentos | PY DINAVISA · AR ANMAT · UY MSP · CL ISP · CO INVIMA · PE DIGEMID · MX COFEPRIS · BR ANVISA |
| Food handling / restaurants | PY INAN · AR ANMAT+SENASA · UY LATU+bromatología · CL SEREMI+SAG · CO INVIMA · PE DIGESA · MX COFEPRIS · BR ANVISA |
| Banking / finance | PY BCP · AR BCRA+CNV · UY BCU · CL CMF · CO Superfinanciera · PE SBS · MX CNBV · BR BCB+CVM |
| Healthcare pros | All: college/board licensing mandatory |
| Construction (obra mayor) | All: municipal permits; BR adds CREA+CAU mandatory |
| Legal services | All: bar associations; **BR OAB mandatory** (lawyer can't practice without OAB number) |
| Transport | PY DINATRAN · AR CNRT · UY MTOP · CL MTT · CO Supertransporte · PE MTC · MX SICT · BR ANTT |
| Private education | Ministry of Education in each country |
| Insurance brokers | Same regulators as banking in most countries |

**Build recommendation:** a single `src/compliance/<country>/<cluster>.json` keyed file per (country, cluster) — 8 × 9 = 72 templates max; most can be generated from 9 master templates with country variable substitution.

---

## 6. Prioritized expansion matrix

Where do we deploy builder capacity next? Scored on **market size × data openness × builder readiness × language cost**.

| Country | Size (SMEs, M) | Open bulk data? | Builder ready? | Language | Recommendation |
|---|---:|---|---|---|---|
| Paraguay | ~0.3 | Partial (ClasiPar scrape, SET per-RUC) | ✅ 6 compliance templates, 5 live tenants | es | **Anchor** — keep deepening |
| Uruguay | ~0.15 | Partial (Gallito scrape) | ✅ Nexa Uruguay live | es | Expand beauty + health verticals |
| Argentina | ~4 | Limited (AFIP per-CUIT) | ✅ Relocation vertical tested | es | Broad expansion after MP/billing localized |
| Colombia | ~1.6 | **Open (RUES + DANE XLSX + Publicar scraping)** | ❌ No tenant | es | **Top expansion target** — data + size + no language cost |
| Mexico | ~4.9 | **Open (DENUE API geolocated)** | ❌ No tenant | es-MX | **Tier 1** — largest Spanish market, DENUE is a lead goldmine; SCIAN ≠ CIIU so needs mapping work |
| Peru | ~2 | Limited (SUNAT per-RUC) | ❌ No tenant | es | Tier 2 — after CO/MX |
| Chile | ~1.4 | Partial (SII + Amarillas.cl scraping) | ❌ No tenant | es-CL | Tier 2 — high GDP, but smaller SME base than CO/MX |
| Brazil | ~20 | **Open (CNPJ monthly dump — gold)** | ❌ No tenant | pt-BR | **Tier 1 long-term** — largest LATAM market, best data; needs Portuguese i18n buildout |

**Call:** after stabilizing PY+UY+AR, prioritize **Colombia (cost-effective, Spanish, open data)** and **Mexico (largest market, DENUE lead goldmine)** in parallel. Brazil is a later strategic play worth the Portuguese investment.

---

## 7. Data sources summary (for future scraping)

### Tier 1 — open, structured, instant
- **Brazil IBGE CNAE API** — `https://servicodados.ibge.gov.br/api/docs/CNAE?versao=2`
- **Brazil Receita Federal CNPJ bulk dump** — full SME universe, monthly
- **Mexico INEGI DENUE API** — geolocated SMEs
- **Colombia DANE CIIU Rev.4 AC 2022 XLSX** — `https://www.dane.gov.co/files/sen/nomenclatura/ciiu/CIIU_Rev_4_AC2022.pdf`
- **MercadoLibre Categories API** (all countries) — `https://api.mercadolibre.com/sites/{MLA|MLU|MLC|MCO|MLM|MPE|MLB}/categories`
- **Google Business Profile categories (es-419)** — mirrored by PlePer + `blakeem/All-Google-Business-Categories` GitHub repo

### Tier 2 — public but requires HTML scraping
- **Paraguay ClasiPar** — 144 rubros already mapped (`PARAGUAY_RUBROS_TAXONOMY.md`)
- **Uruguay Gallito** — Empleos + Servicios with phone exposed
- **Chile Amarillas.cl + Yapo.cl** — phone exposed, region-faceted
- **Colombia Publicar (Páginas Amarillas)** — phone + Messaging exposed
- **Mexico Sección Amarilla** — phone exposed, ~10M monthly visits
- **Peru Páginas Amarillas** — phone public

### Tier 3 — per-record lookup only (no bulk)
- Paraguay SET consulta per-RUC
- Argentina AFIP per-CUIT
- Peru SUNAT per-RUC

### What's not useful for leads
- MercadoLibre / OLX / Vivanuncios — contact is platform-gated (chat only, no phone)
- Yelp LATAM — thin coverage

---

## 8. Action items for the builder

1. **Adopt Google Business Profile `es-419` categories as canonical internal IDs.** Store a crosswalk table to: (CIIU Rev.4 · SCIAN · CNAE · MercadoLibre cat IDs per site · Amarillas labels per country · ClasiPar rubro IDs). One row per business-type, 8 code columns.
2. **Add country field to tenant `site.json`** (already exists as `country`) and route compliance page content by `country × rubro cluster`.
3. **Replicate the 5 PY compliance templates for 7 more countries** — `src/compliance/{py,ar,uy,cl,co,pe,mx,br}/{pharma,food,legal,finance,construction,transport,education,health}.json`.
4. **Build per-country scrapers** in priority order: MX (DENUE API) → CO (Publicar + RUES) → BR (CNPJ dump) → CL (Amarillas.cl) → PE (PA PE). PY ClasiPar scraper already the template.
5. **Expand the 17 P1–P5 registry gaps from `PARAGUAY_RUBROS_TAXONOMY.md`** so beauty+health+legal+finance+transport coverage is 100% before we pitch cross-country.
6. **Add i18n dimension to `src/content/`** — today copy is Spanish-only; need `es-AR` (vos), `es-MX` (different register), `pt-BR` for Brazil.

---

## 9. Open questions

- **Do we need SCIAN ↔ CIIU mapping ourselves, or is there a published crosswalk?** INEGI publishes a SCIAN↔ISIC correspondence table; worth downloading before we invest engineering time.
- **Should internal IDs be GBP leaves (~4,000) or our existing ~1,900 registry types?** GBP gives SEO alignment and future-proof category coverage; our registry is curated for website-feature relevance. Probably: keep registry types as internal, add GBP-ID column for SEO/Structured Data output.
- **Legal exposure of scraping each source.** ClasiPar + Amarillas family have no explicit API but ToS vary; MercadoLibre API is explicit public. Validate with counsel per-country before batch scraping.

---

*Document created: April 2026 · Based on parallel agent research across 8 LATAM markets · Companion to `PARAGUAY_RUBROS_TAXONOMY.md` · Sources verified April 2026, links may age.*
