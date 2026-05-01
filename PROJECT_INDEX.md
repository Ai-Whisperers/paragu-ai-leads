# 📁 Project Structure Index

## Root Directory
```
paraguay-beauty-data/
├── README.md              # Project overview
├── requirements.txt       # Python dependencies
├── .git/                  # Git repository
├── data/                  # Data files
├── docs/                  # Documentation
├── scripts/               # Python scripts
├── src/                   # Source code
└── templates/             # Website templates
```

---

## 📂 Data Directory (`/data/`)

### Processed (Final Data)
| File | Description |
|------|-------------|
| `paraguay_beauty_prioritized.csv` | All 7,463 businesses with priority scoring |
| `paraguay_priority_a.csv` | 3,960 Priority A leads (highest potential) |
| `paraguay_priority_b.csv` | Priority B leads |
| `deep_analysis_summary.json` | Category analysis summary |
| `business_requirements_analysis.json` | Requirements by category |

### Raw (Source Data)
- Empty (intermediate files cleaned up)

---

## 📂 Docs Directory (`/docs/`)

### 01_market_research/ - Market Analysis
| File | Description |
|------|-------------|
| `ANALYSIS.md` | Full market analysis (7,463 businesses) |
| `MARKET_ANALYSIS_SUMMARY.md` | Executive summary |
| `MARKET_DEEP_RESEARCH.md` | Extended market research |
| `BUSINESS_TYPES_ANALYSIS.md` | 4-layer taxonomy audit (Google Places → verticals → beauty categories) |
| `PARAGUAY_RUBROS_TAXONOMY.md` | Paraguayan SME-directory rubros (18 optgroups, 144 options) mapped to builder vertical + type |
| `LATAM_RUBROS_LANDSCAPE.md` | Cross-LATAM classification (PY/AR/UY/CL/CO/PE/MX/BR) — statistical + regulatory + commercial layers, website-need clusters, expansion priority |
| `FEATURE_ROADMAP.md` | First-world competitor analysis |

### 02_requirements/ - Business Requirements
| File | Description |
|------|-------------|
| `BUSINESS_REQUIREMENTS.md` | Requirements by category |
| `BUSINESS_TYPE_REQUIREMENTS.md` | Complete requirements for all 9 types |

### 03_templates/ - Design & Content
| File | Description |
|------|-------------|
| `TEMPLATE_SPECIFICATIONS.md` | Design specs (colors, typography) per category |
| `WIREFRAME_CONCEPTS.md` | Visual layout wireframes |
| `CONTENT_TEMPLATES.md` | Pre-written content for all pages |
| `BUSINESS_INPUT_FORM.md` | Data collection form template |

### 04_technical/ - Implementation
| File | Description |
|------|-------------|
| `IMPLEMENTATION_PLAN.md` | Development roadmap |
| `TECHNICAL_IMPLEMENTATION.md` | Tech stack, deployment, SEO |

### 05_strategy/ - Business Strategy
| File | Description |
|------|-------------|
| `PRICING_STRATEGY.md` | Revenue models and pricing |
| `DEMO_ROSTER_100_RUBROS.md` | 110 Paraguayan rubros chosen for first demo wave, sequenced in 3 waves with execution pipeline |
| `DOCUMENTATION_INDEX.md` | Complete documentation index |

---

## 📂 Scripts Directory (`/scripts/`)

### Data Processing Scripts
| File | Purpose |
|------|---------|
| `scrape_nationwide.py` | Main scraper for nationwide data |
| `deep_analysis.py` | Category analysis |
| `merge_nationwide.py` | Merge data files |

*Note: Multiple versions exist (scrape_beauty_v1-v2, etc.) - these are development iterations*

---

## 📂 Src Directory (`/src/`)

### Core Library
| File | Purpose |
|------|---------|
| `api_client.py` | Google Places API client |
| `scraper.py` | Web scraper |
| `analyzer.py` | Business analysis/scoring |
| `exporter.py` | CSV/Excel export |
| `models.py` | Data models |
| `config.py` | Configuration |
| `main.py` | Main entry point |

---

## 📊 Data Summary

### Key Metrics
- **Total businesses**: 7,463
- **Priority A leads**: 3,960
- **No website**: 75%
- **Categories**: 9 main business types

### Priority A Criteria
- No existing website
- Has phone number
- Has reviews (social proof)
- Category is in target list

---

## 🚀 Quick Start

### View Priority Leads
```bash
head -20 data/processed/paraguay_priority_a.csv
```

### View All Businesses
```bash
head -20 data/processed/paraguay_beauty_prioritized.csv
```

### Run Analysis
```bash
python -m src.main
```

---

## 📋 Next Steps

1. **Build MVP Template** - Start with Peluquería (highest volume)
2. **Set up booking integration** - Fresha + WhatsApp
3. **Create lead outreach** - Contact Priority A businesses
4. **Deploy first websites** - Launch minimum viable product

---

*Last Updated: April 2026*