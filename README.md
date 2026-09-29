<p align="center">
  <img src="docs/images/banner.svg" alt="geiserx.github.io banner" width="900">
</p>

<h1 align="center">geiserx.github.io</h1>

<p align="center">Sergio Fernández's page and CV: <a href="https://geiserx.github.io/">geiserx.github.io</a></p>

---

One HTML file, no build. `index.html` holds the page and its print stylesheet, and the CV PDF at `/sergio-fernandez-cv.pdf` is printed from that same page on every deploy, so the two cannot drift apart.

## How it works

- `index.html` is the whole site. Inline CSS, system fonts, no JavaScript.
- Two blocks inside it are generated: the latest blog posts (from the [blog](https://geiser.cloud) RSS) and the top ten repositories by stars (from the GitHub API). `scripts/update_content.py` rewrites them and touches nothing else; `.github/workflows/update-content.yml` runs it every twelve hours and commits only when something changed. Hand-written project descriptions survive a refresh.
- `.github/workflows/pages.yml` deploys the site with GitHub Actions and prints the CV with headless Chrome. It fails if the CV runs past three A4 pages.
- `docs/redesign/` keeps the 2026 redesign material: the content brief, the audit of the old site, the two alternative mockups and their screenshots.

## Editing

Edit `index.html` and push to `main`. To refresh the generated blocks by hand: `python3 scripts/update_content.py index.html` (`--check` exits 1 if the page is behind).

## Licence

GPL-3.0, see [LICENSE](LICENSE).
