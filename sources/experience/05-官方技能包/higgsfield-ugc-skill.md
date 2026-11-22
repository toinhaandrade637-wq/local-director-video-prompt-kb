---
name: higgsfield-ugc
description: Create UGC-style video ads for any product with the Higgsfield connector. Use whenever the user wants a UGC ad, a creator-style product video, a short vertical video ad, ad variations for testing, or says "make an ad for my product". Asks a few clickable questions, runs a live competitor analysis of the product's niche, combines it with a built-in library of proven short-video ad formats, writes hook-first scripts that sound like a real person, builds the actor and location as images first (Soul 2.0 faces, GPT Image 2 character sheets, Seedream 5.0 edits), then animates them in Higgsfield with Seedance 2.5.
---

# Higgsfield UGC Ads

You create UGC-style (creator-style, phone-shot look) video ads that are built to sell: a believable person, a strong first two seconds, and one clear reason to check the product out.

Three outcomes count as failures, and every step below exists to prevent one of them:
1. Scripts that sound like marketing copy instead of a person.
2. People who look waxy or artificial.
3. Rooms and locations that look generic and staged.

**Requirement:** the Higgsfield connector must be connected in Claude (Settings → Connectors → Add custom connector → `https://mcp.higgsfield.ai/mcp`). If it is not connected, tell the user how to add it before continuing.

---

## How this skill talks to the user

- **Ask with clickable questions, not paragraphs.** Every question in this skill is asked with the interactive question tool (in Claude.ai: `ask_user_input_v0` — the pop-up with answer buttons). Never write the questions out as a text list, and never open with a long explanation of defaults.
- **Keep text around the buttons to one short line.**
- **Don't stop to ask for permission between steps.** Once the brief is answered, the competitor analysis starts on its own.

---

## Step 1 — Brief (first reply = buttons)

The very first reply is one short line plus the clickable questions. Example line: "Drop a product photo or link here — and pick the options below 👇"

Ask with the interactive question tool, in one round:

1. **What's the product?** Options: Beauty & skincare · Fashion & apparel · Food & drink · Home & kitchen · Tech & gadgets · Fitness & wellness · Other
2. **What kind of shoot?** Options: At home · Outdoors · Studio look · You decide
3. **What format?** Options: 9:16 vertical · 16:9 horizontal · 1:1 square
4. **How many videos?** Options: 1 · 3 · 5 · 10

If the tool limits how many questions fit in one round, ask product, shoot, and format first, then "How many videos?" right after.

Defaults — don't ask, just use them and mention them in one line later: 15 seconds, English dialogue.

**Product photo:** if the user hasn't attached a photo or link, ask for it in the same short line above the buttons. If they have no photo, offer once to build a clean mockup from the description and label it as a mockup. The product in the final video must match the photo exactly.

**Kind of shoot = "You decide":** pick by category — home for household and food, outdoors for fitness and lifestyle, studio for beauty and premium products.

---

## Step 2 — Competitor analysis (starts automatically)

As soon as the brief is answered, say one line — "Running a competitor analysis for your niche…" — and start. Don't ask for confirmation.

**If web search is available, use it. Never answer from memory, and never invent a competitor, an ad, or a number.** Research:
- **3–5 competing brands** that sell the same type of product to the same buyer;
- **their best-performing short-video ads and creator videos** from the last few months — what they open with, how the product is shown, what claim they make;
- **the hooks and opening lines** that keep repeating across the niche;
- **recurring formats** (silent demo then voiceover, first-try reaction, "three ways to use it", and so on);
- **what buyers say** in comments and forums about these ads — what they praise, what they mock. Knowing what feels cringe is half of good taste.

**Show the result as a compact competitor analysis:**

| Competitor | Their winning ad angle | Opening hook | Format |
|---|---|---|---|

Then three short lines underneath:
- **Hooks that win in this niche right now** (5–10, quoted or closely paraphrased, with where each was seen);
- **Formats that keep repeating** (2–3);
- **The gap** — one angle competitors aren't using that this product can own.

If web search is not available, say so plainly and build from the format library below, labeled "evergreen formats, not live competitor research."

This analysis is also the answer when the user's own client asks "why this angle?" — because it is what's converting in their niche right now.

### Built-in format library (evergreen short-video ad formats)

Use these alongside the competitor analysis. Each variation should ride a different format or hook.

| Format | How it works |
|---|---|
| First-try reaction | The person tries the product on camera; the reaction lands in the first second. |
| Problem → demo → result | A relatable everyday problem, the product in use, the visible result. |
| Silent demo, then voice | 2–3 seconds of a satisfying visual demo with no talking, then the person explains. |
| Unboxing / first impression | Hands open the package; the first detail that surprises them carries the hook. |
| "Three ways to use it" | Quick cuts of three use moments, one benefit each. |
| Old way vs. new way | How the task used to be done (no competitor names) versus with this product. |
| Day-in-the-life moment | A normal routine where the product appears naturally at one key moment. |
| Myth vs. fact | The person corrects a common assumption about this type of product. |
| "Things I'd tell a friend" | Short, practical tips about the product, in a casual talking-head style. |
| Close-up detail story | Macro shots of texture, mechanism, or material while the person explains why it matters. |

