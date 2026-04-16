# Implementation Plan - Vete Website Builder
## MVP Development Roadmap by Category

---

## Priority Order (by market size)

| Priority | Category | Business Count | Market Opportunity |
|----------|----------|----------------|-------------------|
| 1 | Peluquería (Hair Salons) | 2,393 | 81% no website |
| 2 | Gimnasio/Fitness | 1,087 | 72% no website |
| 3 | Spa/Wellness | 927 | 76% no website |
| 4 | Uñas (Nail Salons) | 488 | 75% no website |
| 5 | Tatuajes/Piercing | 272 | 70% no website |
| 6 | Estética/Facial | 137 | 77% no website |
| 7 | Maquillaje | 130 | 72% no website |
| 8 | Barbería | 39 | 77% no website |
| 9 | Depilación | 9 | 78% no website |

---

## Phase 1: MVP Definition by Category

### 1.1 Peluquería (Hair Salons) - MVP Features

**5 Core Pages Required:**

1. **Homepage**
   - Hero with salon name and tagline
   - "Book Now" CTA (prominent)
   - Featured services preview
   - Photo gallery preview (3-6 images)
   - Location + hours
   - WhatsApp button

2. **Services Page**
   - Full service menu with prices
   - Service categories (cuts, color, treatments)
   - Duration for each service
   - "Book" buttons per service

3. **Portfolio/Gallery Page**
   - Grid of 20-40 high-quality images
   - Categories: cuts, color, transformations
   - Lightbox view for full size

4. **Team/Stylists Page**
   - Individual stylist profiles
   - Photo, name, specialties
   - Link to their Instagram (if applicable)

5. **Contact/Location Page**
   - Full address with map embed
   - Phone number (click-to-call)
   - WhatsApp link
   - Business hours
   - Parking/transit info

**Technical Requirements:**
- Mobile-first responsive
- Booking integration (GlossGenius/Fresha/Square)
- WhatsApp floating button
- Page load < 3 seconds
- SSL certificate

---

### 1.2 Gimnasio/Fitness - MVP Features

**5 Core Pages Required:**

1. **Homepage**
   - Hero with gym name + USP tagline
   - "Join Now" / "Free Trial" CTA
   - Quick membership pricing preview
   - Class schedule highlight
   - Location + hours

2. **Membership/Pricing Page**
   - Clear pricing tiers
   - What's included per tier
   - Promotional offers
   - FAQ on contracts

3. **Classes/Schedule Page**
   - Weekly timetable
   - Filter by class type, instructor
   - "Book" buttons
   - Class descriptions

4. **Trainers Page**
   - Trainer profiles with photos
   - Certifications/specialties
   - Booking link per trainer

5. **Contact/Location Page**
   - Address with map
   - Phone + email
   - Hours including peak times
   - Parking info

---

### 1.3 Spa/Wellness - MVP Features

**5 Core Pages Required:**

1. **Homepage**
   - Hero with relaxing imagery
   - Featured treatments
   - Package deals preview
   - "Book Now" CTA
   - Location + hours

2. **Treatments Menu**
   - Full list of treatments
   - Prices + durations
   - Benefits description
   - Category filters (face, body, couples)

3. **Packages/Bundles**
   - Special package deals
   - Gift voucher option
   - Savings displayed

4. **About/Team**
   - Story of the spa
   - Therapists/technicians
   - Certifications

5. **Contact/Location**
   - Address + directions
   - Booking inquiry form
   - Hours

---

### 1.4 Uñas (Nail Salons) - MVP Features

**5 Core Pages Required:**

1. **Homepage**
   - Hero with nail art showcase
   - "Book Now" CTA
   - Popular services
   - Gallery preview

2. **Services & Pricing**
   - Manicure types (classic, gel, acrylic)
   - Pedicure types
   - Nail art pricing
   - Add-ons

3. **Portfolio Gallery**
   - 30+ nail designs
   - Categories by style/trend
   - Before/after section

4. **Technicians**
   - Individual profiles
   - Specialties

5. **Contact/Booking**
   - Location + hours
   - Online booking
   - WhatsApp

---

### 1.5 Tatuajes/Piercing - MVP Features

**4 Core Pages Required:**

1. **Homepage**
   - Hero with best work
   - Artist spotlight
   - "Book Consultation" CTA

2. **Portfolio**
   - Full gallery organized by style
   - Artist-specific portfolios
   - Before/after (cover-ups)

3. **Artists**
   - Individual artist pages
   - Styles specialties
   - Booking availability

4. **Info/Contact**
   - Location + hours
   - Aftercare info
   - FAQ
   - Consultation form

---

## Phase 2: Template Architecture

### 2.1 Universal Components

