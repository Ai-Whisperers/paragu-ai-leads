# Business Type Requirements & Research Document
## Complete Technical & Content Requirements for Each Beauty/Wellness Category

---

## Table of Contents
1. [Peluquería (Hair Salons)](#1-peluquería-hair-salons)
2. [Gimnasio/Fitness](#2-gimnasiofitness)
3. [Spa/Wellness](#3-spawellness)
4. [Uñas (Nail Salons)](#4-uñas-nail-salons)
5. [Tatuajes/Piercing](#5-tatuajespiercing)
6. [Barbería](#6-barbería)
7. [Estética/Facial (Aesthetic Clinics)](#7-estéticafacial-aesthetic-clinics)
8. [Maquillaje (Makeup Artists)](#8-maquillaje-makeup-artists)
9. [Depilación (Hair Removal)](#9-depilación-hair-removal)

---

# 1. PELUQUERÍA (Hair Salons)

## 1.1 Market Data (Paraguay)
- **Total Businesses**: 2,393
- **No Website**: 1,938 (81%)
- **Has Website**: 455 (19%)
- **Priority A Leads**: 1,653

## 1.2 Target Audience Persona

**Primary Customer**: Woman, 25-45, middle-class, repeat customer
- Books appointments 2-4 weeks in advance
- Researches styles on Instagram before visiting
- Price-sensitive but willing to pay for quality
- Values personal relationship with stylist

**Secondary Customer**: Men seeking cuts, Youth (18-25) for color/trends

## 1.3 Service Offerings (Typical)

| Service Category | Services Included |
|-----------------|-------------------|
| Cuts | Women's cut, Men's cut, Children's cut, Trim |
| Color | Full color, Highlights, Balayage, Ombre, Touch-up |
| Treatments | Keratin, Deep conditioning, Scalp treatment |
| Styling | Blowout, Updo, Special event styling |
| Extensions | Tape-ins, Clip-ins, Sew-in |

## 1.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero image, quick booking, featured services, location
- [ ] **Services Menu** - All services with prices, durations, descriptions
- [ ] **Portfolio Gallery** - 20-40 images organized by service type
- [ ] **Team/Stylists** - Individual profiles with specialties, Instagram links
- [ ] **Contact/Location** - Address, map, hours, phone, Messaging

### Functional Requirements
- [ ] Online booking integration (Fresha/GlossGenius/Square)
- [ ] Messaging direct booking button
- [ ] Click-to-call on mobile
- [ ] Service menu with filter capability
- [ ] Image lightbox/gallery view
- [ ] Responsive design (mobile-first)
- [ ] Page load < 3 seconds

### Content Requirements

**Homepage:**
- Hero image: High-quality salon interior or featured style
- Headline: Salon name + tagline (e.g., "Your Best Look in [City]")
- CTA: "Book Now" button (primary), "View Services" (secondary)
- Quick service cards: 3-4 popular services with prices
- Location snippet: Address + hours
- Social proof: Star rating if available

**Services Page:**
- Service categories (accordion or tabbed)
- Each service: Name, price range, duration, brief description
- "Book" button per service or category
- Add-on services clearly marked

**Portfolio:**
- Grid layout, minimum 20 images
- Categories: Cuts, Color, Highlights, Special Styling
- Lightbox for full-size viewing
- Instagram feed integration optional

**Team Page:**
- Individual cards: Photo, name, title, specialties
- Years of experience
- Link to personal Instagram (optional)
- "Book with [Name]" buttons

**Contact:**
- Full address with Google Maps embed
- Phone number (click-to-call on mobile)
- Messaging business link
- Business hours (including special hours)
- Parking/transportation info
- Contact form for inquiries

## 1.5 Design Requirements

### Color Palette Options
| Style | Primary | Accent | Background | Typography |
|-------|---------|--------|------------|------------|
| Elegant | Charcoal #1a1a1a | Rose Gold #b76e79 | Warm White #faf9f7 | Playfair + Montserrat |
| Modern | Black #000000 | Copper #b87333 | Off-white #f5f5f5 | Oswald + Open Sans |
| Natural | Sage #8f9e8a | Terracotta #c17c5f | Cream #fdfbf7 | Cormorant + Lato |

### Layout Specifications
- Max content width: 1200px
- Hero height: 70vh (desktop), 60vh (mobile)
- Service card grid: 3 columns (desktop), 1 column (mobile)
- Gallery grid: 4 columns (desktop), 2 columns (mobile)
- Spacing between sections: 60px (desktop), 40px (mobile)

### Image Requirements
- Hero images: 1920x1080px minimum
- Service images: 800x600px
- Portfolio images: 1200x1200px (square) or 4:5 ratio
- Team photos: 600x600px
- Format: WebP with JPG fallback

## 1.6 Booking Integration

### Primary Options
1. **Fresha** (Recommended - Free)
   - Free for business
   - Spanish language support
   - Messaging notifications
   - Recurring bookings

2. **GlossGenius**
   - Marketing tools included
   - Loyalty program
   - Product sales

3. **Square Appointments**
   - Good for multi-service
   - Inventory tracking

### Messaging Fallback
- Direct Messaging business link
- Pre-filled message template: "Hola! Quisiera agendar una cita para [service]"

## 1.7 SEO Requirements

### On-Page SEO
- Title tag: "[Salon Name] - Peluquería en [City] | Servicios y Precios"
- Meta description: "Cortes, coloración y tratamientos en [City]. Reserva tu cita online. Precios desde [lowest price]."
- H1: Salon name
- H2: Service categories, Location
- Local keywords: "peluquería [city]", "corte de cabello [neighborhood]"

### Local SEO
- Google Business Profile link
- NAP consistency (Name, Address, Phone)
- Location pages for multi-branch
- "Near me" optimization

### Content SEO
- Blog: Hair care tips, trend guides (optional)
- FAQ section: Common questions answered
- Image alt text: Descriptive, Spanish keywords

## 1.8 Technical Requirements

### Performance
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1
- Time to Interactive: < 3s

### Accessibility
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader friendly
- Alt text for all images
- Color contrast 4.5:1 minimum

### Security
- SSL certificate (HTTPS)
- Contact form spam protection
- Privacy policy page

---

# 2. GIMNASIO/FITNESS

## 2.1 Market Data (Paraguay)
- **Total Businesses**: 1,087
- **No Website**: 783 (72%)
- **Has Website**: 304 (28%)
- **Priority A Leads**: 761

## 2.2 Target Audience Persona

**Primary Customer**: Adult 25-45, fitness-conscious, comparing options
- Researches 3-5 gyms before joining
- Looks for pricing transparency
- Wants to see equipment and facility
- Often searches "gym near me" on mobile

**Secondary**: Athletes (specialty training), Seniors (wellness), Youth (group classes)

## 2.3 Service Offerings (Typical)

| Category | Offerings |
|----------|-----------|
| Memberships | Monthly, annual, pay-per-visit, corporate |
| Group Classes | Yoga, HIIT, Spinning, CrossFit, Pilates |
| Personal Training | 1-on-1 sessions, small group |
| Amenities | Pool, sauna, locker rooms, showers |
| Additional | Nutrition coaching, physical therapy |

## 2.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero, USP, quick pricing, class schedule preview, location
- [ ] **Membership/Pricing** - Clear tiers, pricing, what's included
- [ ] **Class Schedule** - Live timetable, filter by class/instructor/time
- [ ] **Trainers** - PT profiles with specialties, packages
- [ ] **Contact/Location** - Address, map, hours, tour request

### Functional Requirements
- [ ] Live class schedule with booking
- [ ] Membership price display (starting from)
- [ ] Free trial offer capture
- [ ] Facility photo gallery
- [ ] Trainer profiles with booking
- [ ] Location with directions + parking
- [ ] Mobile-responsive
- [ ] Messaging for inquiries

### Content Requirements

**Homepage:**
- Hero: High-energy gym image or video
- Headline: "[Gym Name] - Fitness en [City]"
- USP: What makes you different (e.g., "24/7 Access", "Best Trainers")
- Pricing preview: "Memberships from [price]/month"
- Class schedule highlight: Today's popular classes
- CTA: "Join Now" / "Free Trial"

**Pricing Page:**
- 3-4 membership tiers in table format
- Clear comparison of what's included
- Promotional pricing if applicable
- FAQ: Cancellation, freeze, joining fee
- "Calculate savings" tool (optional)

**Schedule Page:**
- Weekly calendar view
- Filter: Class type, instructor, time, day
- Class cards: Name, time, instructor, capacity
- "Book" buttons integrated
- Link to waitlist if full

**Trainers Page:**
- Individual trainer cards
- Photo, name, certifications
- Specialties (weight loss, muscle, sports)
- Available packages
- "Book Session" buttons

**Contact:**
- Full address with map
- Phone, email, Messaging
- Opening hours (including 24/7 if applicable)
- Parking info
- "Schedule Tour" CTA

## 2.5 Design Requirements

### Color Palette Options
| Style | Primary | Accent | Background | Typography |
|-------|---------|--------|------------|------------|
| Energetic | Black #000000 | Electric Blue #0066ff | Dark Gray #1a1a1a | Oswald + Open Sans |
| Premium | Charcoal #2d2d2d | Gold #c9a227 | White #ffffff | Montserrat + Lato |
| Community | Forest Green #2d5a3d | Orange #ff6b35 | Light Gray #f4f4f4 | Poppins + Roboto |

### Layout Specifications
- Hero height: 80vh (video background preferred)
- Pricing table: Side-by-side tier comparison
- Schedule: Full calendar with scrollable days
- Trainer grid: 3-4 columns (desktop)

## 2.6 Booking Integration

### Primary Options
1. **Mindbody** - Industry standard, robust scheduling
2. **Glofox** - Good for boutique fitness
3. **TeamUp** - Simple, affordable
4. **Gymcatch** - UK-based, simple

### Integration Requirements
- Live class schedule sync
- Booking confirmation emails
- Waitlist functionality
- Membership management sync

## 2.7 SEO Requirements

### Keywords to Target
- "Gimnasio [city]"
- "Gimnasio cerca de mí"
- "Clases de [type] en [city]"
- "Entrenador personal [city]"
- "Membresía gimnasio precios"

### Content Strategy
- Blog: Fitness tips, workout guides, nutrition
- Local landing pages per neighborhood
- Service-specific pages (e.g., "CrossFit [city]")
- FAQ: Guest policy, equipment, etc.

---

# 3. SPA/WELLNESS

## 3.1 Market Data (Paraguay)
- **Total Businesses**: 927
- **No Website**: 704 (76%)
- **Has Website**: 223 (24%)
- **Priority A Leads**: 649

## 3.2 Target Audience Persona

**Primary Customer**: Woman 30-55, seeking relaxation and self-care
- Books for special occasions or regular self-care
- Influenced by reviews and visuals
- Willing to pay for premium experience
- Often searches for "spa near me"

**Secondary**: Couples (romantic getaways), Business travelers, Mums (day off)

## 3.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Massages | Swedish, Deep tissue, Hot stone, Sports, Couples |
| Facials | Hydrating, Anti-aging, Deep cleaning, LED therapy |
| Body Treatments | Scrubs, Wraps, Body polishes |
| Packages | Day packages, Couples experiences, Gift vouchers |
| Additional | Sauna, Steam room, Jacuzzi |

## 3.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero, featured treatments, package deals, booking CTA
- [ ] **Treatments Menu** - Full list with prices, durations, descriptions
- [ ] **Packages** - Special deals, gift options
- [ ] **About** - Spa story, therapists, philosophy
- [ ] **Contact** - Location, hours, booking form

### Functional Requirements
- [ ] Treatment booking with date/time selection
- [ ] Package/ deal showcase
- [ ] Calming visual design (soft colors, nature imagery)
- [ ] Facility photos (environment is selling point)
- [ ] Gift voucher purchase option
- [ ] Mobile-responsive
- [ ] Messaging for inquiries

### Content Requirements

**Homepage:**
- Hero: Serene spa imagery, video tour optional
- Headline: "[Spa Name] - Relaxación en [City]"
- Featured treatments: 3-4 popular services
- Package deals: Highlight savings
- CTA: "Book Now" / "Gift Voucher"

**Treatments Page:**
- Category filters: Face, Body, Massages
- Each treatment: Name, price, duration, benefits
- "Book" button per treatment

**Packages Page:**
- Package cards: Name, included treatments, price, savings
- Gift voucher section
- "For Him", "For Her", "Couples" categories

**About Page:**
- Story: How spa started, philosophy
- Team: Therapists, certifications
- Facility: Environment description

**Contact:**
- Address (often destination/spa location)
- Hours (including any special timing)
- Booking form + phone + Messaging

## 3.5 Design Requirements

### Color Palette Options
| Style | Primary | Accent | Background | Typography |
|-------|---------|--------|------------|------------|
| Luxury | Deep Navy #1a2744 | Gold #c9a227 | Cream #fdfbf7 | Cormorant + Lato |
| Nature | Sage Green #8f9e8a | Earth Brown #8b7355 | Off-white #fafaf8 | Cormorant + Open Sans |
| Minimal | Soft White #f8f8f8 | Blush Pink #e8c4c4 | White #ffffff | Montserrat + Lato |

### Visual Requirements
- Generous whitespace
- Nature-inspired imagery (flowers, water, stones)
- Soft, rounded corners
- Subtle animations (fade-in)
- Calming, slow-moving visuals

---

# 4. UÑAS (NAIL SALONS)

## 4.1 Market Data (Paraguay)
- **Total Businesses**: 488
- **No Website**: 366 (75%)
- **Has Website**: 122 (25%)
- **Priority A Leads**: 342

## 4.2 Target Audience Persona

**Primary Customer**: Woman 20-45, beauty-conscious, nail art enthusiast
- Follows nail trends on Instagram
- Books 1-2 weeks ahead for appointments
- Price-aware but wants quality

**Secondary**: Brides (wedding nails), Special events, Men (basic manicure)

## 4.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Manicures | Classic, Gel, Shellac, Acrylic, Dip powder |
| Pedicures | Classic, Spa, Gel, Medical |
| Nail Art | Simple designs, Custom, 3D, Chrome, French |
| Add-ons | Cuticle care, Nail strengthening, Hand massage |
| Kids | Children's manicures |

## 4.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero with nail art showcase, booking CTA, popular services
- [ ] **Services** - Manicure, pedicure, art categories with prices
- [ ] **Gallery** - 30+ nail designs organized by style
- [ ] **Technicians** - Nail artist profiles
- [ ] **Contact** - Location, hours, booking

### Functional Requirements
- [ ] Service menu with clear pricing
- [ ] Online booking (same-day availability important)
- [ ] Portfolio gallery (critical for this category)
- [ ] Nail art style categories
- [ ] Before/after transformations
- [ ] Mobile-responsive
- [ ] Messaging booking

### Content Requirements

**Homepage:**
- Hero: Stunning nail art image
- Headline: "[Salon Name] - Uñas en [City]"
- Quick services: 3-4 popular with prices
- Gallery preview: 6 top designs
- CTA: "Book Now"

**Services:**
- Tabs/accordion: Manicure, Pedicure, Nail Art
- Each service: Name, price range, duration
- Add-ons clearly marked
- "Book" buttons

**Gallery:**
- 30+ high-quality images
- Categories: Basic, Gel, Acrylic, Art, Bridal
- Lightbox for zoom
- Before/after section

**Technicians:**
- Cards: Photo, name, specialties
- Portfolio link per technician

---

# 5. TATUAJES/PIERCING

## 5.1 Market Data (Paraguay)
- **Total Businesses**: 272
- **No Website**: 190 (70%)
- **Has Website**: 82 (30%)
- **Priority A Leads**: 190

## 5.2 Target Audience Persona

**Primary Customer**: Adult 18-45, seeking custom tattoo or piercing
- Researches artists extensively
- Looks at portfolio extensively
- Wants consultation before committing
- Values hygiene and safety

**Secondary**: First-timers (nervous, need reassurance), Cover-up customers, Collectors

## 5.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Tattoos | Custom designs, Traditional, Realism, Blackwork, Japanese, Cover-ups |
| Piercings | Ear, Nose, Lip, Navel, Industrial, Dermal |
| Additional | Touch-ups, Consultations, Design creation |

## 5.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero with best work, artist spotlight, consultation CTA
- [ ] **Portfolio** - Full gallery organized by style, artist
- [ ] **Artists** - Individual profiles with specialties
- [ ] **Info/Contact** - Location, hours, aftercare, FAQ

### Functional Requirements
- [ ] Portfolio gallery (most important feature)
- [ ] Artist-specific portfolios
- [ ] Consultation booking/request form
- [ ] Style categories for filtering
- [ ] Aftercare information
- [ ] FAQ for first-timers
- [ ] Mobile-responsive

### Content Requirements

**Homepage:**
- Hero: Best piece from portfolio
- Headline: "[Studio Name] - Tatuajes en [City]"
- Artist spotlight: Featured artist
- CTA: "Book Consultation" (not direct booking)
- Trust signals: Hygiene certifications, reviews

**Portfolio:**
- Full gallery: 50+ images
- Filter by: Style, Artist, Body part
- Artist section: Each artist's work
- Before/after: Cover-ups

**Artists:**
- Individual pages: Photo, bio, years experience
- Styles: What they're known for
- Availability: Booking status

**Info:**
- Location + hours
- Aftercare guide (critical)
- FAQ: Pain, healing, age requirements
- Consultation process explanation

## 5.5 Design Requirements

### Aesthetic
- Dark theme typical
- High contrast
- Artistic, edgy feel
- Portfolio-first layout

---

# 6. BARBERÍA

## 6.1 Market Data (Paraguay)
- **Total Businesses**: 39
- **No Website**: 30 (77%)
- **Has Website**: 9 (23%)
- **Priority A Leads**: 27

## 6.2 Target Audience Persona

**Primary Customer**: Men 18-55, grooming-conscious
- Values skill and technique
- Often loyal to specific barber
- Looks at photos of cuts
- Quick visits, often walk-in

**Secondary**: Boys (first cuts), Grooms (wedding), Older gentlemen (traditional)

## 6.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Cuts | Regular cut, Fade, Buzz cut, Beard trim |
| Shaves | Hot towel shave, Beard sculpting |
| Styling | Hair and beard, Special event |
| Additional | Facial, Head massage |

## 6.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero with cut showcase, services, location
- [ ] **Services** - Menu with prices
- [ ] **Portfolio** - Gallery of real cuts
- [ ] **Barbers** - Team profiles
- [ ] **Contact** - Location, hours, booking

### Functional Requirements
- [ ] Service menu with pricing
- [ ] Online booking (or walk-in policy)
- [ ] Portfolio of real cuts (NOT stock photos)
- [ ] Barber profiles
- [ ] Mobile-first (82% of searches on mobile)
- [ ] Click-to-call
- [ ] Walk-in policy clearly stated

### Content Requirements

**Homepage:**
- Hero: Best cut photo
- Headline: "[Barbershop Name] - Barbería en [City]"
- Services snippet: 3 top services + prices
- Portfolio preview
- Location + hours
- CTA: "Book" or "Walk In"

**Services:**
- Clear list with prices
- Duration estimates
- "Book" buttons

**Portfolio:**
- 20+ real cut photos
- Categories: Fades, Classic, Beards
- Before/after

**Barbers:**
- Individual cards: Photo, name, specialties
- "Book with [Name]" buttons

---

# 7. ESTÉTICA/FACIAL (Aesthetic Clinics)

## 7.1 Market Data (Paraguay)
- **Total Businesses**: 137
- **No Website**: 105 (77%)
- **Has Website**: 32 (23%)
- **Priority A Leads**: 96

## 7.2 Target Audience Persona

**Primary Customer**: Woman 30-60, seeking professional skincare/anti-aging
- Wants results, not just relaxation
- Researches treatments extensively
- Concerned about safety and credentials
- Willing to pay premium for quality

**Secondary**: Younger (acne treatments), Men (grooming), Post-procedure care

## 7.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Facials | Hydrafacial, Microdermabrasion, Chemical peels, LED |
| Injectables | Botox, Dermal fillers, PRP |
| Body | Laser treatments, Skin tightening, Cellulite |
| Treatments | Acne treatment, Scar revision, Pigmentation |

## 7.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero, treatments overview, before/after, booking
- [ ] **Treatments** - Service list with descriptions
- [ ] **Before/After** - Real results gallery (critical)
- [ ] **Team** - Practitioners with credentials
- [ ] **Contact** - Location, consultation booking

### Functional Requirements
- [ ] Treatment menu with descriptions
- [ ] Before/after gallery (most important)
- [ ] Provider credentials displayed
- [ ] Consultation booking
- [ ] Pricing transparency (or "from" pricing)
- [ ] Trust signals (certifications, reviews)
- [ ] Mobile-responsive
- [ ] Messaging for inquiries

### Content Requirements

**Homepage:**
- Hero: Professional clinic image
- Headline: "[Clinic Name] - Estética en [City]"
- Key treatments: 3-4 with images
- Before/after preview
- CTA: "Book Consultation"

**Treatments:**
- Categorized: Face, Body, Injectables
- Each: Name, description, "from" price, duration
- "Learn More" expandable

**Before/After:**
- Organized by treatment type
- Real results (critical)
- Consent notes

**Team:**
- Photo, name, title
- Credentials: Training, certifications
- Experience years

---

# 8. MAQUILLAJE (Makeup Artists)

## 8.1 Market Data (Paraguay)
- **Total Businesses**: 130
- **No Website**: 94 (72%)
- **Has Website**: 36 (28%)
- **Priority A Leads**: 91

## 8.2 Target Audience Persona

**Primary Customer**: Woman 22-40, special events (weddings, parties)
- Needs to see artist's style
- Often books months ahead for weddings
- Reviews portfolio extensively
- Wants trial before event

**Secondary**: Editorial/Commercial, Bridal parties, Everyday glam

## 8.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Bridal | Full bridal makeup, Bridal party |
| Events | Special occasion, Prom, Photoshoot |
| Editorial | Fashion, Magazine, Commercial |
| Lessons | 1-on-1 makeup lessons |

## 8.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero with stunning look, portfolio preview, booking
- [ ] **Portfolio** - Full gallery organized by type
- [ ] **Services** - Service list with pricing
- [ ] **About** - Artist bio, experience, style
- [ ] **Contact** - Inquiry form, availability

### Functional Requirements
- [ ] Portfolio gallery (most important)
- [ ] Service menu with prices
- [ ] Inquiry/booking form (not always direct book)
- [ ] Before/after looks
- [ ] Social media integration (Instagram primary)
- [ ] Mobile-responsive

### Content Requirements

**Homepage:**
- Hero: Best editorial/bridal shot
- Headline: "[Artist Name] - Maquillaje en [City]"
- Portfolio preview: 4-6 top images
- Services overview
- CTA: "Book Now" / "Inquire"

**Portfolio:**
- 30+ images minimum
- Categories: Bridal, Events, Editorial, Lessons
- Before/after pairs

**Services:**
- Service list with prices
- What's included (products, touch-up time)
- Trial information (if applicable)

**About:**
- Artist story, experience
- Training, notable work
- Style description

---

# 9. DEPILACIÓN (Hair Removal)

## 9.1 Market Data (Paraguay)
- **Total Businesses**: 9
- **No Website**: 7 (78%)
- **Has Website**: 2 (22%)
- **Priority A Leads**: 7

## 9.2 Target Audience Persona

**Primary Customer**: Woman 20-45, seeking permanent/permanent hair reduction
- Researches technology and safety
- Needs consultation (skin type assessment)
- Books package treatments
- Concerned about pain and safety

**Secondary**: Men (back, chest), Transformations (PCOS)

## 9.3 Service Offerings (Typical)

| Category | Services |
|----------|----------|
| Laser | Diode, Alexandrite, Nd:YAG (all skin types) |
| Waxing | Brazilian, Full body, Facial |
| Electrolysis | Permanent (for small areas) |
| Packages | Multi-session deals, Body areas |

## 9.4 MVP Feature Requirements

### Page Structure
- [ ] **Homepage** - Hero, technology info, treatment areas, consultation CTA
- [ ] **Treatments** - Full list with pricing packages
- [ ] **Technology** - Equipment information (FDA-approved)
- [ ] **Results** - Before/after (minimal for hair removal)
- [ ] **Contact** - Location, free consultation booking

### Functional Requirements
- [ ] Treatment area pricing packages
- [ ] Technology/equipment information
- [ ] Free consultation booking
- [ ] Skin type suitability info
- [ ] Safety information
- [ ] Pricing transparency
- [ ] Mobile-responsive
- [ ] Messaging for inquiries

### Content Requirements

**Homepage:**
- Hero: Smooth skin result image
- Headline: "[Clinic Name] - Depilación en [City]"
- Technology highlights
- Treatment areas quick view
- CTA: "Free Consultation"

**Treatments:**
- Area-based pricing tables
- Packages: 6, 8, 10 session options
- Pricing ranges
- What's included

**Technology:**
- Equipment brand/type
- FDA/CE approval
- Why this technology (painless, all skin types)
- Comparison to alternatives

**Contact:**
- Location + hours
- Free consultation form
- Phone + Messaging

---

# CROSS-CATEGORY SUMMARY

## Essential Features Matrix

| Feature | Hair | Gym | Spa | Nails | Tattoo | Barber | Aesthetic | Makeup | Hair Removal |
|---------|------|-----|-----|-------|--------|--------|-----------|--------|--------------|
| Online Booking | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ |
| Service Menu | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Portfolio Gallery | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Staff Profiles | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Before/After | ⚠️ | ⚠️ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Pricing Display | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ | ✅ |
| Location/Map | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Messaging | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| Mobile-First | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

✅ Essential | ⚠️ Important | ❌ Not Required

## Booking Method by Category

| Category | Primary Booking | Paraguayan Adaptation |
|----------|-----------------|----------------------|
| Hair Salons | Platform (Fresha) | Messaging fallback |
| Gym/Fitness | Platform (Mindbody) | Form + Messaging |
| Spa/Wellness | Platform (Fresha) | Messaging fallback |
| Nail Salons | Platform (Fresha) | Messaging fallback |
| Tattoo/Piercing | Consultation form | Messaging inquiry |
| Barber Shops | Platform (Square) | Walk-in + Messaging |
| Aesthetic Clinics | Consultation form | Messaging inquiry |
| Makeup Artists | Inquiry form | Messaging inquiry |
| Hair Removal | Consultation form | Messaging inquiry |

## Technical Requirements Summary

### All Categories Must Have:
- Mobile-responsive design
- SSL certificate
- Contact form
- Google Maps embed
- Social media links
- Messaging integration
- Fast loading (< 3 seconds)
- Basic SEO (title, meta, schema)

### Performance Targets:
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1
- Time to Interactive: < 3s
- Mobile score (Lighthouse): > 90

---

*Document created: April 2026*