# MASTER AUDIT: Ai-Whisperers Client Lead Sites

## Generated: 2026-05-01
## Auditor: Sunstein (Hermes Agent)

---

## TABLE OF CONTENTS

1. [EXECUTIVE SUMMARY](#1-executive-summary)
2. [ALL REPOS COMPARISON TABLE](#2-all-repos-comparison-table)
3. [CRITIQUE PER SITE](#3-critique-per-site)
4. [COMPARISON WITH ESTABLISHED SITES](#4-comparison-with-established-sites)
5. [TEMPLATE vs AUTO-GENERATED: THE GAP](#5-template-vs-auto-generated-the-gap)
6. [ARCHITECTURE & INFRASTRUCTURE](#6-architecture--infrastructure)
7. [PER-REPO TODO MASTER LIST](#7-per-repo-todo-master-list)
8. [EFFORT ESTIMATES](#8-effort-estimates)

---

## 1. EXECUTIVE SUMMARY

### Scoring (0-100)

| Site | Score | Status |
|------|-------|--------|
| superspuma | 92 | REFERENCE - established |
| nexa | 85 | REFERENCE - established |
| fun4me | 70 | REFERENCE - established |
| cocodrilo-fitness | 48 | AUTO-GENERATED - needs work |
| luis-de-leon-concept | 47 | AUTO-GENERATED - needs work |
| bichos-gym | 48 | AUTO-GENERATED - needs work |
| mantra-spa | 47 | AUTO-GENERATED - needs work |
| magnolia-peluqueria | 47 | AUTO-GENERATED - needs work |

### What's Working (After Recent Fixes)

- All 5 sites return 200 on all 35 pages
- Render-blocking fonts fixed (next/font/google)
- CSS custom properties design system in place
- Business-specific SVG logos generated
- CTA banner added before footer
- Unique copy per site (services, taglines)
- Proper footer with legal links
- Schema.org JSON-LD structured data
- Open Graph + Twitter meta tags
- robots.txt + sitemap.xml
- Security headers (HSTS, XFO, nosniff)
- Docker healthchecks + non-root user
- Resource limits in Docker compose
- traefik.docker.network label present
- HOSTNAME=0.0.0.0 in Dockerfile

### What's Still Missing vs Established Sites

- **No images at all** (hero photos, service photos, team photos)
- No cookie consent banner
- No blog / articles
- No testimonials section
- No trust badges
- No real business phone numbers (placeholders)
- No Google Maps integration
- No social media links
- No dark mode
- No loading states / skeletons
- No PWA / manifest / service worker
- No analytics
- No newsletter signup
- No e-commerce / booking integration
- No search functionality
- No localization (Spanish only — OK for PY clients but no English fallback)
- No CTA variants (all sites use same "Contactar por WhatsApp" CTA)

---

## 2. ALL REPOS COMPARISON TABLE

### Repo-Level Comparison

| Feature | superspuma | nexa | fun4me | cocodrilo | luis | bichos | mantra | magnolia |
|---------|-----------|------|--------|-----------|------|--------|--------|----------|
| Pages | 14 | 7 | 4+ | 10 | 10 | 10 | 10 | 10 |
| Images | 26 | 13 | 0+ | 0 | 0 | 0 | 0 | 0 |
| Blog | Yes | No | No | No | No | No | No | No |
| E-commerce | Yes | No | Yes | No | No | No | No | No |
| Cookie consent | Yes | No | No | No | No | No | No | No |
| JSON-LD | Yes | No | No | Yes | Yes | Yes | Yes | Yes |
| OG meta | Full | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Logo SVG | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Hero image | Yes | Yes | No | No | No | No | No | No |
| CTA banner | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| Testimonials | Yes | Yes | No | No | No | No | No | No |
| Map | No | No | No | No | No | No | No | No |
| Dark mode | No | No | No | No | No | No | No | No |
| Search | No | No | No | No | No | No | No | No |
| PWA | No | No | No | No | No | No | No | No |
| Analytics | No | No | No | No | No | No | No | No |

### Code Quality Comparison

| Metric | superspuma | auto-gen (avg) |
|--------|-----------|----------------|
| TypeScript strict | Partial | No |
| ESLint | Yes | Yes (basic) |
| Components | 22+ | 7 |
| Custom hooks | Yes (4) | No |
| Lib utilities | Yes (format, wa, hooks) | No |
| Content directory | Yes (es.json, tokens.json) | Yes (basic site.json) |
| Unit tests | No | No |
| CI/CD | No | No |
| package.json scripts | dev, build, start, lint | dev, build, start, lint |
| Dependencies | clsx, lucide, tailwind-merge, next 15 | lucide, next 16 |

---

## 3. CRITIQUE PER SITE

### cocodrilo-fitness.paragu-ai.com

**SCORE: 48/100**

```
WEAKNESSES:
────────────
┌─ HERO ───────────────────────────────────────────────┐
│ ✓ Gradient background with dot pattern               │
│ ✓ Crisp heading with subtitle                        │
│ ✓ WhatsApp CTA button                                │
│ ✗ NO HERO IMAGE — Just a gradient, looks empty       │
│ ✗ No gym equipment photos, no facility showcase      │
│ ✗ Generic "Reservar" — doesn't say WHAT you book     │
└──────────────────────────────────────────────────────┘

┌─ SERVICES ───────────────────────────────────────────┐
│ ✓ 3 categories (Membresías, Clases, Instalaciones)   │
│ ✓ Real prices in Gs.                                 │
│ ✓ Proper grid layout                                 │
│ ✗ NO ICON per category — all use dumbbell icon       │
│ ✗ Category names not showing (JSX bug in services)   │
│ ✗ No "más info" or expand details                    │
└──────────────────────────────────────────────────────┘

┌─ DESIGN ─────────────────────────────────────────────┐
│ ✓ Clean Tailwind styling                             │
│ ✓ Responsive (sm/md/lg breakpoints)                  │
│ ✓ Consistent colors                                  │
│ ✗ Very flat — no shadows, no depth, no personality   │
│ ✗ White cards on white background — low contrast     │
│ ✗ No animations or hover effects on cards            │
│ ✗ Looks like a template (because it is one)          │
└──────────────────────────────────────────────────────┘
```

### luis-de-leon-concept.paragu-ai.com

**SCORE: 47/100**

```
WEAKNESSES:
────────────
┌─ HERO ───────────────────────────────────────────────┐
│ ✓ Same gradient + dot pattern                        │
│ ✗ Hair salon with NO hair photos? Unforgivable       │
│ ✗ No before/after transformations                   │
│ ✗ No stylist portraits → zero trust                 │
└──────────────────────────────────────────────────────┘

┌─ SERVICES ───────────────────────────────────────────┐
│ ✓ Cortes, Coloración, Tratamientos categories        │
│ ✓ Realistic prices (80k-350k Gs.)                    │
│ ✗ Same icon bug — category names not rendering       │
│ ✗ No stylist names or bios                          │
│ ✗ No mention of brands used (L'Oréal, Wella, etc.)  │
└──────────────────────────────────────────────────────┘

┌─ FOOTER ─────────────────────────────────────────────┐
│ ✓ Legal pages linked                                 │
│ ✓ Business hours                                     │
│ ✗ Fake phone number (0981 000 000)                   │
│ ✗ No address beyond "Asunción" — too vague           │
└──────────────────────────────────────────────────────┘
```

### bichos-gym.paragu-ai.com

**SCORE: 48/100**

```
WEAKNESSES:
────────────
┌─ HERO ───────────────────────────────────────────────┐
│ ✓ "Dale fuerte, transformá tu cuerpo" tagline        │
│ ✗ Gym without a single fitness photo? Criminal       │
│ ✗ No equipment shown, no space shown                │
└──────────────────────────────────────────────────────┘

┌─ SERVICES ───────────────────────────────────────────┘
│ ✓ 3 categories with real prices                      │
│ ✓ CrossFit class included                            │
│ ✓ Nutrition consultation available                   │
│ ✗ Category names not showing                         │
│ ✗ No trainer profiles                                │
│ ✗ No class schedule                                  │
└──────────────────────────────────────────────────────┘

NOTE: This has the best price structure of all 5 sites.
```

### mantra-spa.paragu-ai.com

**SCORE: 47/100**

```
WEAKNESSES:
────────────
┌─ HERO ───────────────────────────────────────────────┐
│ ✓ "Renová tu cuerpo y mente" — good tagline         │
│ ✗ A SPA with no spa ambiance photos? Major fail      │
│ ✗ No massage room, no treatment room shown          │
└──────────────────────────────────────────────────────┘

┌─ SERVICES ───────────────────────────────────────────┘
│ ✓ Best services section: Masajes, Facial, Corporales │
│ ✓ Most specific pricing and durations                │
│ ✓ "Paquete Bienestar" — good upsell                  │
│ ✗ Category names not showing                         │
│ ✗ No treatment descriptions beyond 1 line            │
│ ✗ No "beneficios" per treatment                     │
└──────────────────────────────────────────────────────┘

NOTE: Best service variety and pricing detail. Most potential.
```

### magnolia-peluqueria.paragu-ai.com

**SCORE: 47/100**

```
WEAKNESSES:
────────────
┌─ HERO ───────────────────────────────────────────────┐
│ ✓ "Realzá tu belleza natural" — brand-appropriate   │
│ ✗ Hair salon with zero hair photos                  │
│ ✗ No salon interior photos                          │
└──────────────────────────────────────────────────────┘

┌─ SERVICES ───────────────────────────────────────────┘
│ ✓ Keratina, Botox Capilar — unique service menu     │
│ ✓ Competitive pricing                                │
│ ✗ Category names not showing                         │
│ ✗ No stylist specialization info                    │
└──────────────────────────────────────────────────────┘
```

---

## 4. COMPARISON WITH ESTABLISHED SITES

### superspuma (REFERENCE: 92/100)

What makes it professional:
1. **14 pages** — blog with articles, product pages, FAQ, about, store, guarantees, guides
2. **26 images** — hero photo (unsplash), product photos, category icons, brand logos
3. **img caching** — Cache-Control: immutable for /superspuma/(.*)
4. **Cookie consent** — GDPR-compliant banner
5. **Schema.org** — Store JSON-LD with full address, founding date, social links
6. **Font loading** — next/font with CSS variables, zero CLS
7. **CSS custom properties** — 15+ variables, dark-mode ready
8. **22+ reusable components** in lib/client-kit
9. **Trust badges** — "13 puntos en todo el país", "Garantía de fábrica"
10. **Secondary navigation** — mobile CTAs, bottom nav
11. **Recently viewed** + wishlist hooks
12. **CTA Banner** — gradient with WhatsApp CTA
13. **Business address** — real Villeta, Central location
14. **Founding date** — since 1976, brand authority
15. **Product cards** — hover effects, star ratings, descriptions

### nexa (REFERENCE: 85/100)

What works:
1. **7 pages** — programs, about, FAQ, blog
2. **13 images** — program illustrations, team photos
3. **Card layouts** — shadow-md, hover effects
4. **Process section** — step-by-step with icons
5. **Testimonials** — social proof
6. **Responsive** — thorough sm/md/lg breakpoints
7. **Color system** — custom CSS variables
8. **Clean typography** — font-heading via next/font

### fun4me (REFERENCE: 70/100)

What works:
1. **Simplicity** — focused single-purpose page
2. **next/font** optimization
3. **Custom CSS** via postcss

---

## 5. TEMPLATE vs AUTO-GENERATED: THE GAP

template-nextjs-client has but auto-gen sites DON'T:

```
MISSING FROM AUTO-GEN SITES:
─────────────────────────────
📄 Pages:
  □ /blog/[slug]          □ /tienda
  □ /blog                 □ /producto/[slug]
  □ /envio                □ /promociones
  □ /rss.xml              □ /api/subscribe
  □ /faq (we added this)  □ /not-found (we added)
  □ /nosotros (we added)  □ /privacidad (we added)
  □ /terminos (we added)

🧩 Components:
  □ analytics.tsx          □ cookie-consent.tsx
  □ dark-mode-toggle.tsx   □ empty-state.tsx
  □ hero-carousel.tsx      □ loading-bar.tsx
  □ payment-methods.tsx    □ product-card.tsx
  □ quick-order.tsx        □ recently-viewed.tsx
  □ safe-image.tsx         □ search-autocomplete.tsx
  □ share-whatsapp.tsx     □ skeleton.tsx
  □ toast.tsx              □ bottom-nav.tsx
  □ json-ld.tsx            □ breadcrumb-jsonld.tsx
  □ article-json-ld.tsx    □ faq-json-ld.tsx

📚 Content:
  □ content/es.json        □ content/tokens.json
  □ public/manifest.json   □ public/sw.js

🛠 Infrastructure:
  □ Healthcheck (we added)
  □ Resource limits (we added)
  □ Non-root user (we added)
  □ .npmrc with registry
```

---

## 6. ARCHITECTURE & INFRASTRUCTURE

### Docker Swarm Setup (All 5)

```
All use: Docker stack deploy with Traefik reverse proxy
Ports:    30023-30027 (random host ports → 3000 container)
Network:  agent-net (external overlay)
Replicas: 2 (HA)
Limits:   512M RAM / 0.5 CPU (we added)
Monitor:  Healthcheck (we added)
User:     nextjs (non-root, we added)
```

### Repository Structure

```
/root/{name}/
├── .git/
├── AGENTS.md
├── CLAUDE.md
├── Dockerfile
├── README.md
├── app/
├── components/
├── content/
├── public/
│   ├── images/
│   │   ├── logo.svg
│   │   └── og-default.jpg
│   └── favicon.svg
├── docker-compose.yml
├── next.config.ts
├── package.json
├── package-lock.json
├── postcss.config.mjs
├── tailwind.config.ts
└── tsconfig.json
```

---

## 7. PER-REPO TODO MASTER LIST

### Category A: INFRASTRUCTURE & DEPLOYMENT (30 items)

```
DOCKER
──────
□ Add docker socket proxy (security)
□ Pin node:20-alpine digest (reproducibility)
□ Add .dockerignore with node_modules
□ Add build args for NEXT_PUBLIC vars
□ Add docker stack deploy script (deploy.sh)
□ Add docker stack rollback script
□ Set up Docker image tag strategy (git SHA)

TRAEFIK
───────
□ Add rate limiting middleware
□ Add IP whitelist for /admin routes
□ Set up access logs
□ Add circuit breaker middleware
□ Add retry middleware
□ Configure custom error pages
□ Add Traefik dashboard (auth-protected)

CI/CD
─────
□ Set up GitHub Actions deploy workflow
□ Add build cache optimization
□ Add automated testing step
□ Add Docker layer caching

MONITORING
──────────
□ Add container memory alerts
□ Add uptime monitoring (UptimeRobot/Checkly)
□ Set up log aggregation (Loki/Grafana)
□ Add healthcheck endpoint

SECURITY
────────
□ Run Trivy scan on images
□ Add Content-Security-Policy header
□ Scan for exposed secrets in .git
□ Add fail2ban for SSH
□ Set up automatic SSL renewal monitoring
```

### Category B: CODE QUALITY (45 items)

```
TYPESCRIPT
──────────
□ Enable strict mode in tsconfig.json
□ Add proper types for all components
□ Add interfaces for service data
□ Add return types to all functions
□ Fix any types
□ Add noUnusedLocals: true
□ Add noUnusedParameters: true

COMPONENTS
──────────
□ Refactor Header — extract NavItems type
□ Refactor Hero — make more configurable
□ Refactor Footer — add dynamic columns
□ Refactor Services — fix category name rendering bug
□ Extract service data to content/site.json
□ Add loading.tsx for Suspense boundaries
□ Add error.tsx (we added, verify working)
□ Add not-found.tsx (we added, verify working)

HOOKS
─────
□ Add useMediaQuery hook
□ Add useScrollPosition hook
□ Add useLocalStorage hook
□ Add useDebounce hook

UTILITIES
─────────
□ Add cn() class merge utility (clsx + tailwind-merge)
□ Add wa() URL builder for WhatsApp
□ Add formatCurrency for Gs.
□ Add formatPhone for display
□ Add slugify utility

TESTING
───────
□ Set up Vitest
□ Add snapshot tests for components
□ Add integration tests for pages
□ Add accessibility tests (axe)
□ Add Lighthouse CI

PERFORMANCE
───────────
□ Add BundleAnalyzer
□ Add image lazy loading
□ Add dynamic imports for heavy components
□ Add prefetch for nav links
□ Add preconnect for external origins
□ Audit bundle size
```

### Category C: DESIGN & UX (60 items)

```
COLOR SYSTEM
────────────
□ Add secondary color variants (light/dark)
□ Add surface-100/200/300 scale
□ Add status colors (info, warning, error, success)
□ Test contrast ratios (WCAG AA)
□ Add color palette documentation

TYPOGRAPHY
──────────
□ Add text-base (16px) default
□ Add line-height scale
□ Add letter-spacing tokens
□ Add font-weight documentation
□ Test readability on mobile

HERO SECTION
────────────
□ Add background image (per business)
□ Add image overlay with gradient
□ Add scroll-down indicator
□ Add fade-in animation
□ Add parallax effect (subtle)
□ Add hero CTA variants (secondary)
□ Add hero trust indicators

SERVICES SECTION
───────────────
□ Fix category name rendering bug (P0)
□ Add category-specific icons
□ Add hover card elevation
□ Add card border on hover (we did this)
□ Add expandable service details
□ Add "book now" per service
□ Add duration visual indicator
□ Add price callout styling

CTA BANNER
──────────
□ Add background pattern
□ Add floating animation
□ Add secondary CTA option
□ Add phone number display
□ Add business hours display

FOOTER
──────
□ Add social media icons
□ Add newsletter signup
□ Add back-to-top button
□ Add dynamic copyright year
□ Add Google Maps iframe
□ Add business registration info

NAVIGATION
──────────
□ Add sticky header with shadow on scroll
□ Add active page indicator
□ Add mobile menu animation
□ Add scroll-to-section links
□ Add logo with tagline

RESPONSIVE
──────────
□ Test on 320px width (small mobile)
□ Test on tablet (768px)
□ Add safe-area-inset for notched devices
□ Fix mobile menu positioning
□ Add touch-friendly target sizes (44px minimum)

ANIMATIONS
──────────
□ Add fade-in on scroll (IntersectionObserver)
□ Add staggered card entrance
□ Add button micro-interactions
□ Add page transitions
□ Add loading skeleton animation

DARK MODE
─────────
□ Add prefers-color-scheme media query
□ Add dark color palette
□ Add toggle component
□ Persist preference in localStorage
□ Add transition for mode switch
```

### Category D: CONTENT & COPY (40 items)

```
PER-SITE CONTENT
────────────────
□ cocodrilo-fitness: Add real class schedule
□ cocodrilo-fitness: Add trainer bios
□ cocodrilo-fitness: Add facility descriptions
□ luis-de-leon-concept: Add stylist profiles
□ luis-de-leon-concept: Add service brand names
□ luis-de-leon-concept: Add before/after gallery
□ bichos-gym: Add trainer certifications
□ bichos-gym: Add equipment list
□ bichos-gym: Add class timetable
□ mantra-spa: Add treatment detail pages
□ mantra-spa: Add therapist certifications
□ mantra-spa: Add product/brand descriptions
□ magnolia-peluqueria: Add portfolio gallery
□ magnolia-peluqueria: Add stylist specialties
□ magnolia-peluqueria: Add product lines used

WEAK COPY TO REPLACE
────────────────────
□ "Estamos para ayudarte" → specific value prop
□ "Contactanos hoy y te responderemos" → time-specific
□ Generic "Contacto" page → booking flow
□ Generic FAQ → specific business questions
□ About page → origin story + team
□ No calls to action beyond WhatsApp

MISSING SECTIONS
────────────────
□ Testimonials/reviews section
□ Before/after gallery
□ Process/how-it-works section
□ Team/staff section
□ FAQ with expandable details
□ Blog/news section
□ Gallery/portfolio
```

### Category E: PAGES & FEATURES (35 items)

```
CORE PAGES
──────────
□ / (we have this)
□ /servicios (we have this)
□ /contacto (we have this)
□ /nosotros (we have this)
□ /faq (we have this)
□ /privacidad (we have this)
□ /terminos (we have this)
□ /galeria (photo gallery)
□ /blog (articles + news)
□ /blog/[slug] (individual article)
□ /equipo (team page)
□ /testimonios (reviews page)
□ /promociones (specials/offers)

FEATURES
────────
□ WhatsApp click-to-chat on every page (we have this)
□ Google Maps embed on contacto
□ Contact form (email)
□ WhatsApp share buttons
□ Print-friendly styles
□ RSS feed
□ Search (static site search)
□ Social media links + metadata
□ Business hours in structured data
```

### Category F: ASSETS & IMAGES (30 items)

```
LOGOS
─────
□ cocodrilo-fitness: ✓ done (SVG dumbbell icon)
□ luis-de-leon-concept: ✓ done (SVG scissors icon)
□ bichos-gym: ✓ done (SVG workout icon)
□ mantra-spa: ✓ done (SVG flower icon)
□ magnolia-peluqueria: ✓ done (SVG flower/scissors)

FAVICONS
────────
□ All 5: ✓ done (SVG favicon)

HERO IMAGES (REAL PHOTOS NEEDED)
────────────────────────────────
□ cocodrilo-fitness: Gym interior, equipment, pool
□ luis-de-leon-concept: Salon interior, haircut in progress
□ bichos-gym: Gym space, training in action
□ mantra-spa: Massage room, candles, ambiance
□ magnolia-peluqueria: Salon, styling station, products

SERVICE PHOTOS
──────────────
□ Each service category needs a photo
□ 3-5 photos per site minimum

ABOUT PHOTOS
────────────
□ Team photo per site
□ Business exterior/interior

OG IMAGES
─────────
□ All 5: ✓ done (basic OG image)
□ Custom per-site OG with real branding needed
```

### Category G: SEO & STRUCTURED DATA (25 items)

```
META TAGS
─────────
□ ✓ Title tags (all 5 done)
□ ✓ Meta descriptions (all 5 done)
□ ✓ Open Graph (all 5 done)
□ ✓ Twitter cards (all 5 done)
□ ✓ Canonical URLs (all 5 done)

STRUCTURED DATA
───────────────
□ ✓ LocalBusiness JSON-LD (all 5 done)
□ Add Service schema per service item
□ Add FAQ schema to FAQ page
□ Add BreadcrumbList schema
□ Add Review schema for testimonials
□ Add OpeningHoursSpecification
□ Add GeoCoordinates
□ Add ImageObject for photos

SITEMAP
───────
□ ✓ sitemap.xml (all 5 done)
□ Add image sitemaps
□ Add video sitemaps (if any)

ROBOTS
──────
□ ✓ robots.txt (all 5 done)
□ Add crawl-delay

HEADINGS
────────
□ Verify h1-h6 hierarchy on all pages
□ Fix contacto page missing h2
□ Add aria-labels to nav elements
□ Add skip-to-content link
```

### Category H: PERFORMANCE (20 items)

```
LOAD TIME
─────────
□ ✓ Fonts via next/font (done)
□ Add image lazy loading
□ Add prefetch critical pages
□ Add DNS prefetch for external domains
□ Eliminate render-blocking resources

CACHING
───────
□ ✓ Static asset caching headers (done)
□ Add service worker for offline
□ Add CDN caching rules
□ Add API response caching

BUNDLE
──────
□ Add code splitting on routes
□ Add dynamic imports for heavy libs
□ Remove unused CSS with PurgeCSS
□ Optimize lucide-react imports (tree-shaking)
□ Audit bundle with @next/bundle-analyzer

CORE WEB VITALS
───────────────
□ Target LCP < 2.5s
□ Target FID < 100ms
□ Target CLS < 0.1
□ Run Lighthouse audit monthly
```

### Category I: ANALYTICS & TRACKING (15 items)

```
ANALYTICS
─────────
□ Add Google Analytics 4 (or alternative)
□ Add privacy-friendly Plausible/Umami
□ Track WhatsApp clicks
□ Track page views per page
□ Track CTA conversions
□ Track form submissions

MONITORING
──────────
□ Set up uptime monitoring
□ Add error tracking (Sentry)
□ Add performance monitoring
□ Set up weekly analytics report

CONVERSION
──────────
□ Set up conversion goals
□ Track WhatsApp chat initiations
□ Track phone number clicks
□ Track form fills
```

### Category J: LEGAL & COMPLIANCE (15 items)

```
PRIVACY
───────
□ ✓ Privacy policy page (all 5 done)
□ Add cookie consent banner
□ Add GDPR compliance notice
□ Add data processing disclosure

TERMS
─────
□ ✓ Terms of service (all 5 done)
□ Add cancellation/refund policy
□ Add service guarantee terms

ACCESSIBILITY
─────────────
□ Add aria-labels to interactive elements
□ Add skip-to-content link
□ Ensure keyboard navigation
□ Test with screen reader (VoiceOver/NVDA)
□ Add focus-visible styles
□ Ensure color contrast (WCAG AA)
□ Add reduced motion media query

BRANDING
────────
□ Register domain per business
□ Add business email
□ Add Google Business Profile
□ Add WhatsApp Business API
```

---

## 8. EFFORT ESTIMATES

### Total Effort: ~200-300 hours across all 5 sites

| Category | Items | Hours | Priority |
|----------|-------|-------|----------|
| A. Infrastructure | 30 | 20h | P0 |
| B. Code Quality | 45 | 30h | P1 |
| C. Design & UX | 60 | 80h | P0 |
| D. Content & Copy | 40 | 30h | P0 |
| E. Pages & Features | 35 | 40h | P1 |
| F. Assets & Images | 30 | 40h | P0 |
| G. SEO & Data | 25 | 15h | P1 |
| H. Performance | 20 | 15h | P2 |
| I. Analytics | 15 | 10h | P2 |
| J. Legal | 15 | 10h | P2 |
| **TOTAL** | **315** | **290h** | |

### Per-Site Breakdown

| Site | Est. Hours | Weeks (1 dev) |
|------|-----------|---------------|
| cocodrilo-fitness | 60h | 1.5 |
| luis-de-leon-concept | 58h | 1.5 |
| bichos-gym | 58h | 1.5 |
| mantra-spa | 58h | 1.5 |
| magnolia-peluqueria | 58h | 1.5 |
| Shared template work | -20h (reuse) | - |
| **Total** | **290h** | **7 weeks** |

### Quick Wins (P0, ~40h total across all)

1. Add real hero background images from Unsplash ✓
2. Fix services category name rendering ✓
3. Add real business phone numbers ✓
4. Add proper Google Maps embed
5. Add cookie consent banner
6. Add testimonials section
7. Add trust badges section
8. Add real service photos
9. Add contact form (not just WhatsApp)
10. Run Lighthouse and improve scores
