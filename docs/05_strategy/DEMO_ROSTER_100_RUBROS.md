# Paraguay Demo Roster — 110 Rubros

Execution plan for standing up **110 demo tenants** in `paragu-ai-builder`, one per Paraguayan rubro, to use as (a) sales pitch artifacts, (b) SEO long-tail landing pages, (c) builder-engine regression coverage across the vertical taxonomy.

**Target:** 110 demos (10% buffer over the 100 ask) live under `sites/demo-*/` in the builder, reachable at `/s/es/demo-<rubro>/` and linked from `/p/<rubro>` marketing pages.

**Paraguay-first:** all demos scoped to PY (locale `es`, PYG currency, PY phone format `+595`, Asunción-metro city fixtures).

---

## 1. What we already have

From `paragu-ai-builder` (audit of `web/app/` and `web/scripts/`):

| Asset | Status | Usage for demos |
|---|---|---|
| `/app/p/[rubro]/` route | ✅ Live (PR #59) | Per-vertical marketing landing (features, pricing hook). Links to matching demo. |
| `/app/demo/` route | ✅ Live (#62) | Single demo route — we'll parameterize per rubro. |
| `sites/dayah-litworks/` pattern | ✅ Live | Template for demo→real migration (`migratedFrom: "web/lib/engine/demo-data.ts"`). |
| `web/scripts/new-tenant.ts` | ✅ Exists | Scaffold new `sites/<slug>/` directory with site.json + pages. |
| `web/scripts/generate-site.ts` | ✅ Exists | Generate full site content from registry + content templates. |
| `web/scripts/generate-preview.ts` | ✅ Exists | Preview without committing to `sites/`. |
| `web/scripts/migrate-demo-to-site.ts` | ✅ Exists | Promote demo → real tenant. |
| `src/content/<vertical>.content.json` | ✅ 9 beauty verticals extracted, more from v3 | Pre-written Spanish copy per vertical. |
| `sites/shared-images/` | ✅ Exists | Shared image pool — avoid per-demo asset duplication. |
| Builder registry `src/registry/*.type.json` | ✅ 1,900+ types | Feature flags + SEO per business type. |
| Compliance templates | ✅ 5 for PY (privacy-py, AML-Nexa, INAN-food, cookies, ToS) | Auto-injected by `legal-review-gate.ts` when required. |

> **Implication:** scaffolding a demo is ~5 min of scripted work per rubro. 110 demos = **~1 day of batch execution** + 1–2 days for image curation and QA.

---

## 2. Selection criteria

We're picking 110 from the full ClasiPar 144 + builder's 1,900 types. Rules:

1. **Must have a matching `<slug>.type.json`** in `paragu-ai-builder/src/registry/`. Skip the 17 P1–P5 registry gaps from `PARAGUAY_RUBROS_TAXONOMY.md` §4 — those come after the gaps are closed.
2. **Prefer Spanish-slug canonical types** (`peluqueria`, `contador`) over English variants (`hair_salon`, `cpa_firm`) when both exist — Spanish is the pitch language.
3. **One demo per distinct website feature profile** — don't do three variants that render identically. E.g. `unas` covers `gel_acrylic_nail_studio` + `dip_powder_nail_studio`.
4. **Distribute across the 11 website-need clusters** from `LATAM_RUBROS_LANDSCAPE.md` §4 so the roster showcases full builder range.
5. **Sequence by complexity**, not by volume — Wave 1 = zero compliance, Wave 2 = mild regulation, Wave 3 = heavy regulation + compliance pages.

---

## 3. The 110 rubros — by wave

### Wave 1 (40) — Fast lane. Zero regulation, high PY SME volume, beauty/trades/events/pets.
*Target: ship all 40 in the first batch (1 day).*

#### Beauty & personal care (10)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 1 | `peluqueria` | Peluquería | A Booking |
| 2 | `barberia` | Barbería | A Booking |
| 3 | `unas` | Manicuría y Pedicuría | A Booking |
| 4 | `estetica` | Estética | A Booking |
| 5 | `depilacion` | Depilación | A Booking |
| 6 | `tatuajes` | Tatuajes | A Booking |
| 7 | `body_piercing_studio` | Piercings | A Booking |
| 8 | `spa` / `day_spa` | Spa | A Booking |
| 9 | `brazilian_wax_studio` | Depilación brasileña | A Booking |
| 10 | `facial_spa` | Spa facial | A Booking |

#### Fitness & wellness (7)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 11 | `gimnasio` | Gimnasio | A Booking |
| 12 | `crossfit_box` | CrossFit | A Booking |
| 13 | `functional_training_studio` | Entrenamiento funcional | A Booking |
| 14 | `dance_fitness_studio` | Baile fitness / Zumba | A Booking |
| 15 | `boxing_gym_training` | Boxeo | A Booking |
| 16 | `yoga_studio` (verify) | Yoga | A Booking |
| 17 | `aromatherapy_studio` | Aromaterapia | A Booking |

#### Pets (5)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 18 | `general_veterinary_clinic` → `veterinaria` | Veterinaria | A/I |
| 19 | `dog_grooming_salon` | Peluquería canina | A/I |
| 20 | `dog_obedience_trainer` | Adiestramiento canino | I |
| 21 | `dog_walker` | Paseador de perros | I |
| 22 | `dog_boarding_kennel` | Pensionado canino | I |

#### Trades / home services (10)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 23 | `electricista` | Electricista | E Trades |
| 24 | `general_plumber` | Plomero | E Trades |
| 25 | `cerrajero` | Cerrajero | E Trades |
| 26 | `carpintero` | Carpintero | E Trades |
| 27 | `albanil` | Albañil | E Trades |
| 28 | `herreria` | Herrería | E Trades |
| 29 | `aire_acondicionado` | Aire acondicionado | E Trades |
| 30 | `handyman_service` | Servicio de mantenimiento | E Trades |
| 31 | `fumigacion` | Fumigación | E Trades |
| 32 | `house_cleaning_service` | Limpieza de hogar | E Trades |

#### Events — party vendors (8)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 33 | `catering` | Catering | F Events |
| 34 | `banquet_hall` | Salón de fiestas | F Events |
| 35 | `estancia_event_venue` | Estancia para eventos | F Events |
| 36 | `bouncy_castle_rental` | Alquiler de castillos inflables | F Events |
| 37 | `childrens_entertainer` | Animación infantil | F Events |
| 38 | `clown_entertainer` | Payaso animador | F Events |
| 39 | `formalwear_rental` | Alquiler de trajes | F Events |
| 40 | `dj_service` | DJ | F Events |

---

### Wave 2 (40) — Core expansion. Low/medium regulation, professional + creative + auto.
*Target: ship across week 2. Requires testimonial + case-study copy.*

#### Creative / portfolio (10)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 41 | `diseno_grafico` | Diseñador gráfico | B Portfolio |
| 42 | `diseno_web` | Diseño web | B Portfolio |
| 43 | `diseno_interiores` | Diseño de interiores | B Portfolio |
| 44 | `branding_agency` | Agencia de branding | B Portfolio |
| 45 | `fotografia_bodas` | Fotografía de bodas | B Portfolio |
| 46 | `fotografia_eventos` | Fotografía de eventos | B Portfolio |
| 47 | `fotografia_producto` | Fotografía de producto | B Portfolio |
| 48 | `drone_aerial_photographer` | Fotografía con drones | B Portfolio |
| 49 | `illustrator_studio` | Ilustrador | B Portfolio |
| 50 | `audiobook_narrator` | Locutor | B Portfolio |

#### Professional services (10)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 51 | `contador` | Contador | D Lead-gen |
| 52 | `cpa_firm` | Estudio contable | D Lead-gen |
| 53 | `auditoria` | Auditoría | D Lead-gen |
| 54 | `despachante` | Despachante de aduana | D Lead-gen |
| 55 | `agencia_aduana` | Agencia aduanera | D Lead-gen |
| 56 | `certified_translator` | Traductor público | B/D |
| 57 | `commercial_appraiser` | Tasador | D Lead-gen |
| 58 | `consultora_rrhh` | Consultora de RRHH | D Lead-gen |
| 59 | `consultora_ti` | Consultora TI | D Lead-gen |
| 60 | `consultora_agro` | Consultora agro | D Lead-gen |

#### Auto (10)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 61 | `general_auto_repair` | Taller mecánico | J Auto |
| 62 | `auto_body_shop` | Chapa y pintura | J Auto |
| 63 | `auto_detailing_shop` / `detailing` | Detailing | J Auto |
| 64 | `gomeria` | Gomería | J Auto |
| 65 | `car_audio_shop` | Audio para autos | J Auto |
| 66 | `brake_specialist` | Especialista en frenos | J Auto |
| 67 | `collision_repair_center` | Centro de colisiones | J Auto |
| 68 | `glass_windshield_repair` | Parabrisas y cristales | J Auto |
| 69 | `automotive_locksmith` | Cerrajería automotriz | J Auto |
| 70 | `grua_remolque` | Grúa y remolque | H/J |

#### Education (10)
| # | Slug | Spanish label | Cluster |
|---|---|---|---|
| 71 | `apoyo_escolar` | Apoyo escolar | G Education |
| 72 | `english_academy` / `instituto_ingles` | Academia de inglés | G Education |
| 73 | `academia_idiomas` | Academia de idiomas | G Education |
| 74 | `academia_cocina` | Academia de cocina | G Education |
| 75 | `escuela_musica` | Escuela de música | G Education |
| 76 | `escuela_conducir` | Autoescuela | G Education |
| 77 | `coding_bootcamp` | Bootcamp de programación | G Education |
| 78 | `digital_marketing_academy` | Marketing digital | G Education |
| 79 | `artes_marciales` | Artes marciales | G Education |
| 80 | `guitar_lessons` | Clases de guitarra | G Education |

---

### Wave 3 (30) — Regulated / higher-ACV. Needs compliance pages + richer content.
*Target: week 3–4. Each requires compliance template + more careful copy.*

#### Health (10) — needs MSP / DINAVISA / INAN compliance
| # | Slug | Spanish label | Regulator |
|---|---|---|---|
| 81 | `consultorio_odontologico` | Consultorio odontológico | MSP |
| 82 | `dermatology_clinic` / `dermatologia` | Dermatología | MSP |
| 83 | `gynecology_clinic` / `ginecologia` | Ginecología | MSP |
| 84 | `geriatria` | Geriatría | MSP |
| 85 | `chiropractic_clinic` | Quiropraxia | MSP |
| 86 | `ent_clinic` | Otorrinolaringología | MSP |
| 87 | `family_medicine_clinic` | Medicina familiar | MSP |
| 88 | `acupuncture_clinic` | Acupuntura | MSP |
| 89 | `fonoaudiologia` | Fonoaudiología | MSP |
| 90 | `farmacia` | Farmacia | DINAVISA |

#### Legal & finance (6) — needs bar/regulator compliance
| # | Slug | Spanish label | Regulator |
|---|---|---|---|
| 91 | `corporate_business_lawyer` | Abogado corporativo | Colegio de Abogados |
| 92 | `family_divorce_lawyer` | Abogado de familia | Colegio de Abogados |
| 93 | `criminal_defense_lawyer` | Abogado penalista | Colegio de Abogados |
| 94 | `immigration_lawyer` | Abogado migratorio | Colegio + DGM |
| 95 | `broker_seguros` | Corredor de seguros | Superintendencia de Seguros |
| 96 | `financial_planner` / `asesor_financiero` | Asesor financiero | BCP/SEPRELAD |

#### Real estate (3)
| # | Slug | Spanish label | Regulator |
|---|---|---|---|
| 97 | `inmobiliaria` | Inmobiliaria | CAVIALPA |
| 98 | `corredor_inmobiliario` | Corredor inmobiliario | CAVIALPA |
| 99 | `desarrollador_inmobiliario` | Desarrollador inmobiliario | MOPC |

#### Hospitality (5)
| # | Slug | Spanish label | Regulator |
|---|---|---|---|
| 100 | `hotel` | Hotel | SENATUR |
| 101 | `hotel_boutique` / `boutique_hotel` | Hotel boutique | SENATUR |
| 102 | `hostal` | Hostal | SENATUR |
| 103 | `alquiler_temporario` | Alquiler temporario | SENATUR |
| 104 | `agencia_viajes` | Agencia de viajes | SENATUR |

#### Food service — retail (6) — needs INAN compliance
| # | Slug | Spanish label | Regulator |
|---|---|---|---|
| 105 | `heladeria` | Heladería | INAN |
| 106 | `cafe_bistro` | Café / bistró | INAN |
| 107 | `artisan_bakery` | Panadería artesanal | INAN |
| 108 | `hamburgueseria` | Hamburguesería | INAN |
| 109 | `drop_off_caterer` / `full_service_caterer` | Catering empresarial | INAN |
| 110 | `food_truck` | Food truck | INAN |

---

## 4. Per-demo content specification

Each `sites/demo-<rubro>/` gets:

```
sites/demo-<rubro>/
├── site.json                # vertical, businessType, country=Paraguay, locale=es, fake contact
├── tokens.json              # pull from src/tokens/<vertical>.tokens.json (no override)
├── pages/
│   ├── home.json            # hero + 4-6 section stack from registry's default composition
│   ├── servicios.json       # or equivalent for non-service rubros
│   └── contacto.json        # address (fake Asunción), WhatsApp, form
└── content/
    └── es.json              # copy overrides on top of src/content/<vertical>.content.json
```

**Site.json contract** (generated):
```json
{
  "vertical": "<from registry>",
  "businessType": "<rubro slug>",
  "country": "Paraguay",
  "domain": "demo.paragu-ai.com",
  "defaultLocale": "es",
  "locales": ["es"],
  "contact": {
    "whatsapp": "+595981000<XXX>",
    "email": "demo-<rubro>@paragu-ai.com",
    "instagram": "@demo.<rubro>.py"
  },
  "location": {
    "city": "<rotating: Asunción, Lambaré, San Lorenzo, Luque, Fernando de la Mora, Capiatá>",
    "neighborhood": "<realistic per city>"
  },
  "integrations": {
    "crm": "hubspot",
    "email": "mailchimp",
    "analytics": "ga4"
  },
  "features": { /* inherited from registry */ },
  "demo": true,
  "createdAt": "2026-04-21"
}
```

The `"demo": true` flag lets the admin dashboard filter them out of real-tenant metrics, and `robots.ts` can noindex them if desired.

---

## 5. Content generation strategy

Three content tiers, chosen by rubro complexity:

| Tier | Approach | Rubros | Effort |
|---|---|---|---|
| **Generated** | Copy `src/content/<vertical>.content.json` → substitute `{{placeholders}}` with generic PY-realistic values | Wave 1 (40) | ~2 min/rubro via script |
| **Augmented** | Start from template, then GPT-generate 1 paragraph of rubro-specific flavor + 3 service items | Wave 2 (40) | ~10 min/rubro, batch-able |
| **Curated** | Manual pass: compliance language, regulator mention, price anchors in guaraníes, FAQ | Wave 3 (30) | ~30 min/rubro |

**Realistic PY defaults to substitute:**
- Business name pattern: `Demo <Rubro> Asunción`
- Phone: `+595 981 000 XXX` (Personal prefix — widely recognized)
- City rotation: Asunción (40%), Gran Asunción metro (40%), Ciudad del Este / Encarnación (20%)
- Prices in PYG (guaraníes), not USD — consult cluster C pricing norms
- Hours: "Lun a Vie 8:00–18:00, Sáb 8:00–13:00"
- WhatsApp CTA as the dominant contact action

**Image strategy:**
- Pull from `sites/shared-images/` first
- For gaps: generate via builder's existing `generate-images.js` script (Gemini pipeline is wired)
- Each demo needs: 1 hero, 3–6 gallery, 1 team/about, 1 location/map-overlay
- Keep images tagged by cluster in `shared-images/clusters/<cluster>/` so they're reusable

---

## 6. Execution pipeline

Proposed order of work:

### Step 1 — Close the 2 P1 registry gaps (30 min)
Add `laundry_dry_cleaning.type.json` and `ambulance_service.type.json` using `web/scripts/create-type.ts`. Neither is in the initial 110 but both block Wave 3.5 follow-ups.

### Step 2 — Build a `scripts/batch-create-demos.ts` (2–3 h)
Iterates over a roster JSON (below), calls `new-tenant.ts` + `generate-site.ts` for each entry. Commits one `sites/demo-<rubro>/` directory per rubro.

Roster file (`paragu-ai-builder/sites/_demo-roster.json`):
```json
{
  "version": "1.0.0",
  "country": "Paraguay",
  "wave": 1,
  "rubros": [
    { "slug": "demo-peluqueria", "rubro": "peluqueria", "vertical": "beauty-personal-care", "city": "Asuncion" },
    { "slug": "demo-barberia", "rubro": "barberia", "vertical": "beauty-personal-care", "city": "Lambare" },
    ...
  ]
}
```

### Step 3 — Run Wave 1 (1 day)
Batch-create 40 demos. Manually spot-check 5. Commit in one PR per cluster (4 PRs).

### Step 4 — Image population (1 day, parallelizable)
Run `generate-images.js` for any missing assets. Cluster-share where possible.

### Step 5 — Link from `/p/<rubro>` marketing pages (0.5 day)
For each existing `/p/<rubro>`, add a "Ver demo en vivo" CTA pointing to `/s/es/demo-<rubro>/`.

### Step 6 — Waves 2 + 3 (week 2–3)
Same pipeline. Wave 3 requires compliance page review via `legal-review-gate.ts`.

### Step 7 — QA pass (1 day)
- `web/scripts/a11y-audit.ts` on 10 random demos
- Lighthouse CI via existing `lighthouserc.json`
- `audit-duplicates.ts` to verify no demo content collides with real tenant
- Visual smoke via Playwright (existing setup)

**Total effort:** 6–8 working days with one engineer + part-time copy/image review.

---

## 7. Success metrics

A demo is "ready to pitch" if:

- [ ] Resolves at `/s/es/demo-<rubro>/` with 200 + correct HTML
- [ ] Hero + at least 4 sections render, no missing-image holes
- [ ] WhatsApp float button works with placeholder number
- [ ] All copy is Spanish, PY-flavored (no generic "123 Main St")
- [ ] Regulated rubros (Wave 3) carry a compliance snippet in the footer
- [ ] Lighthouse ≥85 on mobile (builder default budget)
- [ ] `demo: true` flag set so admin metrics exclude it

---

## 8. Deliverable checklist for the builder team

1. [ ] **Roster JSON** — `paragu-ai-builder/sites/_demo-roster.json` with all 110 entries, waves, and clusters.
2. [ ] **Batch script** — `scripts/batch-create-demos.ts` that consumes the roster.
3. [ ] **110 `sites/demo-*/` directories** committed, grouped into cluster-PRs.
4. [ ] **Marketing cross-links** — each `/p/<rubro>` page adds a demo CTA.
5. [ ] **Admin exclusion** — `demo: true` honored by `/admin/tiles` and `/admin/leads`.
6. [ ] **Noindex flag** — `robots.ts` excludes `/s/es/demo-*/` OR includes depending on SEO decision.
7. [ ] **Compliance gating** — Wave 3 demos ship with country-rubro compliance page.
8. [ ] **Back-population of taxonomy doc** — once demos exist, update `PARAGUAY_RUBROS_TAXONOMY.md` to mark demo status per rubro.

---

## 9. Rubros intentionally NOT in the 110

- **18 "Otros" catch-alls** from ClasiPar (directory IDs 26, 38, 44, 62, 66, 81, 86, 91, 96, 109, 116, 124, 135, 141, 153, 160, 168) — placeholder entries.
- **17 P1–P5 registry gaps** from `PARAGUAY_RUBROS_TAXONOMY.md §4` — need new `type.json` files first.
- **Sub-type clones** — e.g. `hair_color_studio`, `blow_dry_bar`, `braiding_salon` all render similarly to `peluqueria`. Roll into a single demo, not three.
- **Niche health specialties** — `bioidentical_hormone_clinic`, `coolsculpting_studio`, etc. Low PY volume, high regulatory cost.
- **Cross-border / international-only** — `international_household_mover`, `international_relocation` (these are live as real tenants Nexa Paraguay/Uruguay — no demo needed).
- **Death-care vertical** — culturally variant, skip for initial batch.

These can be added as "Wave 4" expansion (target: +30 after the 110 are proven).

---

## 10. Decisions — locked

1. **Route pattern:** `/demo/<rubro>` (singular `demo`, path-based — not subdomain). Shared auth + analytics with the rest of paragu-ai.com. Implementation: new `web/app/demo/[rubro]/page.tsx` that resolves to `sites/demo-<rubro>/` via the existing site loader.
2. **SEO: noindex on all demos**, all 3 waves. Add `<meta name="robots" content="noindex,nofollow">` via the page's `generateMetadata` and include `/demo/*` in `robots.ts`. Demos are sales artifacts, not SEO assets — the `/p/<rubro>` marketing pages carry the SEO weight and link into the demos.
3. **Contact forms → AI Whisperers sales inbox.** Every demo's form and WhatsApp float routes to our capture pipeline (`/api/leads` with `source: "demo"` and `demoRubro: "<rubro>"`). Demo visitors are leads; treat them as such. Existing leads-digest cron (PR #70) surfaces them in `/admin/demo-requests`.
4. **Promotion trigger: 50 generated tenants in that rubro.** When a rubro accumulates 50 live tenants (real + demo combined), the demo for that rubro gets promoted via `migrate-demo-to-site.ts` to become the canonical showcase for the rubro. Rationale: 50 tenants = proven market fit for that rubro; the demo becomes a reference implementation worth indexing. At promotion time: (a) flip `demo: false`, (b) remove the noindex, (c) wire real contact info if available, (d) move it out of `/demo/<rubro>` into its own slug. Track the counter in `/admin/tiles`.

---

## 11. Status (executed)

- **PR [#85](https://github.com/Ai-Whisperers/paragu-ai-builder/pull/85)** — merged 2026-04-21 — Wave 1 (40) + Wave 2 (40) + Wave 3 (30) = 110/110 demo tenants + `/demo/[rubro]` route + P1 gaps (2 type.json) + `sites/_demo-roster.json` + `web/scripts/batch-create-demos.ts`.
- **PR [#88](https://github.com/Ai-Whisperers/paragu-ai-builder/pull/88)** — merged 2026-04-21 — 15 P2-P5 registry gaps closed; `/p/[rubro]` falls back to `/demo/<rubro>` when no curated demo exists.

All 4 locked decisions in §10 are implemented. Validation: 115/115 sites OK.

**Not yet done:**
- 72 country×cluster compliance templates (blocks Wave 3 promotion)
- Admin filters on `demo: true` / `demoWave` in `/admin/tiles` + `/admin/leads`
- Replace the `SALES_WHATSAPP` placeholder in `web/scripts/batch-create-demos.ts` with the real AI Whisperers sales line before pitch use

---

*Document created: April 2026 · Companion to `PARAGUAY_RUBROS_TAXONOMY.md` and `LATAM_RUBROS_LANDSCAPE.md` · Owner: AI Whisperers team · Status: executed (110/110 demos live).*
