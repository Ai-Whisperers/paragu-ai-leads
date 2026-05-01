# Builder Integration - Extraction Map
## How Leads Repo Content Maps to the Builder Template System

This document maps every piece of content in the leads repo to its
structured equivalent in `paragu-ai-builder`.

---

## Source -> Destination Mapping

### Design Tokens (Visual Identity)
| Leads Repo Source | Builder Destination | Status |
|---|---|---|
| `TEMPLATE_SPECIFICATIONS.md` Section 1.1 (Peluqueria colors) | `src/tokens/peluqueria.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 2.1 (Gimnasio colors) | `src/tokens/gimnasio.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 3.1 (Spa colors) | `src/tokens/spa.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 4.1 (Unas colors) | `src/tokens/unas.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 5.1 (Tatuajes colors) | `src/tokens/tatuajes.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 6.1 (Barberia colors) | `src/tokens/barberia.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 7.1 (Estetica colors) | `src/tokens/estetica.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 8.1 (Maquillaje colors) | `src/tokens/maquillaje.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` Section 9.1 (Depilacion colors) | `src/tokens/depilacion.tokens.json` | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` (shared spacing, breakpoints) | `src/tokens/base.tokens.json` | Extracted |

### Page Composition (Section Layout)
| Leads Repo Source | Builder Destination | Status |
|---|---|---|
| `WIREFRAME_CONCEPTS.md` (all 9 layouts) | `src/registry/*.type.json` (pages + sections) | Extracted |
| `TEMPLATE_SPECIFICATIONS.md` (component library) | `src/registry/*.type.json` (features) | Extracted |
| `BUSINESS_TYPE_REQUIREMENTS.md` (feature matrix) | `src/registry/*.type.json` (features) | Extracted |

### Content Templates (Spanish Copy)
| Leads Repo Source | Builder Destination | Status |
|---|---|---|
| `CONTENT_TEMPLATES.md` Section 1 (Peluqueria) | `src/content/peluqueria.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 2 (Gimnasio) | `src/content/gimnasio.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 3 (Spa) | `src/content/spa.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 4 (Unas) | `src/content/unas.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 5 (Tatuajes) | `src/content/tatuajes.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 6 (Barberia) | `src/content/barberia.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 7 (Estetica) | `src/content/estetica.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 8 (Maquillaje) | `src/content/maquillaje.content.json` | Extracted |
| `CONTENT_TEMPLATES.md` Section 9 (Depilacion) | `src/content/depilacion.content.json` | Extracted |

### Business Input Schemas (Data Collection)
| Leads Repo Source | Builder Destination | Status |
|---|---|---|
| `BUSINESS_INPUT_FORM.md` (universal fields) | `src/schemas/base-business.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Hair Salon form) | `src/schemas/peluqueria.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Gym form) | `src/schemas/gimnasio.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Spa form) | `src/schemas/spa.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Nail form) | `src/schemas/unas.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Tattoo form) | `src/schemas/tatuajes.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Barber form) | `src/schemas/barberia.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Aesthetic form) | `src/schemas/estetica.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Makeup form) | `src/schemas/maquillaje.schema.json` | Extracted |
| `BUSINESS_INPUT_FORM.md` (Hair Removal form) | `src/schemas/depilacion.schema.json` | Extracted |

### SEO & Technical Config
| Leads Repo Source | Builder Destination | Status |
|---|---|---|
| `TECHNICAL_IMPLEMENTATION.md` (SEO templates) | `src/registry/*.type.json` (seo section) | Extracted |
| `TECHNICAL_IMPLEMENTATION.md` (performance targets) | `src/tokens/base.tokens.json` (performance) | Extracted |
| `TECHNICAL_IMPLEMENTATION.md` (accessibility) | `src/tokens/base.tokens.json` (accessibility) | Extracted |
| `TECHNICAL_IMPLEMENTATION.md` (image specs) | `src/tokens/base.tokens.json` (images) | Extracted |
| `BUSINESS_TYPE_REQUIREMENTS.md` (booking config) | `src/registry/*.type.json` (features.onlineBooking) | Extracted |

### Custom Client Pages (One-off)

These are bespoke single-client pages that live outside the 9-vertical
template system. The builder consumes the structured `page-spec.json` to
render the page at the matching slug.

| Leads Repo Source | Builder Destination | Status |
|---|---|---|
| `docs/07_clients/dayah-litworks/page-spec.json` | route `/dayah-litworks` | Drafted |
| `docs/07_clients/dayah-litworks/CONTENT.md` | (reference copy, source of truth) | Drafted |

---

## Lead Data -> Builder Pipeline (Future)

The CSV data in `data/processed/` can feed the builder:

```
paraguay_priority_a.csv
  |
  +--> Extract: name, phone, address, city, types, rating
  |
  +--> Map to: base-business.schema.json
  |
  +--> Auto-populate: content templates with real data
  |
  +--> Generate: preview website for sales pitch
```

### Fields Available from Lead Data
| CSV Column | Builder Schema Field |
|---|---|
| `name` | `businessName` |
| `phone` | `contact.phone` |
| `international_phone` | `contact.whatsapp` |
| `address` | `location.address` |
| `city` | `location.city` |
| `neighborhood` | `location.neighborhood` |
| `lat`, `lng` | `location.coordinates` |
| `google_maps_url` | `location.googleMapsUrl` |
| `website` | `seo.existingWebsite` |
| `rating` | (social proof display) |
| `total_reviews` | (social proof display) |
| `primary_type` | `businessType` (mapped via vertical) |
| `saturday_hours`, `sunday_hours` | `hours` |

---

*Extraction map created: April 2026*