| Component | Description |
|-----------|-------------|
| Header | Logo, nav, book button, WhatsApp |
| Footer | Contact, hours, social links, copyright |
| Hero Section | Image/video background, headline, CTA |
| Service Card | Image, title, price, duration, book button |
| Gallery Grid | Masonry/grid layout, lightbox |
| Team Card | Photo, name, title, specialty, link |
| Testimonial Slider | Quote, client photo, rating |
| Map Block | Embedded Google Maps |
| CTA Banner | Full-width call to action |
| WhatsApp Float | Fixed position chat button |

### 2.2 Category-Specific Components

**Hair Salon:**
- Stylist availability calendar
- Hair color chart
- Appointment booking flow

**Gym:**
- Class schedule table
- Membership comparison table
- Trainer booking calendar

**Spa:**
- Treatment package builder
- Duration calculator

**Nail Salon:**
- Nail art style categories
- Color/polish brand showcase

**Tattoo:**
- Style filter gallery
- Consultation form
- Aftercare accordion

---

## Phase 3: Booking Integration Options

### 3.1 Primary Options for Paraguay

| Platform | Best For | Integration Level |
|----------|----------|-------------------|
| **Fresha** | Free tier, widely used | Full API |
| **GlossGenius** | Salons, marketing tools | Full API |
| **Square** | Small businesses | Full API |
| **Calendly** | Consultations, simple | Widget embed |
| **WhatsApp** | Direct booking | Click-to-chat |

### 3.2 Paraguayan Adaptation

**Recommended Approach:**
1. Primary: Fresha (free, supports Spanish, popular)
2. Fallback: WhatsApp business integration
3. Premium: GlossGenius for salons wanting more features

**Implementation:**
- Embed booking widget in "Book Now" buttons
- Add WhatsApp quick-chat for direct bookings
- Create custom booking form that sends to business WhatsApp

---

## Phase 4: Design Templates

### 4.1 Hair Salon Template (Priority 1)

**Color Palette:**
- Primary: Deep charcoal (#1a1a1a)
- Accent: Rose gold (#b76e79)
- Background: Warm white (#faf9f7)
- Text: Dark gray (#333333)

**Typography:**
- Headings: Playfair Display (serif, elegant)
- Body: Montserrat (sans-serif, readable)

**Layout:**
- Hero: Full-width image, centered text overlay
- Services: 3-column grid, hover effects
- Portfolio: Masonry grid, lightbox
- Team: Horizontal scroll or 2x2 grid

### 4.2 Gym Template (Priority 2)

**Color Palette:**
- Primary: Black (#000000)
- Accent: Electric blue (#0066ff)
- Background: Dark gray (#1a1a1a)
- Text: White (#ffffff)

**Typography:**
- Headings: Oswald (bold, energetic)
- Body: Open Sans (clean, readable)

**Layout:**
- Hero: Video background or high-energy image
- Pricing: 3-4 tier comparison table
- Schedule: Filterable calendar view

### 4.3 Spa Template (Priority 3)

**Color Palette:**
- Primary: Sage green (#8fbc8f)
- Accent: Soft gold (#d4af37)
- Background: Cream (#fdfbf7)
- Text: Charcoal (#36454f)

**Typography:**
- Headings: Cormorant Garamond (elegant serif)
- Body: Lato (clean, light)

---

## Phase 5: Development Checklist

### Pre-Launch Requirements

- [ ] Mobile responsiveness tested on iOS + Android
- [ ] Page load speed < 3 seconds (Core Web Vitals)
- [ ] SSL certificate installed
- [ ] Google Business Profile linked
- [ ] WhatsApp business number integrated
- [ ] Booking system connected and tested
- [ ] Contact forms sending to business
- [ ] Images optimized (WebP format)
- [ ] Basic SEO meta tags per page
- [ ] GDPR/privacy policy page (if required)

---

## Quick Start: Priority 1 MVP (Hair Salon)

### Files to Create:
1. `templates/peluqueria/index.html` - Homepage
2. `templates/peluqueria/servicios.html` - Services
3. `templates/peluqueria/galeria.html` - Portfolio
4. `templates/peluqueria/equipo.html` - Team
5. `templates/peluqueria/contacto.html` - Contact
6. `css/peluqueria.css` - Styling
7. `js/peluqueria.js` - Interactivity

### Components to Build:
- Header with nav + booking button
- Hero section
- Service cards grid
- Gallery lightbox
- WhatsApp floating button
- Contact form
- Map embed
- Footer

### Estimated Development Time:
- Template structure: 2-3 days
- Styling (responsive): 2 days
- Interactivity: 1 day
- Testing: 1 day
- **Total: ~7 days per template**

---

## Next Steps

1. **Confirm MVP scope** - Are 5 pages per category sufficient?
2. **Select first template** - Start with Peluquería?
3. **Booking integration** - Test Fresha vs GlossGenius
4. **Design system** - Create reusable component library
5. **Content template** - Business info input form

*Document created: April 2026*