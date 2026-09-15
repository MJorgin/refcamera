# Generation Contract

Use this internal structure for every first batch. Keep it concise enough for the image model to obey, but explicit about reference roles.

```text
Use case: <template-id>
Asset type: <where the image will be used>
Primary request: <original subject and goal>

Provider/model: <native tool / provider + model / text-only fallback>
Reference transport: <native upload / direct URL / data URL / multipart / virtual text rules>

Input images:
- Image A: <source label/URL; license/source if known>; composition/layout reference only—use camera angle, framing, subject placement, negative space, crop, and hierarchy.
- Image B: <source label/URL; license/source if known>; style reference only—use lighting, color palette, material texture, rendering medium, finish, and mood.
- Optional Image C: <object/identity/material anchor only, when needed>

Composition from A:
- <camera/framing>
- <subject placement and scale>
- <negative space / visual flow>
- <foreground/background relationship>

Style from B:
- <light direction and quality>
- <palette>
- <materials and surface finish>
- <medium and rendering texture>
- <mood>

Original subject/scene:
<describe the new subject, setting, action, and key props>

Text (verbatim):
<exact text, or “No text”>

Constraints:
- Create an original subject/scene.
- Image A controls structure; Image B controls surface style.
- Ignore people, text, watermarks, branding, exact landmarks, source-specific objects, and location identity from references unless explicitly requested.
- Do not copy logos, characters, products, watermarks, campaign text, or unique branding from either reference.
- Maintain coherent perspective, scale, and lighting.
- Keep all text exactly as specified and readable.

Avoid:
collage/moodboard look, duplicated reference subject, mixed perspective, unreadable text, watermark, extra fingers or malformed objects, visual clutter

Output:
<aspect ratio / dimensions / number of variants>
```

## Provider transport notes

- For SiliconFlow Qwen-Image-Edit-2509 JSON requests, map A/B to `image` and `image2`; add `negative_prompt` when useful and do not set `image_size` for the edit model unless current docs say otherwise.
- For Seedream-style requests, map one or multiple images according to the installed model version. Use a sanitized caller that never prints headers.
- For text-only providers, include the same role-separated rules but set `Reference transport: virtual text rules` and do not call the result a true reference-image generation.

## Variant instructions

Append one of these per variant while keeping the main contract fixed:

- `Variant 1 — Balanced: follow A and B equally.`
- `Variant 2 — Composition-first: prioritize the geometry and negative space from A; apply B more subtly.`
- `Variant 3 — Style-first: prioritize the light, palette, and material from B while retaining A's main layout.`
- `Variant 4 — Editorial wildcard: keep A's layout, but explore one different lens/material/palette choice: <controlled change>.`

## Refinement contract

For the selected variant:

```text
Edit the selected generated image.
Keep unchanged: <composition / identity / palette / pose / layout>.
Change only: <one element or local region>.
Preserve the reference roles: A remains the composition source; B remains the lighting/material source.
Do not add: <unwanted elements>.
Maintain coherent lighting, perspective, material, and text accuracy.
```

Do not combine a composition repair with a style overhaul in the same pass. Separate structural drift from surface refinement.

## No-tool fallback

If the current host does not expose a native image generation tool, say so plainly and provide the contract for manual use. Do not imply that an image was generated. Suggest the API/CLI route only if the user explicitly asks for it and understands credential requirements.
