# Two-Reference Workflow

## 1. Intake and role audit

Identify the pair:

| Reference | Primary job | Allowed signals | Ignored signals |
|---|---|---|---|
| A | Composition | camera angle, framing, subject scale, placement, crop, negative space, foreground/midground/background, visual flow, hierarchy | color grade, exact object, logo, character, brand, texture |
| B | Style and atmosphere | lighting direction/quality, palette, material, rendering medium, surface detail, lens mood, illustration/photo/3D language | layout, exact subject, pose unless separately requested, text, brand marks |

If one image is strong at both layout and style, split it deliberately:

- use its geometry as A only;
- use a second image for B;
- explicitly tell the model not to transfer the first image's subject or palette.

## 2. Rights and originality check

Note the usage context without giving legal advice:

- Personal experimentation: lower practical risk, but outputs should still avoid direct duplication.
- Client/commercial/public work: require owned, licensed, public-domain/CC-compatible references, or sufficiently abstracted rules.
- Likes/saves/reposts are not licenses.
- Avoid exact logos, characters, watermarks, campaign layouts, unique products, and recognizable people unless the user has appropriate rights.

When rights are unclear, use generalized observations such as "centered hero composition with left negative space" rather than "recreate this image".

## 3. Abstract the references

Write observations as reusable rules.

### Reference A composition extraction

- Shot/framing: close-up, wide, macro, over-shoulder, top-down, isometric, etc.
- Subject placement: center, rule-of-thirds, low horizon, dominant foreground, etc.
- Depth and layers: foreground frame, background separation, leading lines.
- Negative space: where copy or UI can live.
- Visual hierarchy: what is largest, sharpest, brightest, or most contrasted.
- Geometry: horizontal, diagonal, radial, symmetrical, fragmented.

### Reference B style extraction

- Light: soft/hard, warm/cool, rim, backlight, studio, natural, chiaroscuro.
- Palette: dominant 1–2 colors, accent color, saturation, contrast.
- Material: matte, glossy, glass, metal, ceramic, fabric, skin, paper, plastic.
- Medium: photorealistic, editorial photo, 3D render, collage, ink, vector-like illustration, etc.
- Finish: grain, bloom, shallow depth of field, clean CGI, analog texture.
- Mood: calm, luxurious, playful, tense, clinical, nostalgic, futuristic.

## 4. First generation batch

Default to four variants with one shared contract:

1. **Balanced** — follow A and B equally.
2. **Composition-first** — stronger obedience to A; B is subtler.
3. **Style-first** — stronger lighting/material transfer; keep A recognizable.
4. **Editorial wildcard** — one controlled change in lens, palette, or material without changing layout.

Generate one variant per tool call when the host's image tool creates one image per invocation. Save project-relevant outputs into the current workspace.

## 5. Selection scorecard

Score each variant from 1–5:

- composition match to A;
- style match to B;
- originality and absence of copied protected elements;
- subject clarity and correct anatomy/object structure;
- lighting/material coherence;
- text accuracy, when text is requested;
- fitness for the intended crop and use context.

Pick a winner by total fit, not by the prettiest unrelated image.

## 6. Refinement passes

Use one lever at a time:

- **Composition-locked:** keep A geometry, improve subject, expression, props, or perspective.
- **Style-locked:** keep palette/light/material, correct layout drift.
- **Local edit:** replace/remove one object, fix text, change background, or adjust material.
- **Finish pass:** add grain, contrast, sharpness, or background cleanup without changing content.

If layout consistently fails, raster prompting is insufficient; recommend a structure-control workflow or a code-native wireframe/sketch.
