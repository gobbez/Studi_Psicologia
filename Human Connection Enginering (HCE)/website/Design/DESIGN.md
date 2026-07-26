---
name: Psyche Flow
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c7c4d8'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#908fa1'
  outline-variant: '#464556'
  surface-tint: '#c1c1ff'
  primary: '#c1c1ff'
  on-primary: '#1500a8'
  primary-container: '#5d5cff'
  on-primary-container: '#fdf9ff'
  inverse-primary: '#4643e9'
  secondary: '#44e2cd'
  on-secondary: '#003731'
  secondary-container: '#03c6b2'
  on-secondary-container: '#004d44'
  tertiary: '#ddb7ff'
  on-tertiary: '#490080'
  tertiary-container: '#9a46e9'
  on-tertiary-container: '#fff8fd'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1dfff'
  primary-fixed-dim: '#c1c1ff'
  on-primary-fixed: '#09006b'
  on-primary-fixed-variant: '#2b20d2'
  secondary-fixed: '#62fae3'
  secondary-fixed-dim: '#3cddc7'
  on-secondary-fixed: '#00201c'
  on-secondary-fixed-variant: '#005047'
  tertiary-fixed: '#f0dbff'
  tertiary-fixed-dim: '#ddb7ff'
  on-tertiary-fixed: '#2c0051'
  on-tertiary-fixed-variant: '#6900b3'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  stack-gap: 32px
---

## Brand & Style

The design system is centered on the concept of "Introspective Discovery." It balances the clinical authority of psychology with the immersive, dopamine-driven engagement of modern gaming. The target audience includes curious self-learners and wellness enthusiasts seeking insights through interactive media.

The visual style is **Glassmorphism**, utilizing translucent layers and vibrant background blurs to suggest depth and mental clarity. By layering "frosted" surfaces over organic, shifting gradients, the UI evokes a sense of fluid consciousness and modern sophistication. Interactions are designed to feel tactile and high-fidelity, ensuring the quiz experience feels like a journey rather than a test.

## Colors

The palette uses a deep indigo base to establish a "night mode" environment that reduces eye strain and enhances focus. 

- **Primary (Vibrant Violet):** Used for key actions and progress indicators to provide the "wow" factor.
- **Secondary (Soft Teal):** Reserved for success states, secondary insights, and highlighting positive traits.
- **Tertiary (Electric Purple):** Used sparingly for high-level interactive elements and rare "achievement" moments.
- **Neutral (Deep Space):** A dark navy-blue foundation that provides better contrast for glass effects than pure black.

Backgrounds should utilize a slow-moving linear gradient between the neutral and primary shades to maintain visual interest without distracting from the content.

## Typography

The typography strategy prioritizes readability and impact. **Montserrat** is used for headlines to provide a geometric, confident, and "designed" feel that resonates with a premium digital experience. **Inter** is utilized for body copy and UI labels because of its exceptional legibility and systematic tone, ensuring complex psychological descriptions are easy to digest.

Text should rarely be pure white; use a high-opacity tint of the secondary or primary color (e.g., 90% white with a hint of teal) to ensure it sits harmoniously within the glassmorphic containers.

## Layout & Spacing

The layout follows a **fluid grid** model with a maximum content width of 1200px for desktop. On mobile, margins are reduced to 16px to maximize screen real estate for immersive questions.

Spacing follows an 8px rhythmic scale. Quiz questions are centered vertically and horizontally in the viewport to minimize peripheral distractions. Use generous white space (or "clear space") around glass panels to allow the background gradients and blurs to frame the content effectively.

## Elevation & Depth

Depth is communicated through **Glassmorphism** and ambient shadows. 

1.  **Base Layer:** A deep indigo gradient.
2.  **Mid Layer (Glass Panels):** 40% opacity white with a 20px Backdrop Blur and a subtle 1px white border (10% opacity) to define the edge.
3.  **Active Layer (Cards/Buttons):** 60% opacity with an increased backdrop blur and a vibrant outer glow using the primary or secondary color.

Shadows are not black; they are deep indigo with 40% opacity, spread wide (30px-50px) to create a soft, "floating" effect rather than a harsh drop.

## Shapes

The design system uses **Rounded (0.5rem base)** corner radii. This strikes a balance between professional software and approachable gaming. 

- **Cards and Quiz Containers:** Use `rounded-xl` (1.5rem) to feel friendly and modern.
- **Buttons and Inputs:** Use `rounded-lg` (1rem) for a distinct, clickable appearance.
- **Selection Indicators:** Small decorative elements may use full pill-shapes to indicate status without adding visual bulk.

## Components

### Buttons
Primary buttons use a vibrant gradient from Primary to Tertiary. They feature a "hover-glow" effect where the box-shadow expands when hovered. Secondary buttons should be glass-styled with a clear white border.

### Quiz Cards
Questions are housed in large, semi-transparent glass panels. Interaction should be animated; when an answer is selected, the card should "pulse" with the secondary teal color before transitioning to the next screen.

### Progress Bars
The progress bar is a slim, glowing line at the top of the viewport. Use a gradient fill (Teal to Violet) that grows as the user completes the quiz, creating a sense of momentum.

### Chips & Tags
Used for personality traits or categories. These should be low-opacity "pills" with colored text matching the trait's category, ensuring they don't compete with the primary call-to-action.

### Input Fields
Inputs are minimal glass fields. On focus, the 1px border should animate to a 2px Primary color border with a subtle inner glow, signaling that the "system" is listening.