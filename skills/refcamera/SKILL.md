---
name: refcamera
description: Direct AI image generation with role-separated visual references—A for composition, B for lighting/style/material, and optional C for identity or texture. Discover rights-safe references, route to reference-capable image models, run visual QA, and preserve source records. Use for raster image creation/refinement, not SVG/code-native graphics.
---

# RefCamera

RefCamera turns visual references into an original generated image through a repeatable role-separated workflow. The method is model-agnostic; the execution layer should adapt to the best available image model that accepts references plus a prompt:

- **Reference A = skeleton.** It controls composition, camera angle, subject placement, negative space, crop, and visual hierarchy.
- **Reference B = surface.** It controls lighting, color, material, rendering medium, texture, and mood.

The two references must not both be used for vague "overall style". Keep their roles separate so the model has fewer conflicting signals.

## Read these references

1. Read [`references/workflow.md`](references/workflow.md) for intake, rights, role separation, variants, and refinement.
2. Read [`references/playbook-catalog.md`](references/playbook-catalog.md) to classify the job and assign A/B/C reference roles before choosing a style template.
3. Read [`references/template-router.md`](references/template-router.md) to map the selected playbook to a compact gpt-image-2-style-library template.
4. Read [`references/reference-discovery.md`](references/reference-discovery.md) when the user did not provide both references.
5. Read [`references/provider-router.md`](references/provider-router.md) before choosing an image model or API.
6. Read [`references/realistic-portrait-photography.md`](references/realistic-portrait-photography.md) for photorealistic human portraits, especially when feedback says the result looks like AI, an over-retouched studio portrait, or not a real photo.
7. Read [`references/generation-contract.md`](references/generation-contract.md) before calling the image generation tool.

For repeatable local API runs, prefer:

```bash
python3 scripts/refcamera_generate.py \
  --prompt "<role-separated prompt>" \
  --image-a "<composition-reference-url-or-path>" \
  --image-b "<style-reference-url-or-path>" \
  --out "<output.png>"
```

If the compact router does not cover a case and the installed `gpt-image-2-style-library` skill is available, read its full `references/style-library.md` rather than guessing a template.

## Required inputs

Ask for missing information only when it blocks generation:

- Reference A: composition/layout reference, or search intent if the skill must discover one.
- Reference B: style/lighting/material reference, or search intent if the skill must discover one.
- Primary subject and what should be original.
- Asset use: poster, product shot, UI, infographic, scene, character, etc.
- Aspect ratio or target dimensions.
- Whether the work is personal, client, commercial, or public-facing.
- Exact in-image text when applicable.

If the user provides two images without assigning roles, infer the most useful split, state it in one short line, and proceed unless the split is genuinely ambiguous.

If either reference is missing, do not collapse the method into a text-only prompt by default. Search for rights-safe candidates by visual keywords, inspect/score them with a vision model when available, and select one A and one B before generation.

## Default execution

1. Confirm reference roles and rights risk at a high level.
2. If references are missing, discover candidates by keyword, prefer explicit license metadata, and score A/B fitness with a vision model when possible.
3. Classify the highest-risk variable with a playbook card, assign A/B/C roles, then map the playbook to one template ID.
4. Abstract Reference A into composition rules and Reference B into style rules; use C only for a distinct identity, material, prop, or texture anchor.
5. Build one generation contract with explicit preserve/ignore boundaries.
6. Route to a native/reference-capable image model. Prefer a model that accepts multiple reference inputs; use text-only generation only when reference-capable models/credentials are unavailable and the user accepts that weaker path.
7. Send reference URLs directly first. If the provider cannot fetch a URL, retry using an in-memory data URL or the provider's file-upload mechanism. Do not require persistent downloads.
8. For a first exploration, generate four variants unless the user asks for one or cost/speed matters.
9. Review variants for composition fidelity, style transfer, originality, text, perspective, and usage fit.
10. Pick one direction and refine through a second edit/generation pass: composition-locked, style-locked, or object/text edit.

For realistic human portraits, once the user accepts the age, face direction, and composition, run a finish pass that locks those elements and changes only the photographic surface: natural light, real skin texture, flyaway hairs, camera color, grain, and location detail. Avoid replacing the accepted face while fixing an "AI photo" problem.

## Tool and safety boundaries

- Prefer the host's built-in image generation capability when it accepts reference images. For API fallback, use existing local credentials and provider adapters; do not install packages or ask for new credentials unless available routes are insufficient.
- The workflow improves the probability of a strong result by separating structural and stylistic controls; it does not guarantee that every provider will produce the best image. Validate outputs and iterate rather than claiming deterministic quality.
- Do not scrape image platforms, download private images, automate Midjourney or another image service, or pretend popularity grants a license.
- For personal/internal mood work, high-aesthetic platform links the user manually provides may be analyzed for composition and lighting; for public/commercial work, use licensed/user-owned references or abstract rules and avoid identifiable source expression.
- Do not copy identifiable branding, logos, characters, distinctive product designs, watermarks, or the protected creative expression of either reference.
- For commercial work, prefer owned, licensed, public-domain/CC-compatible, or abstracted references. A high-like image is research, not permission.
- If exact imitation would likely reproduce a protected image or a real person's identity, redirect to an original composition using only generalized visual principles.
- Use code-native SVG/HTML/CSS for simple logos, diagrams, or deterministic graphics instead of raster generation.

## Response shape

When generating, briefly show:

- selected template ID;
- selected playbook ID;
- selected model/provider and why it is reference-capable;
- A/B source URLs or user-provided source labels and rights status;
- Reference A composition rules;
- Reference B style rules;
- originality and rights constraints;
- generated variants or, if the current host has no image generation tool exposed, a clearly labeled copy-ready generation contract.

Do not stop at a prompt when the user asked for an image and a native generation tool is available.