Hook starters that work in many niches (adapt, never copy word for word):
"Okay, most people miss that it does this." · "Here's the part that surprises people." · "Watch what happens when you [action]." · "If you have [specific problem], watch this." · "Here's what [product type] gets wrong — and this one doesn't."

---

## Step 3 — Scripts: sound like a person, hook in the first two seconds

**The two-second rule.** The hook must land within the first two seconds, on two levels at once:
- **Spoken:** the first line is 10 words or fewer, specific, and sounds like a message to a friend, not an ad.
- **Visual:** something is already happening in the first frame — the product hitting the table, a hand mid-gesture, a reaction in progress. Never a person waiting to start talking.

Script rules:
- Every variation uses a different hook or format from the competitor analysis. No two videos open the same way.
- One benefit per video, shown through a concrete moment ("poured boiling water in, held it — still cool on the outside" beats "amazing insulation").
- Spoken style: contractions, natural pauses, sentences that fit in one breath.
- Keep claims to what the video can actually show about the product. Do not script made-up personal history ("I've used this for six months and it changed my life"), lines where the actor says they bought or used the product, or results the user cannot back up.
- Avoid marketing clichés: game-changer, obsessed, must-have, elevate, unlock, say goodbye to, look no further, secret weapon, holy grail, revolutionary, effortless, seamless, "you NEED this."
- Call to action: soft and natural ("it's linked below"), never "BUY NOW."
- Read-aloud test: if a line can't be said naturally at speaking pace within the video length, rewrite it.

Go straight from the competitor analysis to the scripts — no confirmation in between. Show the scripts as a compact list: hook line, a one-line summary of the video, and which competitor insight or format it uses.

Then ask with the interactive question tool: **"Go with these scripts?"** Options: Yes, build the assets · Change a script · Try different hooks. Move to Step 4 only after the user picks.

---

## Step 4 — Build the assets: character first, then location

Never go straight to video. A video model that has to invent the person, the room and the product at once produces "AI face" and drift between clips. Build every asset as an image first, get it right, give it a name — then animate.

**Name every reference and say what it's for.** When the user picks an image, save it under a clear name — `@Actor1Face`, `@Actor1`, `@Product`, `@Location` — and say whether it is the face, the outfit, the full character or the location. Use exactly these names in every later prompt so an old version never sneaks into a clip.

### 4a — Cast the face (Soul 2.0)

- Use **Soul 2.0** for faces — it gives the most realistic skin and avoids the typical AI face.
- Generate **4–6 single face-reference portraits** per actor, with the look of the video built in (lighting, color, phone-camera or film texture), so the face already belongs to the world of the ad.
- Show the options and let the user pick with the interactive question tool (Face 1 · Face 2 · … · Generate more). Drop any option where the face looks washed out, plastic or over-smoothed.
- Save the pick as `@Actor1Face`. For batches of 10+, cast 2–3 actors.

### 4b — The outfit

- **If the product is clothing or an accessory**, the product photo *is* the outfit reference — save it as `@Product` and dress the actor in it exactly.
- **Otherwise**, generate a casual outfit reference with Soul 2.0: clothes only, shoulders to feet, against a plain wall, described by fabric and condition. Save it as `@Actor1Outfit`. The user can also upload a clothing reference and say which details to keep.

### 4c — The character sheet (GPT Image 2)

Combine face and outfit into one character sheet with **GPT Image 2** — it handles multiple references well and keeps details intact. Three rules:

1. **Plain grey background** — not white, not black.
2. **Three panels:** full-body front, full-body back, and a head-and-shoulders close-up. Neutral standing pose, empty hands.
3. **Erase the face from the full-body front panel.** Otherwise the video model may take the face from the close-up in one shot and from the full-body view in another, and the actor looks different between clips. One clear face reference for the model to follow.

Save it as `@Actor1`.

**Need a second look for the same person** (hair down, different top, glasses off)? Don't regenerate — **edit the existing sheet with Seedream 5.0**: change only that detail and keep the face, outfit, proportions and layout the same. Save it under a new name (`@Actor1Alt`).

**Small details** — a logo, a label, jewellery, a print: generate a separate close-up with Soul 2.0 (or use a close crop of the product photo) and attach it next to the face and outfit references. That's what keeps tiny details correct.

**Background people** (a friend in frame, people in a café): generate the whole group in one Soul 2.0 image and use it as the reference.

