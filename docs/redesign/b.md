# Mockup B: the terminal

File: [b.html](b.html). One self-contained page with inline CSS and JS. The only external request is JetBrains Mono from Google Fonts (`display=swap`), and the page falls back to the system monospace font without it.

## The idea

The page looks like my homelab dashboards and the akou app: dark, monospace, one amber accent, content in bordered panels with a short label on the top edge. It opens with a single prompt line, my name and the one-line summary, then six panels: `now`, `work`, `projects`, `education`, `certs`, `links`. Everything is text in tables and lists, so a recruiter can scan it in under a minute and it prints as a plain CV.

## What it drops from the old site, and why

- **The hero with the blue background image and the logo cloud.** It took the whole first screen and said nothing about what I do now.
- **The long vertical timeline.** Eleven jobs as cards with bullet lists took several screens. The table puts one job on one line: dates, company, role, what I did.
- **The about paragraph.** "Enthusiastic", "passionate", "tireless" and the emoji go. The summary line I already use replaces them.
- **The skills tag cloud.** A cloud of forty names does not show what I did with them. The tools now sit next to the job or project where I used them. If recruiters or ATS filters need a flat list, it can come back as one line under `work`.
- **The contact form.** It needed a third-party backend. A mailto link does the same job with nothing to maintain.
- **Bootstrap, jQuery, Font Awesome and the gulp build.** The page needs none of them.

## What it keeps

- Every job, with the dates from the April 2026 CV.
- Both degrees, the MSc dissertation topic and the honourable mention.
- Every certification, including the expired ones. They are marked "expired" in grey instead of hidden.
- The PDF CV link, the email and the public profiles.
- "Strong opinions, loosely held." It moves to the footer.

New: what I am building now (akou), the five latest blog posts, a one-line homelab note, and the top ten repos by stars with akou pinned first.

## Stars and JavaScript

The star counts in the HTML are the ones from 2026-09-29, and with JavaScript off the page is complete and says "stars on 2026-09-29". A small script fetches `https://api.github.com/users/GeiserX/repos?per_page=100`, paging until it has every repo, since about 200 do not fit in one page. It replaces the numbers only if it found all eleven repos. It then re-sorts every row except akou and changes the label to "stars live from GitHub". If the request fails or hits the rate limit, nothing changes.

## Phone, light mode and print

- **Phone:** under 720 px each table row becomes a short block. For work, that is dates, then company, role and the one line. For projects, it is repo, language and stars, then the one line. Nothing scrolls sideways at 375 px.
- **Light mode:** the page follows `prefers-color-scheme`, with the same layout and a darker amber. Dark is the default.
- **Print:** the page turns into black on white in a sans-serif font. Panel borders, the prompt line, the "post" and "site" links, the CV link and the footer are hidden, so it prints as a CV of about three A4 pages.

## The risk, and how the mockup avoids it

A terminal look can read as a gimmick to a recruiter, as if the style mattered more than the content. The mockup keeps the style to typography and borders and never makes the reader play along:

- **No fake shell:** no typing animation, no blinking cursor, no commands to type, no ASCII art. The one prompt line is decoration and hidden from screen readers.
- **Plain words:** headings are single words, and every fact is written as a normal sentence. Nothing is written as command output.
- **Quiet colour:** one accent, at a contrast that stays readable, and no glow or neon.
- **Real structure:** tables have headers and captions, and the JSON-LD `Person` block, the Open Graph tags and the meta description are all there for search and link previews.
- **CV first:** the print stylesheet removes the look completely. A recruiter who prints it or opens it on a phone gets a normal CV.

## Checked

Rendered with Playwright's Chromium at 1280 px in dark and light, at 375 px, with JavaScript off, and as print to A4 PDF. There were no console errors and no horizontal overflow. The live star fetch replaced every number.
