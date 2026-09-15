# Two-Reference Playbook Catalog

Read this after `workflow.md` and before `template-router.md`. It borrows the card, tag, guidance, and pitfall structure from a style library, but each card is specialized for role-separated visual references.

## How to choose

1. Identify the highest-risk variable: identity, age/face, geometry/perspective, light and location, material texture, product shape, narrative readability, or text/layout.
2. Assign references by variable:
   - **A** controls geometry, crop, camera position, subject scale, layout, and hierarchy.
   - **B** controls light, palette, material, rendering medium, camera finish, and atmosphere.
   - **C** is optional and must have one narrow job: identity/age anchor, skin/hair texture, logo/prop, key material, or another non-overlapping anchor.
3. If the user already accepted a draft and asks for a correction, use that draft as the edit or identity anchor. Do not replace an accepted face while fixing light, texture, or background.
4. Choose one primary playbook. Use a second only when it controls a clearly separate risk.
5. Map the playbook to one template ID in `template-router.md`.

| Playbook | Use for | Typical template mapping |
|---|---|---|
| `realistic-portrait` | Photoreal people, beauty, lifestyle portraits | `realistic-photography` |
| `candid-street-documentary` | Street life, documentary moments, candid action | `street-accident-moment` or `realistic-photography` |
| `product-material` | Product hero, packaging, material and surface study | `product-commerce-visual` |
| `architecture-interior` | Interior, exterior, spatial rendering | `architecture-space` |
| `narrative-scene` | Key art, cinematic environment, story moment | `scene-storytelling` |
| `character-consistency` | Turnarounds, costume sheets, recurring character | `character-design-sheet` |
| `poster-hero-composition` | Poster/cover hierarchy with a dominant visual | `poster-layout-system` |
| `concept-product-breakdown` | Exploded product, functional callouts, invention visual | `concept-product-breakdown` |

## Playbook cards

### `realistic-portrait`

Use when the asset is a believable photograph of a person, especially close-ups, beauty, fashion-lifestyle, or portraits with age and identity sensitivity.

- **A — composition and age:** camera distance, head/shoulder crop, eye placement, gaze, expression, face proportions, and visual age. Prefer an original generated reference or the user's accepted draft; do not clone a real person's identity.
- **B — light and place:** practical window/daylight, location context, camera color, lens depth of field, and ambient atmosphere.
- **C / anchor — surface or identity:** use an accepted draft to lock identity/age, or a separate unretouched photo only for skin, eyebrow/eyelash fibers, flyaway hair, and fabric texture.
- **Prompt modules:** camera/lens, light direction, real location, adult age when relevant, natural makeup, skin structure, everyday clothing, slight handheld imperfection.
- **Pitfalls:** plastic skin, beauty-filter smoothing, studio rim light, dreamy bokeh, age drift, school uniform for youthful portraits, sexualization, copied celebrity face, and replacing the accepted face during a texture pass.
- **QA:** real-camera feel, clearly intended age, identity continuity, skin and hair detail, coherent eye light, anatomy, and absence of child-coded/sexualized cues.

For detailed cues, read `realistic-portrait-photography.md`.

### `candid-street-documentary`

Use when the image needs a decisive public-life moment, documentary phone/camera photo, candid interaction, weather on the street, or realistic action in a city environment.

- **A — moment and geometry:** camera height, subject distance, action peak, foreground/midground/background layers, motion path, and negative space.
- **B — documentary surface:** daylight or practical night light, weather, street color, grain, lens character, and local environmental texture.
- **C / anchor — prop or place:** use only for a specific vehicle, signage style, clothing detail, or location element that must remain consistent.
- **Prompt modules:** exact moment, camera height, motion blur amount, plausible street context, pedestrian scale, practical light, documentary color.
- **Pitfalls:** staged advertising poses, fake heroic rim light, overly clean streets, impossible motion, unsafe or implausible accidents, unreadable random signage, and copying a recognizable photographer's composition.
- **QA:** action peak is readable, bodies and vehicles are physically plausible, light direction matches shadows, scale is coherent, and the scene does not look like a staged poster unless requested.

### `product-material`

Use for product hero images, packaging, e-commerce detail shots, material studies, and images where shape accuracy and surface response are the main risks.

- **A — shape and layout:** product silhouette, hero angle, crop, scale, label area, supporting props, and negative space.
- **B — surface and light:** key/fill/rim direction, material response, background, contact shadow, color palette, and commercial or candid finish.
- **C / anchor — exact asset:** user-owned logo, packaging artwork, material macro, or prior accepted product draft.
- **Prompt modules:** product geometry, dimensions/silhouette, material, finish, label constraints, surface imperfections if appropriate, prop scale, shadow contact.
- **Pitfalls:** changed product shape, invented buttons or packaging, random props, floating shadows, glossy plastic overreach, fake branding, and tiny illegible text.
- **QA:** shape fidelity, label/logo correctness, readable text, material response under one coherent light, contact shadows, and no unrelated props.

