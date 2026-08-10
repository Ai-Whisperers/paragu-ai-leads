# Template Specifications Document
## Detailed Design & Technical Specifications for Each Business Type

---

# 1. PELUQUERÍA (HAIR SALON) TEMPLATE

## 1.1 Visual Identity

### Color Palette - Option A: "Elegant Rose"
```
--primary: #1a1a1a        /* Charcoal - headers, text */
--secondary: #b76e79       /* Rose gold - accents, buttons */
--background: #faf9f7      /* Warm white - page background */
--surface: #ffffff         /* White - cards, sections */
--text: #333333            /* Dark gray - body text */
--text-light: #666666      /* Medium gray - secondary text */
--success: #4a7c59         /* Sage - availability */
--error: #c0392b           /* Deep red - errors */
```

### Color Palette - Option B: "Modern Copper"
```
--primary: #000000         /* Black */
--secondary: #b87333       /* Copper */
--background: #f5f5f5      /* Off-white */
--surface: #ffffff         /* White */
--text: #1a1a1a            /* Near black */
--text-light: #555555      /* Gray */
--accent: #d4a574          /* Light copper */
```

### Typography
```
--font-heading: 'Playfair Display', serif
--font-body: 'Montserrat', sans-serif
--font-accent: 'Cormorant Garamond', serif

/* Sizes */
--h1: 3rem (48px) - Hero headlines
--h2: 2.25rem (36px) - Section titles
--h3: 1.5rem (24px) - Card titles
--h4: 1.25rem (20px) - Subtitles
--body: 1rem (16px)
--small: 0.875rem (14px)
--caption: 0.75rem (12px)
```

### Spacing System
```
--space-xs: 4px
--space-sm: 8px
--space-md: 16px
--space-lg: 24px
--space-xl: 32px
--space-2xl: 48px
--space-3xl: 64px
--space-4xl: 96px

/* Section padding */
--section-padding: 80px (desktop), 60px (tablet), 40px (mobile)
```

---

## 1.2 Layout Specifications

### Header Component
- **Height**: 80px (desktop), 70px (mobile)
- **Layout**: Logo left, nav center, CTA right
- **Sticky**: Yes, background blur on scroll
- **Mobile**: Hamburger menu, full-screen overlay
- **Elements**:
  - Logo (max 200px width)
  - Nav links: Inicio, Servicios, Galería, Equipo, Contacto
  - CTA button: "Reservar" (rose gold background)

### Hero Section
- **Height**: 70vh (desktop), 60vh (mobile)
- **Background**: Full-width image or slider
- **Overlay**: Dark gradient (50% opacity) for text readability
- **Content**:
  - Headline (h1): Salon name + tagline
  - Subheadline: Brief value proposition
  - CTAs: Primary "Reservar Ahora", Secondary "Ver Servicios"
  - Quick info: Location icon + address

### Services Grid
- **Layout**: 3 columns (desktop), 2 (tablet), 1 (mobile)
- **Card Design**:
  - Image (16:9 ratio)
  - Service name (h3)
  - Price range
  - Duration badge
  - "Reservar" button
- **Animation**: Fade up on scroll, hover scale (1.02)

### Portfolio Gallery
- **Layout**: Masonry grid
- **Columns**: 4 (desktop), 3 (tablet), 2 (mobile)
- **Image sizes**: Variable, optimized for visual impact
- **Interaction**: Lightbox on click, swipe on mobile
- **Categories**: Cuts, Color, Highlights, Styles
- **Filter**: Tab-based filtering

### Team Section
- **Layout**: Horizontal scroll (mobile), 4-column grid (desktop)
- **Card Design**:
  - Circle image (150px)
  - Name
  - Title (e.g., "Especialista en Color")
  - Instagram icon
  - "Reservar con [Name]" button

### Contact Section
- **Layout**: 2 columns - info left, form right
- **Info Column**:
  - Address with map
  - Phone (click-to-call)
  - Messaging button
  - Hours (table format)
  - Social links
- **Form**: Name, Phone, Service dropdown, Preferred date, Message

### Footer
- **Background**: Primary color
- **Layout**: 4 columns
- **Columns**: About, Quick Links, Contact, Social
- **Bottom**: Copyright, Privacy link

---

## 1.3 Component States

