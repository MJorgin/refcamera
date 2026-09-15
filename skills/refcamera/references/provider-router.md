# Provider Router

The RefCamera role-separated contract stays fixed; provider fields change.

## Selection order

1. **Host-native image tool** when it accepts multiple image inputs and preserves output files in the workspace.
2. **Configured high-quality edit/reference model**, e.g. Qwen-Image-Edit-2509, Seedream 4/5 image mode, gpt-image edit, FLUX Kontext, or another provider-specific multi-reference endpoint.
3. **OpenAI-compatible image/edit endpoint** already configured on the machine.
4. **Text-to-image fallback** only when no reference-capable credential/model is available; explicitly tell the user that A/B were encoded as text rather than sent as images.

## Locally observed adapters

| Provider/model | Reference fields | Notes |
|---|---|---|
| SiliconFlow `Qwen/Qwen-Image-Edit-2509` | `image`, `image2`, `image3` in `/v1/images/generations`; URL or data URL | Best current local route when `SILICONFLOW_API_KEY` is available. The service may fail to fetch some Flickr URLs; retry with data URLs. |
| SiliconFlow `Qwen/Qwen-Image-Edit` | `image` in `/v1/images/generations`; URL or data URL | Single-reference editing; can combine A/B into one image or text only. |
| SiliconFlow `Kwai-Kolors/Kolors` | text only via `/v1/images/generations` | Useful fallback, not a true role-separated reference path. |
| Zhipu `glm-image` | text only via `/paas/v4/images/generations` | GLM vision keys can inspect references, but `glm-image` itself is not a reference-image input. |
| Volcano/Ark Seedream 4/5 | `image` as URL, data URL, or array depending model/version | Use only with `ARK_API_KEY`, `MODEL_IMAGE_API_KEY`, or `MODEL_AGENT_API_KEY`. Avoid scripts that print Authorization headers. |
| OpenAI-compatible edit models | provider-specific multipart or JSON fields | Verify the exact endpoint and field names from current docs; do not assume `/images/generations` accepts files. |

For arbitrary JSON providers, the bundled helper supports field mapping:

```bash
python3 scripts/refcamera_generate.py \
  --provider generic-json \
  --endpoint "$IMAGE_EDIT_ENDPOINT" \
  --api-key-env MY_IMAGE_KEY \
  --model "$MODEL_ID" \
  --image-a "$URL_A" --image-b "$URL_B" \
  --image-a-field image --image-b-field style_image \
  --extra-json '{"size":"1664x928"}' \
  --out output.png
```

Use `--response-url-path` when the returned URL is not under `images[0].url` or `data[0].url`. Multipart-only providers still need a provider-specific call because their field encodings differ.

## URL and upload handling

1. Send public image URLs directly when supported.
2. If the image provider returns fetch/unknown-server errors, fetch the image locally, convert it to a data URL in memory, and retry.
3. Use multipart upload only when the provider requires it; follow its field order and limits.
4. Persist source references only when the user needs an audit bundle. Temporary processing may stay in memory or the system temp directory.
5. Never log API keys, Authorization headers, signed URLs with credentials, or private image contents.

## Reference count mapping

- Two references and a multi-image model: A=`image`, B=`image2`; use `image3` for an optional object/identity anchor.
- One-reference edit model: create a side-by-side A/B contact sheet or send the stronger reference while encoding the other as precise text. Label this as a degraded path.
- Text-only model: preserve A/B separation in the prompt but state that no image references were sent.

## Prompt requirements for reference models

State role boundaries directly:

- “Image 1 is composition/layout only; ignore its subject identity, palette, text, people, and era unless requested.”
- “Image 2 is lighting/material/style only; ignore its composition, subject identity, and location.”
- “Create an original scene: ...”

Add negative prompts when supported, but do not rely on negatives alone for rights safety.

## Quality control

After generation, inspect with a vision model or equivalent visual review:

- A geometry fidelity;
- B surface/lighting fidelity;
- originality and absence of source-specific watermarks/branding;
- subject/architecture/anatomy/text/perspective correctness;
- intended aspect ratio and use fit.

Refine one lever at a time. If geometry fails repeatedly, make a wireframe/contact sheet and send that as Reference A.