### `architecture-interior`

Use for interiors, exteriors, furniture layouts, real-estate-style views, and spatial concepts.

- **A — space and perspective:** viewpoint, lens feel, vanishing points, room depth, circulation path, furniture placement, and subject scale.
- **B — material and atmosphere:** daylight direction/time, lamp practicals, wall/floor/metal/fabric finishes, palette, weather, and mood.
- **C / anchor — fixture or material:** specific furniture piece, material swatch, window design, or accepted spatial draft.
- **Prompt modules:** camera position, focal length feel, architectural style, time of day, light source, material list, human scale cues, functional layout.
- **Pitfalls:** warped lines, impossible rooms, mismatched scale, floating furniture, contradictory window and lamp light, over-decorated spaces, and distorted repeated patterns.
- **QA:** perspective and parallax are coherent, materials react correctly, light sources agree, circulation is believable, and people/props have correct scale.

### `narrative-scene`

Use for cinematic key art, story moments, environmental storytelling, fantasy/sci-fi scenes, and images where a situation must read at thumbnail size.

- **A — story geometry:** protagonist scale, camera angle, foreground/background relationship, conflict, sight lines, path of motion, and dominant shape.
- **B — world surface:** time, weather, light direction, color script, atmosphere, lens/finish, and medium.
- **C / anchor — key element:** specific creature, vehicle, weapon, prop, costume, or previously accepted environment.
- **Prompt modules:** protagonist objective, immediate event, location, era/world rules, key prop, depth layers, light as story cue, lens and finish.
- **Pitfalls:** too many events, several equally bright focal points, inconsistent era, contradictory weather, scale mistakes, generic concept-art haze, and copying a protected film frame.
- **QA:** one clear story beat, readable focal hierarchy, coherent world rules, scale and perspective, and lighting that guides the eye.

### `character-consistency`

Use for original character sheets, turnarounds, costume variants, and recurring character work where the same identity must survive multiple views.

- **A — sheet geometry:** view count, neutral pose, turnaround order, full-body/half-body crop, alignment, and negative space.
- **B — costume and render surface:** fabric, armor, material, palette, lighting style, outline/brush language, and finish.
- **C / anchor — identity:** accepted face/character draft or user-owned character reference.
- **Prompt modules:** same face and body proportions, age/species, expression range, costume inventory, consistent accessories, neutral background, view labels only if requested.
- **Pitfalls:** different face per view, changing height or age, random costume pieces, overlapping views, inconsistent material, and using a known IP character as identity.
- **QA:** facial landmarks match, proportions repeat, accessories are tracked, material is consistent, and all views have coherent lighting and scale.

### `poster-hero-composition`

Use when a poster, cover, campaign key visual, or social hero needs strong hierarchy and a dominant image. This card controls composition; exact typography may need a dedicated design route.

- **A — layout skeleton:** aspect ratio, title safe area, hero placement, horizon, visual flow, copy space, and margin.
- **B — campaign surface:** light, color grade, palette, material, mood, lens/illustration finish, and contrast.
- **C / anchor — brand asset:** user-owned logo, product, character, or approved campaign element.
- **Prompt modules:** exact headline text, hierarchy, hero scale, background depth, palette, placement constraints, safe margins, and output aspect ratio.
- **Pitfalls:** moodboard/collage output, multiple heroes, fake logos, misspelled words, unreadable type, decorative clutter, and letting B override the layout.
- **QA:** headline legibility, one dominant subject, correct aspect ratio, safe margins, no extra text/logos, and composition that leaves usable space.

### `concept-product-breakdown`

Use for invented products, exploded views, mechanical callouts, technical hero renders, and functional diagrams that still need a polished raster finish.

- **A — breakdown structure:** exploded axis, part order, assembly direction, callout slots, spacing, and camera angle.
- **B — technical surface:** studio or practical light, material finish, edge quality, background, color coding, and render grain.
- **C / anchor — product identity:** prior accepted product draft, user-owned CAD/render, or specific material/part reference.
- **Prompt modules:** product purpose, named parts, exploded direction, connectors, materials, callout style, labels only when provided, scale cues.
- **Pitfalls:** impossible mechanisms, duplicated parts, random labels, fake UI text, unclear assembly direction, and decorative explosions that hide function.
- **QA:** each part is identifiable, assembly direction is coherent, connectors align, labels are short and correct, and scale/material stay consistent.

## Deliberately excluded

Do not force these into a role-separated bitmap workflow unless visual references clearly add value:

- UI screenshots and dashboards;
- dense infographics and documents;
- logos, icons, and simple vector marks;
- exact text-heavy layouts;
- deterministic charts or diagrams.

Prefer code-native, vector, presentation, document, or dedicated UI workflows for those outputs.
