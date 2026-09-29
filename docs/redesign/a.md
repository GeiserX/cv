# Mockup A: the document

Preview: [a.html](a.html). Open it in a browser, then press Cmd+P to see the CV it prints.

## The idea

The page is the CV. One column of well-set text that reads top to bottom: who I am, what I am doing now, where I have worked, what I have shipped, what I studied. The printed version is the same page with the blog list taken out, so the website and the PDF cannot tell different stories.

## What changed after the first review (2026-09-29)

- The opening line says AI innovator first, then that the DevOps, Kubernetes, networking, distributed systems and software engineering work continues. Open source and the homelab are named as the hobby, without a list of hardware.
- Now describes the Xebia work with Disney and, in one deliberately vague sentence, the collaboration with San Francisco-based projects on AI agent infrastructure.
- akou is no longer pinned or featured. Projects are the top ten by GitHub stars, nothing else.
- Every job that has a blog post or a repository behind it links to it: Claranet to five posts, ACSdesk to the GenieACS container, services and two posts, AP Data Services to AdamPartsFinder, Good Peoples Connected to the PiSpot repos, Electrónica Martínez to three repos and two posts. The BEng entry links the final project post (zero-touch provisioning, honourable mention).
- Certifications carry years and links for all seven, including the two Drive scans. AWS Solutions Architect Professional shows 2026. The four expired ones show their span and the word expired.
- Skills are three groups in this order: AI, DevOps and platform, Software.
- The X handle is in the contact row and in the Twitter card metadata.
- Date ranges use "to" instead of a dash.

## What it drops from the old site, and why

- **The blue logo-cloud hero.** It shows tools, not work.
- **The vertical timeline graphic.** Eleven jobs over several screens. Here each job takes three lines: dates in the left gutter, role and company, one line of what, with links to the evidence.
- **The skills tag cloud.** No order, tools touched once next to tools used daily. Replaced by three short groups.
- **The contact form.** A mailto link does the same job with no third party.
- **"Download Resume" pointing at a stale PDF.** The PDF is generated from this page, see below.
- **The 2020 "About me" copy.** "Enthusiastic", "passionate", "tireless" are gone.
- **Bootstrap, jQuery, the gulp build and all JavaScript.** One HTML file, inline CSS, system serif stack (Charter on macOS and iOS, Cambria and Georgia as fallbacks). No web font.

## How the page stays current

Two blocks are generated and everything else is hand-written.

- `<!-- posts:start -->` to `<!-- posts:end -->`: the latest five posts from https://geiser.cloud/rss/.
- `<!-- projects:start -->` to `<!-- projects:end -->`: the top ten repositories by stars from the GitHub API (forks, archived repos, awesome lists and Homebrew taps excluded), with GitHub's own first sentence as the description and the homepage as the Site link. The "Stars as of" date updates with them.

[`scripts/update_content.py`](../../scripts/update_content.py) rewrites both blocks and touches nothing outside the markers. [`.github/workflows/update-content.yml`](../../.github/workflows/update-content.yml) runs it every twelve hours and on demand, and commits only when something changed. It is the same pattern the profile README already uses for its post list and star badges, in one script instead of two actions. `update_content.py index.html --check` exits 1 when the page is behind, so it doubles as a test; on 2026-09-29 a deliberately wrong star count made it fail and a clean run made it pass.

## How the CV PDF is made

The print stylesheet does the layout: A4, 15 mm margins, 9.6 pt text, the section nav and the post list hidden, links printed as plain black text. The contact row prints as readable addresses because each link's text is the address itself.

A hand-made PDF drifts from the site as soon as it is forgotten, so the plan is a GitHub Action that prints the PDF on every push and ships it with the site:

```yaml
name: pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest   # public repo: GitHub-hosted runners are free
    steps:
      - uses: actions/checkout@v7
      - name: Print the CV from the page itself
        run: |
          sudo apt-get install -y --no-install-recommends poppler-utils
          mkdir -p _site && cp index.html _site/
          google-chrome --headless=new --no-sandbox --no-pdf-header-footer \
            --print-to-pdf=_site/sergio-fernandez-cv.pdf "file://$PWD/_site/index.html"
          test "$(pdfinfo _site/sergio-fernandez-cv.pdf | awk '/^Pages:/{print $2}')" -le 2
      - uses: actions/upload-pages-artifact@v4
        with: { path: _site }
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: github-pages
    steps:
      - uses: actions/deploy-pages@v4
```

Chrome is preinstalled on `ubuntu-latest`, and `pdfinfo` comes from `poppler-utils`. The page-count check fails the build if an edit pushes the CV onto a third page. The PDF is never committed; it exists only in the deployed site at `/sergio-fernandez-cv.pdf`. Switching over means changing the repo's Pages source from "Deploy from a branch" to "GitHub Actions". Once that is done, a "CV (PDF)" link goes in the contact row, and the blog's About page can point at it instead of the hand-uploaded file.

## Open choices

- The phone number stays out, as on the blog. The PDF therefore has no phone number.
- The X handle is @GeiresX, taken from the GitHub profile's social links.
- 5G-DIVE is text only because its site answers 403 to automated checks.
