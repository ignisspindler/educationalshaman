# educationalshaman.com — Site Specification

## 1. Concept & Vision

A site for a transformational learning guide who bridges scientific rigor and spiritual depth. The experience should feel like stepping into a warm, illuminated space—part observatory, part sanctuary. Visitors should feel seen, curious, and quietly energized. The tone is intellectual but not cold; spiritual but not woo-woo.

## 2. Design Language

**Aesthetic Direction:** "Illuminated Pathway" — think a warm lantern through a forest at dusk. Light emerging from within darkness. The contrast between deep, contemplative backgrounds and radiant, warm focal points.

**Color Palette:**
- Background: `#0d1117` (deep night sky)
- Surface: `#161b22` (elevated card surfaces)
- Primary: `#c9a227` (warm gold — illumination, value)
- Accent: `#e07b39` (ember orange — warmth, transformation)
- Gradient: `#c9a227` → `#e07b39` → `#8b2fc9` (gold to ember to violet for depth)
- Text: `#f0f0f0` (warm white), `#a8a8a8` (muted secondary)
- Border: `#2d333b`

**Typography:**
- Headings: **Playfair Display** (elegant, scholarly gravitas)
- Body: **Inter** (clean, highly readable)
- Accent/Labels: **Cormorant Garamond** (spiritual, refined italic moments)

**Spatial System:**
- 8px base unit, generous whitespace
- Sections breathe — 120px vertical padding between major sections
- Content max-width: 1100px, centered

**Motion Philosophy:**
- Entrance animations: fade-up on scroll (200ms ease-out, staggered 80ms)
- Subtle glow pulses on CTA buttons
- Parallax on hero background (light rays)
- Hover states: gentle scale (1.02) + warm shadow lift

**Visual Assets:**
- Icons: Phosphor Icons (duotone style)
- Images: Gemini-generated hero imagery evoking transformation, light, journey
- Decorative: radial gradient glows, subtle starfield pattern on hero

## 3. Layout & Structure

**Hero Section**
- Full-viewport with radial gradient background + starfield
- Bold headline + subheadline
- CTA button with warm glow
- Floating geometric shapes suggesting pathways/layers

**About Section**
- Photo placeholder + narrative bio
- The 7-question journey as a visual timeline
- Eugene's credentials displayed as elegant badges

**Services Section**
- 3 coaching packages as cards with hover effects
- Price, duration, what's included

**Process Section**
- The 7 questions as an interactive accordion or stepped journey
- Each question reveals guidance on what it unlocks

**Testimonials Section**
- Rotating quote carousel
- Warm gradient background

**Contact/Conversion Section**
- Simple form: name, email, what brings you here
- Strong CTA to book discovery call

**Footer**
- Minimal, warm, with social links

## 4. Features & Interactions

**Navigation:**
- Sticky top nav, blurs on scroll
- Smooth scroll to sections
- Mobile hamburger menu

**Hero:**
- Parallax starfield background
- Animated headline entrance
- Floating geometric accents

**7-Question Journey (Process):**
- Cards expand to reveal the transformational question + explanation
- Shows how each question leads to the next

**Services Cards:**
- Hover: lift + glow border
- Click: expand to full package details

**Contact Form:**
- Validation feedback
- Success state with warm confirmation message

**Scroll Animations:**
- Elements fade-up on viewport entry
- Staggered reveals for lists/grids

## 5. Component Inventory

**Button (Primary):**
- Default: gold gradient bg, dark text, rounded-lg
- Hover: scale(1.03), brighter glow
- Active: scale(0.98)
- Disabled: 50% opacity

**Card (Service):**
- Default: dark surface, subtle border
- Hover: gold border glow, slight lift
- Contains: icon, title, price, feature list, CTA

**Accordion (Process Steps):**
- Default: collapsed, shows step number + question preview
- Active/Open: reveals full question + guidance text
- Transition: 300ms ease

**Input Field:**
- Default: dark bg, subtle border
- Focus: gold border + glow
- Error: red border + message below

**Quote Carousel:**
- Auto-rotates every 5s
- Manual dots for navigation
- Fade transition between quotes

## 6. Technical Approach

- **Single HTML file** (index.html) with embedded CSS/JS for simplicity
- Vanilla JS for interactions (no framework needed)
- CSS custom properties for theming
- Google Fonts: Playfair Display, Inter, Cormorant Garamond
- Phosphor Icons via CDN
- Fully responsive (mobile-first breakpoints: 768px, 1024px)