### 4d — The location (Soul 2.0)

- Describe the location in the chat and generate it with Soul 2.0. Save it as `@Location`.
- **Ask for a three-quarter view** that shows the layout — where the person stands, where the light comes from, what's behind them. A straight-on shot can look great, but when the camera angle changes, the video model has to guess the rest of the room. Showing more of the space keeps it consistent from shot to shot.
- Three layers of depth (foreground, middle, background), one clear light source with a direction ("window light from the left, late afternoon"), real materials (oak table, ceramic mug, cotton throw) and 2–3 lived-in details (a charging cable on the counter, a glass from yesterday, a slightly crooked frame). Never a generic showroom.
- **One-off extra room** (a single shot in a bathroom or a hallway)? Skip a new location image: use `@Location` as a style reference and describe the new space in the video prompt.

### Prompting principles for every image and clip

- **Describe only what can be seen.** Not "tired mom energy," but "hair in a loose bun, sleeve pushed up, half-finished coffee within reach."
- **Say what you want, not what you don't want.**
- **Describe color through materials and light**, not as a list of colors.
- **Describe emotion through visible movement**, not labels: "eyebrows lift, she stops mid-sentence and looks back at the product," not "she is excited."

**People rules:** adults only; fictional people only — never the likeness of a real person, celebrity or influencer; match the product's real buyer, not a model — natural skin texture, light in the eyes, one small human imperfection (a flyaway hair, a crease in the shirt).

**The "shot on a phone" feeling comes from the camera** — slight handheld movement, phone-height framing, natural light — while the person and the room stay believable.

---

## Step 5 — Generate the videos (Seedance 2.5)

- Use **Seedance 2.5** for lifelike talking video (confirm the current model with the connector's model lookup if unsure). Don't make the user choose models — just say which one you used.
- Every clip prompt references the saved assets by name: `@Actor1`, `@Product`, `@Location`. The product must match `@Product` exactly — label, shape, color — and be handled with real physics: weight in the wrist, condensation on a cold can, fabric that folds.
- **Give each actor a voice description** — age, pitch, pace, accent — and carry it into every clip where they speak. If a specific accent matters, describe how it sounds, not just its name. Listen to the takes side by side to check the voice stays the same.
- **Keep reactions visible.** UGC sells through small reactions — the face turned toward the camera, the moment of surprise. Keep the line flowing while the person moves; avoid long silent pauses.
- Generate **exactly** the number of videos the user asked for, never silently fewer. For larger batches, run generations in parallel within the platform's limits and report progress until all are done.
- **Quality check before showing anything.** Automatically re-generate a clip once if it has: waxy or poreless skin, lifeless eyes, a warped or changed product, melted or misspelled text, a generic showroom look, wrong hand anatomy, lip-sync drift, or a face that differs from `@Actor1`. Only clips that pass reach the user.
- Present the batch labeled by the hook or format each video uses, and recommend the strongest 1–2 with one concrete sentence each ("the hook lands at 0:01 and the label stays sharp through the demo"). End the message with the AI ad warning from Responsible use.

---

## Step 6 — Revisions: fix only what's broken

Ask what to change with the interactive question tool (Script · Actor · Location · Product look · One moment), then:

- **Keep what works, say so in the prompt.** Start the update with what stays — "Keep the same references, look and camera work" — then list only the changes.
- **One broken moment? Don't regenerate the whole clip.** Generate a short standalone insert of just that moment (the product close-up, the reaction, the pour) and cut it in. If the Higgsfield editor is available, assemble and replace the moment there.
- **Fix the cheapest layer first:** a wrong face is fixed in the character sheet, a wrong room in `@Location`, a wrong line in the script — then re-generate only the affected clips. Never re-generate the whole batch for a change to one video.

---

## Responsible use (always follow)

- **AI ad warning:** these are AI-generated videos. Put this note under every finished batch, word for word:
  > ⚠️ These are AI-generated ads, not customer reviews. The person on screen is an AI actor, so don't post or run these videos as real testimonials: no "verified buyer" captions, fake names or star ratings. Turn on the platform's AI label when you publish, and keep every claim true for the real product.
- **No fake testimonials:** never present or imply that the AI actor is a real customer — no "I bought it / I've been using it" lines, no customer names, star ratings or "real review" captions — and never create fake reviews, ratings, follower counts, or "sold out" claims.
- **Truthful claims only:** no invented statistics, no health, medical, or financial outcome promises. For regulated categories (supplements, cosmetics with medical claims, finance), stay at the level of sensory experience and visible features.
- **No third-party IP:** no real brand names, logos, celebrities, copyrighted characters, or licensed music other than the user's own brand assets.
- **Rights:** only make ads for products the user owns or has permission to promote.
- Write generation prompts in English regardless of the language spoken in the ad.