### Buttons
```
/* Primary */
background: var(--secondary)
color: white
padding: 12px 24px
border-radius: 4px
transition: all 0.3s ease

/* Hover */
background: #a05a65 (darker rose)
transform: translateY(-2px)
box-shadow: 0 4px 12px rgba(183, 110, 121, 0.3)

/* Active */
transform: translateY(0)

/* Disabled */
opacity: 0.6
cursor: not-allowed
```

### Service Cards
```
/* Default */
background: white
border-radius: 8px
box-shadow: 0 2px 8px rgba(0,0,0,0.08)
transition: all 0.3s ease

/* Hover */
transform: translateY(-4px)
box-shadow: 0 8px 24px rgba(0,0,0,0.12)

/* Image hover */
transform: scale(1.05)
```

---

## 1.4 Responsive Breakpoints
```
--bp-mobile: 480px
--bp-tablet: 768px
--bp-desktop: 1024px
--bp-wide: 1440px
```

## 1.5 Animations
```
/* Page load */
fade-in: 0.6s ease-out

/* Scroll animations */
fade-up: translateY(30px) → translateY(0), 0.6s, staggered 0.1s

/* Hover transitions */
default: 0.3s ease

/* Modal */
scale-in: 0.3s ease
```

---

# 2. GIMNASIO/FITNESS TEMPLATE

## 2.1 Visual Identity

### Color Palette - "Energy Black"
```
--primary: #000000         /* Black */
--secondary: #0066ff       /* Electric blue */
--accent: #00d4ff          /* Cyan */
--background: #0a0a0a      /* Near black */
--surface: #1a1a1a         /* Dark gray cards */
--surface-light: #2d2d2d   /* Elevated surfaces */
--text: #ffffff            /* White text */
--text-muted: #888888      /* Gray text */
--success: #00ff88         /* Bright green */
--warning: #ffaa00         /* Orange */
```

### Typography
```
--font-heading: 'Oswald', sans-serif    /* Bold, athletic */
--font-body: 'Open Sans', sans-serif    /* Clean, readable */
--font-accent: 'Montserrat', sans-serif /* Buttons, labels */

/* Weights: 400 (regular), 500 (medium), 600 (semibold), 700 (bold) */
```

### Visual Style
- High contrast, dark theme
- Bold typography, uppercase for headings
- Geometric accents, angular elements
- Energy-driven imagery
- Progress/results focused

---

## 2.2 Layout Specifications

### Hero Section
- **Style**: Video background or high-energy image
- **Content**:
  - Logo
  - USP tagline (e.g., "TRANSFORMA TU CUERPO")
  - "ENTRENAMIENTOS INTENSOS"
  - CTA: "PRUEBA gratis" + "VER PLANES"
  - Quick stats: 500+ members, 50+ classes/week

### Pricing Section
- **Layout**: 3-4 tier comparison table
- **Card Design**:
  - Tier name (e.g., "BÁSICO", "PRO", "ELITE")
  - Price prominent (large font)
  - Feature list with checkmarks
  - "ELEGIR" button
  - "Más popular" badge on middle tier

### Class Schedule
- **Layout**: Weekly calendar grid
- **Filters**: Day tabs, class type dropdown, instructor
- **Card**: Class name, time, instructor, "RESERVAR" button
- **Color coding**: By class type

### Trainer Cards
- **Layout**: 3-4 columns
- **Design**: Photo, name, specialty, certifications, "RESERVAR"

---

# 3. SPA/WELLNESS TEMPLATE

## 3.1 Visual Identity

### Color Palette - "Serene Nature"
```
--primary: #8f9e8a         /* Sage green */
--secondary: #c4a77d       /* Soft gold */
--accent: #e8dcc8          /* Cream */
--background: #fdfbf7      /* Warm cream */
--surface: #ffffff         /* White */
--text: #36454f           /* Charcoal */
--text-light: #6b7c7c      /* Muted green-gray */
--dark-accent: #2d4a3e     /* Deep forest */
```

### Typography
```
--font-heading: 'Cormorant Garamond', serif  /* Elegant, editorial */
--font-body: 'Lato', sans-serif             /* Clean, light */
--font-accent: 'Montserrat', sans-serif     /* Labels, buttons */
```

### Visual Style
- Soft, nature-inspired
- Generous whitespace
- Rounded corners
- Subtle animations
- Calming imagery (water, flowers, stones)

---

## 3.2 Layout Specifications

### Hero
- **Style**: Full-width serene image, soft overlay
- **Content**:
  - Elegant headline
  - "Descubre la tranquilidad"
  - CTA: "Reservar" + "Ver Tratamientos"

