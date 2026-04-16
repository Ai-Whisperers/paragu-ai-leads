# Dayah Lit Works - Service Budget Page

> Source content for the page rendered at `paragu-ai-builder.pages.dev/dayah-litworks`.
> Spanish (original) copy is the source of truth; English notes are for reference only.

---

## Brand

| Field | Value |
|---|---|
| Business Name | Dayah Lit Works |
| Owner | Dayah Araujo |
| Role | Book Cover Designer |
| Vertical | Creative services / book cover design & interior layout |
| Working Days | Monday - Friday (business days) |
| Default Delivery | 2 to 4 weeks (to be defined with client) |

### Tagline
- ES: "Diseño de portadas y maquetación para tu libro."
- Header line used in source PDF: "PRESUPUESTO DE SERVICIOS - DAYAH ARAUJO - BOOK COVER DESIGNER"

---

## Service Packages

All prices are in USD. All projects share the same delivery window (2-4 weeks, to be defined with client).

### Custom Covers

#### 1. Portada Digital - eBook - $40 USD
Detalles del proyecto:
- Portada de libro electronico (JPG/PDF)
- Titulo en formato PNG y Portadilla PNG
- 2 banners de revelacion de portada
- 2 mockups

#### 2. Portada Paperback - $60 USD
Detalles del proyecto:
- Portada de libro tapa blanda (JPG/PDF)
- Archivo imprimible (PDF)
- Titulo en formato PNG y Portadilla PNG
- 2 banners de revelacion de portada
- 2 mockups

#### 3. Portada Paperback & eBook - $80 USD
Detalles del proyecto:
- Portada de libro electronico (JPG/PDF)
- Archivo imprimible (PDF)
- Titulo en formato PNG y Portadilla PNG
- 2 banners de revelacion de portada
- 2 mockups

### Premade Covers

> Premades se trabajan desde:
> - Alteraciones en redaccion y tipografias
> - Cambios de color especificos
> - Cambios menores en la posicion de los elementos

#### 4. Premade eBook - $30 USD
Detalles del proyecto:
- Portada de libro electronico (JPG/PDF)
- Titulo en formato PNG y Portadilla PNG
- 2 banners de revelacion de portada
- 2 mockups

#### 5. Premade eBook & Paperback - $50 USD
Detalles del proyecto:
- Portada de libro tapa blanda (JPG/PDF)
- Archivo imprimible (PDF)
- Titulo en formato PNG y Portadilla PNG
- 2 banners de revelacion de portada
- 2 mockups

### Interior Layout (Maquetacion)

#### 6. Maquetacion eBook - $15 USD
Detalles del proyecto:
- Diseno interior
- Entrega del archivo segun especificaciones de la plataforma (WORD/PDF)

#### 7. Maquetacion Paperback - $25 USD
Detalles del proyecto:
- Diseno interior
- Entrega del archivo segun especificaciones de la plataforma (PDF)

#### 8. Maquetacion eBook & Paperback - $40 USD
Detalles del proyecto:
- Diseno interior
- Entrega del archivo segun especificaciones de la plataforma (WORD/PDF)

### Standard Disclaimer (shown on every package)

> Tiempo estimado total: a definir con el cliente. Estimado de 2 a 4 semanas.
>
> Obs.: Los detalles del proyecto pueden ser modificados por el cliente.
> El costo del presupuesto podria sufrir variaciones en base a un plan
> predefinido, dependiendo de las modificaciones establecidas.

---

## Conditions of Service (Condiciones de ambas partes)

> El pago del presupuesto lleva implicito su aceptacion y el cumplimiento
> de los siguientes items.

1. **Referencias previas.** Recuerda siempre de mandarme referencias de
   ideas, tipografias, colores o estilos que tengas antes de solicitar el
   diseno, no despues de enviar la propuesta terminada.
2. **Dias habiles.** Se realizara el trabajo en dias habiles (lunes a
   viernes), el tiempo suficiente acordado para entregar una pieza de
   calidad.
3. **No reembolso.** Si una vez iniciado el proyecto el cliente decidiera
   rescindir el contrato y no seguir trabajando con Dayah LitWorks, no se
   le reembolsara el porcentaje adelantado.
4. **Revision del cliente.** El cliente adquiere la responsabilidad de
   revisar el diseno, los textos y datos antes de empezar cualquier
   proceso de impresion, reproduccion y/o publicacion, y libera a Dayah
   LitWorks de cualquier responsabilidad por los errores que se pudieran
   producir, siempre y cuando no los hubiese comunicado con anterioridad.
5. **Cambios de orientacion.** Este acuerdo no incluye los trabajos
   adicionales que se puedan derivar de los cambios de orientacion en su
   desarrollo por parte del cliente; si se diera el caso, Dayah LitWorks
   tendra que informar al cliente y podra modificar el presupuesto
   anadiendo los incrementos en el importe que se pudieran producir, pero
   manteniendo los mismos criterios de valoracion utilizados en el primer
   presupuesto.
6. **Derechos del diseno.** Los derechos del o los disenos realizados
   pertenecen a Dayah LitWorks hasta que el cliente no haya efectuado el
   100% del pago.
7. **Portfolio.** Dayah LitWorks podra mostrar, siempre que lo crea
   conveniente, los trabajos realizados en el portfolio, asi como en otras
   plataformas digitales como Instagram, Facebook, TikTok.

---

## Payment Methods (Formas de pago)

- Western Union
- Transferencias Bancarias
- Efectivo

---

## Page Composition Notes (for builder)

Section order on `/dayah-litworks` (mirrors `page-spec.json:sectionOrder`):

1. **Hero** - "Presupuesto de Servicios" + nombre/rol + delivery badge + animated cover-flip stack (static fallback for reduced-motion).
2. **Portfolio strip** - Horizontal-scroll of 8 Instagram covers (`@dayahlitworks`), 2:3 aspect ratio.
3. **Packages** - Segmented control switches between Personalizadas / Premades / Maquetacion (default: Personalizadas). Cards stagger fade-up on scroll, lift on hover. "Mas elegido" badge on Paperback+eBook ($80); "Entrega rapida" on Premade eBook. Currency toggle (USD <-> PYG) sits near the pricing header.
4. **Standard disclaimer** - Once below the pricing block.
5. **Testimonials** - Carousel; collect copy before launch.
6. **Conditions of Service** - Accordion, collapsed by default.
7. **Payment methods** - 3 icon tiles.
8. **Contact CTA** - WhatsApp primary; persistent sticky pill bottom-right (desktop) and bottom-bar (mobile) after 600px scroll.

### Visual identity (see `page-spec.json:designTokens`)
- Palette: cream `#f7f1e6` background, ink `#1a1a1a`, copper accent `#a3683f`.
- Display: Cormorant Garamond / Playfair Display. Body: Inter.
- Cards: 12px radius, soft shadow, hover lift 1px.

### Motion & accessibility
- All motion respects `prefers-reduced-motion`.
- Card entrance: 80ms stagger, fade-up 16px, 450ms ease-out.
- Page transition: 250ms fade. Smooth scroll on anchor links.
- Lighthouse target 90+, lazy-loaded images, webp/avif, font-display swap.

Spanish copy only on the public page; do not translate.
