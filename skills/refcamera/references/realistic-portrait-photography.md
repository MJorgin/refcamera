# Realistic Portrait Photography

Read this for photorealistic people portraits and for feedback such as “不太像真人照片”, “像 AI 写真”, “太成熟”, “塑料皮肤”, or “像棚拍精修”.

## Outcome

The target is a believable camera photograph: correct youthful age and composition, natural light, a real location, visible but healthy skin structure, and slight photographic imperfection. Do not chase a smoother or prettier result when the user is asking for realism.

## Role-separated references

- **Reference A — age, face proportions, and composition.** Prefer an original generated reference or the user's accepted generated draft. Use it for visual age, head/shoulder crop, eye placement, gaze, expression, and subject scale. Do not use a real person's photograph to clone identity.
- **Reference B — light and location surface.** Choose a candid photo with window/daylight, a recognizable cafe/street/home/outdoor environment, natural camera color, and normal lens depth of field.
- **Reference C — optional skin/hair texture anchor.** For a finish pass, add a separate unretouched photo that supplies pores, fine skin variation, eyebrow/eyelash fibers, and flyaway hair. Ignore its pose, subject identity, location, and palette.

A dreamy, creamy, heavily blurred reference often creates the “AI portrait studio” look even when the prompt asks for realism. If the accepted image is pretty but synthetic, replace the style reference instead of relying only on negative prompts.

## Two-pass refinement

1. **Base pass:** A controls age/composition; B controls candid natural light and environment. Establish the correct person, age, framing, and mood.
2. **Finish pass:** Use the accepted generated image as A, a real-light/location image as B, and a skin-texture image as C when supported. Explicitly lock identity, age, expression, pose, clothing, composition, and scene; change only skin finish, hair detail, light, camera color, grain, and background realism.

Change one lever at a time. If age is already accepted, do not regenerate freely from a new face reference.

## Age and safety language

“Girl” and “少女” are ambiguous. For a beauty or close-up portrait, make adulthood explicit unless the user appropriately asks for a child and the framing is non-glamourized. A useful default is “visually around 20 years old, clearly adult, youthful but not childlike.”

Avoid school uniforms, child-coded wardrobe, sexualized posing, and nudity for youthful portraits. Use everyday casual clothing instead.

## Positive prompt cues

- candid photo taken by a friend with a 35mm, 50mm, or 85mm full-frame lens; f/1.8–f/2.8 when shallow depth of field is desired
- window light, overcast daylight, or soft morning sunlight; not studio lighting
- real cafe, street, campus-adjacent, home, or outdoor location with concrete but unobtrusive details
- natural pores, fine skin texture, subtle tone variation, natural sheen, and unpainted natural lip texture
- a few flyaway hairs, natural eyebrow and eyelash fibers, minimal/no makeup
- real Fujifilm/Sony camera color, subtle film grain, slight handheld framing, minor imperfection
- shallow but natural depth of field; background should read as a place, not become abstract creamy bokeh

## Negative prompt cues

Plastic skin, over-smoothed skin, porcelain doll skin, beauty filter, AI portrait, influencer filter, studio lighting, heavily retouched editorial photo, dreamy bokeh, fake rim light, wax-figure face, perfect symmetry, strong makeup, school uniform, child, minor, sexualized pose, nudity, mature woman, watermark, logo, text, cartoon, anime, 3D render, malformed eyes/teeth/ears, overexposure.

## Visual QA

Review the output for:

1. real camera photograph versus AI/studio image;
2. clearly adult intended age with youthful freshness;
3. pores, subtle skin variation, flyaway hairs, and natural lip/eye texture;
4. practical light direction and a believable location;
5. eyes, teeth, ears, hands when visible, hairline, and anatomy;
6. absence of school-uniform/child-coded/sexualized cues, watermarks, logos, and text.

When choosing between variants, compare realism and the accepted age/composition separately. A slightly less polished image can be the correct answer. Keep iterating if the face becomes older or the composition drifts while adding texture.

## File and rights hygiene

- After the user accepts a final portrait, keep the selected final file and any required source/license metadata.
- Move rejected drafts, intermediate generated references, and temporary candidate downloads to Trash or delete exact temporary files. Do not delete unrelated deliverables in the same folder.
- Keep a source record for external references, including title/author when available, landing page, direct URL, and license.
- Likes and saves are not licenses. For public or commercial work, replace CC-SA/non-commercial/unknown references with owned, licensed, CC0/public-domain, or sufficiently abstracted original references.
