# RefCamera

> Give AI image models a cinematography crew, not a moodboard.

RefCamera is a Codex skill for role-separated AI image generation. Instead of sending a model a pile of inspirational images, assign each reference a narrow job:

- **A — geometry:** composition, camera angle, crop, subject scale, and hierarchy.
- **B — surface:** lighting, color, material, camera finish, and atmosphere.
- **C — optional anchor:** identity, age, skin/hair texture, product shape, or one specific material.

The same contract can be routed to different reference-capable image models. The current helper includes a SiliconFlow Qwen Image Edit adapter and a generic JSON adapter, with URL-to-data-URL fallback when a provider cannot fetch a public image URL.

## Why RefCamera

Moodboard prompting often causes reference contamination: the model copies faces, clothing, locations, watermarks, or lighting from the wrong image. Multi-turn edits also drift: fixing skin texture can replace the face, and changing lighting can break the composition.

RefCamera solves this by making the reference roles and edit invariants explicit:

1. Classify the task with a playbook.
2. Assign A/B/C reference roles.
3. Write an original generation contract.
4. Route to a reference-capable model.
5. Review composition, surface realism, safety, and originality.
6. Refine one variable at a time while locking accepted parts.

## Included playbooks

- Realistic portrait
- Candid street/documentary photo
- Product/material study
- Architecture/interior
- Narrative scene
- Character consistency
- Poster hero composition
- Concept product breakdown

Text-heavy UI, dense infographics, logos, icons, and deterministic diagrams are intentionally out of scope. Prefer code-native, vector, document, or UI workflows for those.

## Install

Copy the skill into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/refcamera ~/.codex/skills/refcamera
```

Restart Codex or reload skills if needed.

## Configure image generation

The included helper does not require Python dependencies beyond the standard library.

Set a SiliconFlow key in either the environment or a local secrets file:

```bash
export SILICONFLOW_API_KEY="your-key"
```

Or put it in `~/.codex/secrets/media-tools.env`:

```ini
SILICONFLOW_API_KEY=your-key
```

Never commit this file. The script reads the key locally and does not print authorization headers.

## Quick start

```bash
python3 ~/.codex/skills/refcamera/scripts/refcamera_generate.py \
  --provider siliconflow-qwen-edit \
  --image-a ./composition-reference.png \
  --image-b ./lighting-reference.jpg \
  --out ./output.png \
  --prompt "$(cat examples/realistic-portrait-contract.md)"
```

For a model that uses different JSON field names:

```bash
python3 scripts/refcamera_generate.py \
  --provider generic-json \
  --endpoint "$IMAGE_EDIT_ENDPOINT" \
  --api-key-env MY_IMAGE_KEY \
  --model "$MODEL_ID" \
  --image-a ./a.png \
  --image-b ./b.jpg \
  --image-a-field image \
  --image-b-field style_image \
  --extra-json '{"size":"1024x1536"}' \
  --prompt "..." \
  --out ./output.png
```

Run `python3 scripts/refcamera_generate.py --help` for all options.

## Reference contract

Every generation should state:

- what each image controls;
- what must be ignored from each image;
- the original subject or scene;
- text, logos, and watermark constraints;
- rights/use context;
- target aspect ratio and number of variants;
- invariants for follow-up edits.

See [`examples/realistic-portrait-contract.md`](examples/realistic-portrait-contract.md).

## Realistic portrait guidance

For photorealistic people, make adulthood explicit when appropriate and separate age/composition from lighting/texture:

- use A to lock framing, visual age, gaze, and face proportions;
- use B for practical light, location context, lens color, and atmosphere;
- use an accepted draft as C when the user says the face or age is already right;
- use a separate texture reference only for skin, hair fibers, and camera finish;
- avoid school uniforms, child-coded styling, sexualized posing, and nudity in youthful portraits.

If the image looks like AI, do not immediately redraw the face. Replace the light/style reference and reduce beauty-filter polish.

## Rights and privacy

Likes, saves, and reposts are not licenses.

- Personal exploration can use broader mood research, but outputs should still avoid direct duplication.
- Client, public, or commercial work should use owned, licensed, public-domain/CC-compatible, or original generated references.
- Record title, author, page URL, direct URL, and license for external references.
- Do not scrape private platforms, bypass access controls, or automate services that prohibit automation.
- Treat personal photos and identifiable faces as private input; avoid caching or publishing them without permission.

RefCamera is a workflow aid and does not provide legal advice.

## Repository layout

```text
skills/refcamera/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/refcamera_generate.py
examples/
LICENSE
```

## Roadmap

- Reference preflight checks for watermarks, age ambiguity, aspect ratio, and conflicting light
- Run manifests with prompt, provider, source records, and QA notes
- Seedream adapter and multi-variant batch support
- Provider capability matrix
- Optional local photographic finish pass for grain, color, and subtle handheld framing
- More rights-safe example packs without identifiable real portraits

## License

MIT. See [`LICENSE`](LICENSE).