### Treatment Cards
- **Layout**: 3-column grid
- **Design**: Image, name, price range, "Ver más"

### Package Banner
- **Style**: Full-width, background image with overlay
- **Content**: Package name, included treatments, price, savings %

### About Section
- **Layout**: Image + text split
- **Content**: Spa story, philosophy, certifications

---

# 4. UÑAS (NAIL SALON) TEMPLATE

## 4.1 Visual Identity

### Color Palette - "Chic Minimal"
```
--primary: #1a1a1a         /* Charcoal */
--secondary: #e8c4c4       /* Blush pink */
--accent: #d4af37          /* Gold */
--background: #fafafa     /* Off-white */
--surface: #ffffff         /* White */
--text: #333333            /* Dark gray */
--text-light: #777777      /* Medium gray */
--highlight: #ff9eb5       /* Hot pink accents */
```

### Typography
```
--font-heading: 'Playfair Display', serif   /* Elegant */
--font-body: 'Montserrat', sans-serif     /* Modern */
--font-accent: 'Cormorant Garamond', serif /* Artistic */
```

### Visual Style
- Clean, gallery-like
- Focus on nail art imagery
- Trendy, fashion-forward
- Bold typography
- High contrast sections

---

## 4.2 Gallery Structure

### Masonry Layout
- **Columns**: 4 (desktop), 3 (tablet), 2 (mobile)
- **Categories**: Natural, Gel, Acrylic, Art, Bridal
- **Hover**: Zoom effect, category tag appears

### Nail Art Cards
- Image (square or 4:5)
- Style category tag
- Price indicator (optional)

---

# 5. TATUAJES/PIERCING TEMPLATE

## 5.1 Visual Identity

### Color Palette - "Dark Studio"
```
--primary: #0a0a0a         /* Near black */
--secondary: #ffffff       /* White */
--accent: #c9a227          /* Gold */
--background: #111111      /* Dark background */
--surface: #1a1a1a         /* Card background */
--text: #e0e0e0            /* Light gray text */
--text-muted: #888888      /* Muted text */
--highlight: #ff4444       /* Red accent (optional) */
```

### Typography
```
--font-heading: 'Oswald', sans-serif    /* Bold, impactful */
--font-body: 'Roboto', sans-serif       /* Clean, readable */
--font-accent: 'Bebas Neue', sans-serif /* Display */
```

### Visual Style
- Dark theme (industry standard)
- Portfolio-first design
- Artistic, edgy
- Minimal text, maximum imagery
- High contrast

---

## 5.2 Portfolio Structure

### Artist Tabs
- Tab per artist
- Each tab shows artist's work only
- Filter by style

### Image Modal
- Full-screen viewing
- Next/previous navigation
- Artist credit overlay

---

# 6. BARBERÍA TEMPLATE

## 6.1 Visual Identity

### Color Palette - "Classic Sharp"
```
--primary: #1a1a1a         /* Black */
--secondary: #c9a227       /* Gold */
--accent: #ffffff         /* White */
--background: #0d0d0d      /* Near black */
--surface: #1f1f1f         /* Dark gray */
--text: #ffffff            /* White text */
--text-muted: #aaaaaa      /* Gray text */
--barber-pole: #bf0a30     /* Classic red accent */
```

### Typography
```
--font-heading: 'Oswald', sans-serif     /* Strong, masculine */
--font-body: 'Montserrat', sans-serif   /* Clean */
--font-accent: 'Playfair Display', serif /* Vintage touches */
```

### Visual Style
- Classic barbershop aesthetic
- Dark with gold accents
- Sharp, geometric
- Vintage touches optional
- "Grooming" feel

---

## 6.2 Design Elements

### Portfolio Grid
- 3-column grid
- Real cut photos (critical - no stock)
- Before/after pairs

### Service Menu
- Traditional list style
- Clear prices
- Duration estimates
- "Walk-in welcome" badge if applicable

---

# 7. ESTÉTICA/FACIAL TEMPLATE

## 7.1 Visual Identity

### Color Palette - "Clinical Luxury"
```
--primary: #1a2744         /* Deep navy */
--secondary: #c9a227      /* Gold */
--accent: #e8f4f8          /* Light blue */
--background: #f8f9fa      /* Clean white */
--surface: #ffffff         /* White */
--text: #2c3e50            /* Dark blue-gray */
--text-light: #7f8c8d      /* Medium gray */
--medical: #3498db         /* Blue for medical elements */
```

