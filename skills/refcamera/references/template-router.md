# GPT-Image-2 Template Router

First use [`playbook-catalog.md`](playbook-catalog.md) to classify the job and assign role-separated references. This router maps that playbook to a compact prompt template after A/B/C roles are clear.

Choose one primary template. This is a compact routing layer inspired by the installed `gpt-image-2-style-library`; read that full reference for long-tail cases.

| User intent | Template ID | Lock tightly |
|---|---|---|
| App screen, dashboard, social UI, live interface mockup | `ui-screenshot-system` | platform, aspect ratio, UI hierarchy, exact visible text |
| Explainer, process diagram, timeline, knowledge card | `infographic-engine` | 3–5 modules, flow direction, short labels, icon/arrow language |
| Micro-to-macro or scientific scale comparison | `scientific-scale-diagram` | 6–8 scale frames, units, distinct detail levels |
| Event poster, cover, campaign visual, social poster | `poster-layout-system` | subject, headline, layout, palette, aspect ratio |
| Athlete, sport product, dramatic sports campaign | `sports-campaign-poster` | sport, pose, hero prop, title, dramatic light |
| Title typography is the main visual | `conceptual-typography-poster` | exact title, type-as-structure, restrained palette |
| Poetic Chinese/ink portrait or cultural atmosphere | `ink-double-exposure-poster` | silhouette, ink texture, negative space, quiet premium mood |
| Nature/science poster with a clean educational feel | `nature-science-poster` | clear subject, short labels, whitespace, soft shadow |
| E-commerce hero, packaging, product detail, sales visual | `product-commerce-visual` | product shape, selling points, materials, scene, text blocks |
| Personalized beauty/skincare report visual | `personalized-beauty-report` | report structure, personal data framing, clean premium beauty styling |
| Logo, brand system, brand board, identity package | `brand-identity-package` | brand attributes, mark construction, typography, restrained palette |
| Multiple brand touchpoints in one presentation | `brand-touchpoint-board` | item list, grid, consistent identity, label hierarchy |
| Interior, architecture, spatial rendering | `architecture-space` | viewpoint, materials, scale, light source, spatial function |
| Realistic lifestyle or editorial photograph | `realistic-photography` | lens feel, natural light, texture, candid composition |
| Decisive street moment or accident scene | `street-accident-moment` | action peak, safety/context, realistic perspective |
| General illustration, painterly or graphic art | `illustration-art-style` | medium, line/shape language, color, texture |
| Character turnaround or setting sheet | `character-design-sheet` | views, proportions, costume, expression, neutral background |
| Designer toy, blind-box figure, collectible render | `3d-collectible-toy` | silhouette, material, base, turnaround or hero angle |
| Narrative environment or key-art scene | `scene-storytelling` | protagonist cue, setting, conflict, light, foreground/background |
| Historical, classical, ancient-world topic | `history-classical-themes` | period accuracy, costume, architecture, props |
| Book/document layout, report cover, publication graphic | `document-publishing` | page grid, typography hierarchy, readable copy |
| Product invention, exploded view, technical breakdown | `concept-product-breakdown` | parts, callouts, materials, function labels |

## Selection order

1. Match the output artifact first: UI, poster, product, infographic, character, scene, or document.
2. Match the visual style second: realistic, 3D, illustration, classical, infographic.
3. Match the context third: commerce, education, social, tech, travel, food, history, or creative.
4. If two templates are plausible, choose the one that controls the highest-risk element. For example, a poster with complex data uses `infographic-engine`; a data graphic with strong campaign typography uses `poster-layout-system`.

## Template-specific non-negotiables

- UI and documents: exact text, platform, grid, and hierarchy.
- Posters: headline legibility and one dominant visual.
- Products: accurate shape and material; no random props that confuse the product.
- Infographics: short labels and a small module count.
- Characters: keep identity consistent across views.
- Historical/scientific topics: prioritize factual constraints over decoration.
