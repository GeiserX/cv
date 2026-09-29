# Mockup C: the editorial

File: [c.html](c.html). One self-contained page with inline CSS, one Google Font (Newsreader, `display=swap`) and a few lines of JavaScript for the theme toggle only. It works with JavaScript off: the toggle stays hidden and the page follows the system theme.

## The idea

The page reads like a magazine profile. The name is set very large, the one-line sits under it and the links are a quiet row. Three sections follow, Now, Work and Projects, with serif display type, thin rules and a lot of space. The same markup prints as a plain CV.

## What it drops from the old site, and why

- **The "My Portfolio" navbar and the blue logo-cloud hero.** The name and the one-line say who this is faster than a collage of logos.
- **The vertical timeline.** Eleven roles become a two-column table with dates on the left and role, company and one line on the right, so the whole career fits on one screen.
- **The skills tag cloud.** The tools already appear in context in each work line. A tag cloud reads as keyword stuffing and dates quickly. If a skills list is wanted back, it fits as one plain paragraph under About.
- **The contact form.** A mailto link in the header does the same job with nothing to maintain or spam-filter.
- **The old About copy** ("enthusiastic", "passionate", "tireless", emojis). It is replaced by one paragraph in the plain voice from the brief.
- **"Download Resume".** The print stylesheet makes the page itself the CV.

## What it keeps

- The mantra "Strong opinions, loosely held", as the last line of About.
- Every role, now with the April 2026 CV dates and titles, plus the links to the posts that tell the Good Peoples and Electrónica Martínez stories.
- Education and certifications, now side by side, with the three expired certifications marked and greyed.

## Details

- **Now.** akou uses its brand banner (`assets/brand/akou-banner.svg`), with the latest five posts beside it and the homelab in one line.
- **Projects.** Cards are sorted by stars with akou pinned first. Banner tiles are cropped to the 900x200 shape most repos use. DeclaRenta's image is a 1200x630 social card, so it is letterboxed on black instead of cropped.
- **Dark variant.** It follows `prefers-color-scheme` by default. The toggle overrides it and remembers the choice in `localStorage`.
- **Print.** The page prints on A4 in black on white. Banners, the posts list, the homelab line and the footer are hidden. Projects become a two-column text list and each row avoids page breaks. It prints to three pages. Forcing it onto two would need smaller type than a CV should use.
- **Head.** It has a title, a meta description, a canonical URL, Open Graph `profile` tags and a JSON-LD `Person` with the public links. There is no `og:image`, because the brief allows external references only to banners and the font. The akou banner or a hosted portrait could fill it later.
- **Checked** in headless Chromium through Playwright at 1440 px in light and dark, at 390 px on mobile, and in print emulation. All 12 images decoded, no page errors, no horizontal overflow.

## Banners (checked with curl on 2026-09-29)

A made-up repo returned 404 on the same URL pattern, which confirms the check can fail.

| Repo | `docs/images/banner.svg` | Used |
|---|---|---|
| akou | 404 | Brand banner in Now (`assets/brand/akou-banner.svg`, 200). Typographic tile in the grid. |
| Telegram-Archive | 200 | Banner |
| genieacs-container | 200 | Banner |
| VPN-Bypass | 200 | Banner |
| whisper-subs | 200 | Banner |
| CashPilot | 404 | Typographic tile |
| LynxPrompt | 200 | Banner |
| DeclaRenta | 200 | Banner, letterboxed |
| Wayback-Archive | 200 | Banner |
| Pumperly | 200 | Banner |
| smart-covers | 200 | Banner |
| genieacs-mcp | 200 | Banner |
| Personal-Genome-Pipeline | 200 | Banner |
