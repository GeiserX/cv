# geiserx.github.io: what is wrong today and what to change

Audit of the live site on 2026-09-29, before the mockups in this folder.

## What the site is today

A 2020 Bootstrap 3 portfolio template, last content edit March 2026. jQuery 1.12 from Google's CDN, Font Awesome 4, Lato from Google Fonts, a gulp build for SCSS, and until two weeks ago a committed `node_modules` with 56 known vulnerabilities. Page title is "My Portfolio". Roughly 9,200 px tall on desktop.

## Findings, ranked

1. **It contradicts the rest of your presence.** Hero says "Senior Cloud DevOps Engineer"; the blog says you build AI agent tooling and open-source apps; the GitHub README says "Staff AI Engineer". Experience stops at Claranet, so Xebia (since July 2025) is missing. The CV PDF in the repo (March 2026) is older than the one on the blog (April 2026), and neither mentions akou or the blog. Three versions of the same résumé, all drifting.
2. **The hero is a logo cloud of 60 vendor logos** (Trello, Basecamp, Okta, Puppet...) behind your name. It says "tools I have heard of", not "things I built". It is also the heaviest asset on the page.
3. **The timeline is the whole page.** Eleven jobs with four to eight bullets each, in the order of a CV but at the width of a blog. A recruiter scrolls past nine screens of Repsol internship bullets from 2014 before reaching Education. Nobody reads a 2014 internship in bullet form; one line is enough.
4. **Projects shows three items from 2020** (Kubernetes assessment, 5G-DIVE, a provisioning service) while GitHub shows Telegram-Archive at 215 stars, genieacs-container at 135, VPN-Bypass at 122, whisper-subs at 103, and akou. The site's best material is not on the site.
5. **The skills section is a tag cloud of 50 badges** with no order. It reads as keyword stuffing. A one-paragraph line, grouped, does more.
6. **The contact form posts to Formspree with your ProtonMail address in the action URL**, so the address is public anyway and the form adds a third party for nothing. A `mailto:` link and the blog link do the same job.
7. **Nothing points at the blog.** The blog is where you actually write; the site never links it in the body.
8. **Certifications are shown as all current.** CKA, AWS Associate and Terraform Associate show as expired on Credly. Showing them as current is the kind of thing an interviewer checks.
9. **No metadata.** Title "My Portfolio", no meta description, no Open Graph image, no JSON-LD. Sharing the link on LinkedIn shows nothing. Search shows "My Portfolio".
10. **Build machinery for a static page.** gulp, SCSS, package.json, a lockfile, Dependabot PRs, a stale workflow: all to compile one stylesheet. A single HTML file with inline CSS has no dependencies to update and cannot rot.
11. **Accessibility basics.** Low-contrast grey on white in the timeline, emoji in body copy, icon-only social links without labels, no skip link.

## What to do, regardless of which mockup you pick

- **One source of truth for the CV.** The page is the CV. A print stylesheet makes Cmd+P produce it, and a GitHub Action runs headless Chromium on every push to write `cv.pdf` into the repo, so the PDF on the blog's About page can point here and never drift again. The seven job-title versions collapse to one line you edit in one place.
- **Kill the build.** One `index.html`, one `cv.pdf`, a `favicon`, an `og.png`. Delete gulp, SCSS, package.json, node_modules, the jQuery and Bootstrap copies, and the vendor logo hero. Pages serves the file as is.
- **Lead with Now.** akou and the last five posts at the top, pulled from the blog RSS at build time by the same Action (Ghost's feed has no CORS, so not client-side). The person reading has 20 seconds; what you build today is the answer.
- **Experience as a table, one line per job.** Dates left, company and role, one line of what. Link the three jobs that have a blog post behind them (Electrónica Martínez, Good Peoples Connected, Claranet) to the post instead of re-telling them.
- **Projects from GitHub, sorted by stars, akou pinned.** Same as the blog portfolio generator does, but static: the Action refreshes the star counts.
- **Certifications with honest state.** Held, and the year it expired where Credly says so.
- **Metadata.** Title "Sergio Fernández", a one-line description, an OG image (your headshot from the blog or the akou wordmark), JSON-LD Person with the public links.
- **Drop the contact form.** `sergio@geiser.cloud` as a link.
- **Domain, optional.** `cv.geiser.cloud` as a CNAME on the repo, so the GitHub subdomain stops being the canonical URL. Cloudflare record plus a `CNAME` file; Pages issues the certificate.
- **What to keep.** The GPL licence, the repo name, the URL, the company logos if you want them, but on the blog's About page, not here.

## The three mockups

See `a.md`, `b.md` and `c.md` next to each file for the rationale, and the screenshots in this folder. Short version:

- **A, the document.** Text only, one column, reads and prints as a CV. Lowest risk, fastest to maintain, the one I would ship first.
- **B, the terminal.** Dark monospace panels in the style of your dashboards and akou. Strong personality, matches what you build now, some recruiters will find it cold.
- **C, the editorial.** Big type, project banners from your repos, light theme. The most "portfolio" of the three and the most work to keep looking good as banners change.