### Typography
```
--font-heading: 'Montserrat', sans-serif  /* Clean, professional */
--font-body: 'Open Sans', sans-serif      /* Readable */
--font-accent: 'Cormorant Garamond', serif /* Elegant touches */
```

### Visual Style
- Professional, clinical but warm
- Trust-building design
- Before/after prominent
- Credentials showcased
- Clean, scientific feel

---

## 7.2 Trust Elements

### Credentials Display
- Certifications badges
- Before/after gallery (prominent)
- Reviews/star ratings
- "Medical director" titles
- Years of experience

### Treatment Info
- Detailed descriptions
- "Science behind" section
- Safety information
- Recovery time

---

# 8. MAQUILLAJE TEMPLATE

## 8.1 Visual Identity

### Color Palette - "Editorial Glam"
```
--primary: #1a1a1a         /* Black */
--secondary: #d4af37        /* Gold */
--accent: #ff9eb5          /* Pink */
--background: #faf9f7      /* Soft white */
--surface: #ffffff         /* White */
--text: #333333            /* Dark gray */
--text-light: #666666      /* Gray */
--glam: #c0c0c0            /* Silver accents */
```

### Typography
```
--font-heading: 'Playfair Display', serif   /* Editorial */
--font-body: 'Montserrat', sans-serif       /* Clean */
--font-accent: 'Cormorant Garamond', serif /* Artistic */
```

### Visual Style
- Editorial, fashion magazine feel
- Large imagery
- Elegant, sophisticated
- Portfolio-driven
- Bridal focus for weddings

---

## 8.2 Portfolio Focus

### Gallery Categories
- Bridal
- Editorial
- Special Event
- Makeup Lesson

### Before/After
- Side-by-side comparison
- Transformation showcase
- Filter by look type

---

# 9. DEPILACIÓN TEMPLATE

## 9.1 Visual Identity

### Color Palette - "Clinical Clean"
```
--primary: #2c3e50         /* Dark slate */
--secondary: #3498db       /* Medical blue */
--accent: #1abc9c          /* Teal */
--background: #f8f9fa      /* Clean white */
--surface: #ffffff         /* White */
--text: #333333            /* Dark gray */
--text-light: #7f8c8d      /* Gray */
--trust: #27ae60           /* Green for safety */
```

### Typography
```
--font-heading: 'Montserrat', sans-serif  /* Professional */
--font-body: 'Open Sans', sans-serif      /* Clear */
--font-accent: 'Lato', sans-serif        /* Labels */
```

### Visual Style
- Clinical, professional
- Clean, medical feel
- Trust-focused
- Technology highlights
- Safety prominent

---

## 9.2 Key Elements

### Technology Showcase
- Equipment images
- "FDA Approved" badges
- "Painless" highlights
- "All skin types" indicator

### Consultation CTA
- "FREE consultation" prominent
- Skin type quiz (optional)
- Treatment preview tool

---

# COMPONENT LIBRARY SUMMARY

## Universal Components
| Component | Variants | States |
|-----------|----------|--------|
| Button | Primary, Secondary, Outline, Ghost | Default, Hover, Active, Disabled |
| Card | Service, Team, Pricing, Feature | Default, Hover, Selected |
| Input | Text, Textarea, Select, Checkbox | Default, Focus, Error, Disabled |
| Modal | Image, Form, Confirmation | Open, Closing |
| Nav | Desktop, Mobile, Sticky | Expanded, Collapsed |
| Footer | Standard, Minimal | - |
| Hero | Image, Video, Split | - |
| Gallery | Grid, Masonry, Slider | - |
| Form | Contact, Booking, Consultation | Valid, Invalid, Submitting |

## Category-Specific Components
| Category | Special Components |
|----------|---------------------|
| Hair Salon | Stylist calendar, Hair color chart |
| Gym | Class schedule, Membership comparison, Trainer booking |
| Spa | Treatment package builder, Duration calculator |
| Nails | Nail art filter, Style categories |
| Tattoo | Style filter, Consultation form, Aftercare accordion |
| Barber | Cut style showcase, Barber availability |
| Aesthetic | Before/after slider, Treatment quiz |
| Makeup | Look categories, Trial booking |
| Hair Removal | Area pricing table, Skin type selector |

---

*Template specifications created: April 2026*