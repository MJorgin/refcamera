# Reference Discovery

Use this when the user has a clear image goal but did not provide both reference images.

## Outcome

Find two role-separated references:

- **A / composition:** camera geometry, layout, subject scale, crop, leading lines, foreground/midground/background.
- **B / style:** lighting, palette, material, medium, finish, atmosphere.

A single beautiful image is not enough unless it can be deliberately split into geometry and surface signals.

## Source risk tiers

Choose the source policy from the asset use, not from convenience.

| Use context | Allowed practical approach |
|---|---|
| Personal exploration / internal mood research | High-aesthetic platforms such as Midjourney galleries, Pinterest, Behance, Zcool, Xiaohongshu, and film stills may inform visual analysis. Prefer links/images the user manually provides or pages that are intentionally public; do not bulk scrape, bypass access controls, hide the source, or reproduce identifiable expression. |
| Client pitch / company-internal deliverable | Use licensed/user-owned references, public-domain/CC-compatible sources, or abstract the platform research into non-protected geometry and lighting rules. Keep a source note when practical. |
| Public/commercial publication, ads, product art | Use owned/licensed references or create original reference images. Avoid feeding source-unknown stock, paid-gallery images, celebrity likenesses, IP characters, logos, watermarked images, or near-copying a distinctive campaign/image. |

Popularity, likes, saves, or ranking are discovery signals, not rights grants. For any use context, separate general visual principles from protected expression: composition geometry and lighting direction are safer; exact subject, layout, logo, character, face, wardrobe, text, watermark, and distinctive scene design are not.

## Search strategy

1. Build separate keyword sets:
   - A: subject/scene + composition words such as `low angle`, `symmetric`, `central axis`, `wide angle`, `leading lines`, `stairs`, `aerial`, `over-shoulder`.
   - B: style words such as `golden hour`, `volumetric light`, `cinematic`, `sea of clouds`, `backlight`, `film still`, `material`, `editorial lighting`.
2. For automated discovery, search rights-aware and machine-accessible sources first:
   - Wikimedia Commons;
   - Openverse with source, license, and landing-page metadata;
   - Unsplash/Pexels/Pixabay or similar sources when their current license and API terms permit the use;
   - museum/library/open-data collections;
   - user-owned or client-provided assets.
3. For public/commercial work, prefer PD/CC0/CC BY, compatible modern photo licenses, or customer-owned assets. Avoid NC/ND sources unless the use clearly fits and the user accepts the constraint.
4. Do not bulk scrape, automate login, bypass anti-bot controls, or download from Midjourney galleries, Pinterest, Instagram, Xiaohongshu, Behance, Dribbble, private pages, or paywalled/search-engine image results. The user may manually provide a small number of links/images for analysis.
5. Prefer stable direct image URLs with license/source metadata. Keep the source page URL for attribution and audit.

## Using high-aesthetic but rights-uncertain references

When the user manually supplies a high-aesthetic reference from a platform:

1. inspect it for A/B role signals;
2. write explicit “ignore” boundaries for face/identity, exact subject, wardrobe, logo, watermark, text, platform style markers, and distinctive composition details when needed;
3. for personal exploration, either send the image to a reference-capable model with an originality boundary or convert it into abstract rules;
4. for commercial/public work, prefer rules-only conditioning or replace it with a licensed/original reference;
5. run a post-generation similarity check against the source's most identifiable elements.

## Vision scoring

When a vision model is available, send each candidate separately or in a small labeled group and ask for:

- score from 1–5 for the intended A or B role;
- signals worth preserving;
- signals that must be ignored;
- rights/commercial concerns visible from metadata, if any.

Pick the highest role-specific candidate, not the most generally attractive image.

## Fallback when search is blocked or unsuitable

If a suitable licensed image cannot be found, use one of these safer alternatives:

- ask the user to provide their own references;
- generate two lightweight original references with a text-to-image model, then feed those originals into the reference-capable model;
- construct explicit virtual references as detailed A/B rules, while clearly stating that the provider did not receive actual image inputs.

Do not present virtual text rules as actual image-to-image conditioning.
