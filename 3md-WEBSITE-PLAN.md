# WEBSITE PLAN: 3 MIND (3MD) — Agencia Creativa

## Domain: 3md.paragu-ai.com (or register 3mindpy.com)
## Stack: Next.js 16 + Tailwind CSS v4 + Docker Swarm + Traefik
## Timeline: ~40 hours

---

## PHASE 1: FOUNDATION (8h)

### Repo Setup
- Create repo Ai-Whisperers/3md-website
- Clone template-nextjs-client as base
- Set up Dockerfile, docker-compose, Traefik labels
- Configure Cloudflare DNS (A record to VPS)
- Deploy scaffold with 200 page

### Design System
- Colors: Dark creative agency palette
  - Primary: #0a0a0a (near black)
  - Secondary: #ff6b35 (energetic orange)
  - Accent: #ffffff
  - Background: #f5f5f5
- Fonts: 
  - Heading: Playfair Display (elegant/elevated)
  - Body: Inter (clean/modern)
- CSS custom properties via @theme

---

## PHASE 2: PAGES (20h)

### Home (/)
- Full-screen hero with showreel video background
- Animated headline: "Transformamos ideas en experiencias visuales impactantes"
- CTA: "Ver Portfolio" + "Contactanos"
- Client logo bar (VW, Carmen Steffens, Lez a Lez, etc.)
- Featured work grid (4 items)
- Stats counter (X proyectos, X clientes, X anos)
- CTA banner

### Portfolio (/portfolio)
- Grid layout with filter buttons (Todo, Video, Foto, Marca)
- Project cards with hover overlay + title
- Lazy-loaded images + lightbox
- Individual project pages (/portfolio/[slug])
  - Hero image/video
  - Client name + industry
  - Description (ES/EN toggle)
  - Gallery
  - Results/metrics

### Services (/servicios)
- 4 service cards in grid:
  1. Marketing Digital — Social media, ads, strategy
  2. Produccion Audiovisual — Film, video, editing
  3. Fotografia — Product, event, brand photography
  4. Publicidad — Campaign creation, branding
- Each card with icon + description + CTA
- Expandable details with pricing ranges

### About (/nosotros)
- Brand story: "3 MIND nace de la idea de..."
- Team section (founder + collaborators)
- Values: Creativity, Strategy, Impact

### Contact (/contacto)
- Contact form (name, email, phone, project type, message)
- WhatsApp click-to-chat
- Google Maps embed (Fray Luis de Leon C/Venezuela)
- Email: 3mindpy@gmail.com
- Phone: 0991 691501
- Instagram link: @somos3md

### Blog (/blog)
- Case studies formatted as blog posts
- Each project becomes a blog entry
- Tags: video, fotografia, marketing, eventos

---

## PHASE 3: FEATURES (8h)

- Dark mode (agency aesthetic)
- Video background on hero (showreel)
- Smooth scroll animations
- Image lazy loading with blur placeholder
- Portfolio filter with URL state
- Multilingual support (ES default, EN toggle)
- Cookie consent
- Analytics (Plausible or GA4)

---

## PHASE 4: CONTENT (4h)

- Copywriting for all pages (ES + EN)
- Extract 5 best portfolio projects from Instagram
- Create project descriptions with client context
- Write service descriptions with pricing ranges
- SEO meta tags per page
- Schema.org JSON-LD (CreativeAgency type)

---

## EFFORT SUMMARY

| Phase | Hours | Deliverables |
|-------|-------|-------------|
| Foundation | 8h | Repo, deploy, DNS, design system |
| Pages | 20h | Home, Portfolio, Services, About, Contact, Blog |
| Features | 8h | Dark mode, video, animations, i18n, analytics |
| Content | 4h | Copy, photos, SEO, structured data |
| **TOTAL** | **40h** | **Full professional agency website** |
