# CLAUDE.md — cv

Sergio's personal page and CV at https://cv.geiser.cloud/ (GitHub Pages PROJECT site of repo GeiserX/cv with the custom domain; it must never be the user site geiserx.github.io, because a custom domain on the user site is applied to every project site under geiserx.github.io/<repo>/ too. The separate GeiserX/geiserx.github.io repo only redirects here). Repo GeiserX/cv, GPL-3.0.

- `index.html` is the whole site: one file, inline CSS, system serif stack, no JavaScript, print stylesheet that produces the CV. Keep it that way; do not add a build, a framework or a web font.
- Two blocks are generated and must not be hand-edited: between `<!-- posts:start -->`/`posts:end` (blog RSS) and `<!-- projects:start -->`/`projects:end` (GitHub API, top ten by stars). `scripts/update_content.py index.html` rewrites them; `--check` exits 1 when the page is behind. Hand-written one-liners inside the projects block are kept by the script; a repo new to the list gets GitHub's first sentence.
- `.github/workflows/update-content.yml` runs that script every twelve hours. `.github/workflows/pages.yml` deploys on push to `main` and prints `/sergio-fernandez-cv.pdf` from the page with headless Chrome; the deploy fails past three A4 pages. Pages source is "GitHub Actions", not a branch.
- Facts on the page come from `docs/redesign/CONTENT.md`. Rules from the owner: AI innovator first, the DevOps, Kubernetes, networking, distributed systems and software engineering work is ongoing ("have been doing", twelve years), akou is one project among many, projects strictly by stars, Xebia and Disney named, the San Francisco collaboration stays vague and never names a company, interviews are for Xebia's contractor hires, no hardware lists, no phone number, no em dashes, dates use "to".
- Public repo on GitHub-hosted runners (free). Never move CI to a self-hosted runner.
- No secrets in the repo.
