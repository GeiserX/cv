# Mockup A: the document

Preview: [a.html](a.html). Open it in a browser, then press Cmd+P to see the CV it prints.

## The idea

The page is the CV. It is one column of well-set text that reads top to bottom: who I am, what I'm building now, where I've worked, what I've shipped, and what I studied. The printed version is the same page with the "Now" section taken out, so the website and the PDF can't tell different stories.

## What it drops, and why

- **The blue logo-cloud hero.** It shows tools, not work. The tools are listed in one short Skills paragraph at the bottom.
- **The vertical timeline graphic.** It spreads eleven jobs over several screens. Here each job takes three lines: dates in the left gutter, role and company, and one line on what I did.
- **The skills tag cloud.** It had no order and mixed tools I use every day with ones I touched once. The Skills paragraph lists only what I'd claim today, grouped by area.
- **The contact form.** A mailto link does the same job with no backend and no spam filter.
- **"Download Resume" pointing at a stale PDF.** The PDF is now generated from this page, as described below.
- **The 2020 "About me" text in [the current page](../../index.html).** Words like "enthusiastic", "passionate" and "tireless" are gone. What replaces them is the one line I already use to describe what I do.
- **Bootstrap, jQuery, the gulp build and all JavaScript.** The page is one HTML file with inline CSS, and it loads no web fonts. It uses the system serif stack, which is Charter on macOS and iOS with Cambria and Georgia as fallbacks.

## What it keeps

- The name at the top and the "Strong opinions, loosely held" mantra, which moves to the footer.
- The full work history, with dates taken from the April 2026 CV.
- Education and certifications. The expired certifications stay on the page but are greyed out and marked expired, so nobody has to guess.
- Projects. This time they are the top ten by GitHub stars, one line each, with akou pinned first.

## Layout details

- The column is about 68 characters wide, set in rem so the smaller nav and footer text keep the same width.
- Section headings are small uppercase labels with a hairline rule under them. Nothing else on the page has decoration.
- Light and dark follow `prefers-color-scheme`. There is no toggle, because a toggle needs JavaScript.
- On phones the date gutter stacks above each entry.
- The head carries a `<title>`, a meta description, Open Graph profile tags, `rel="me"` for Mastodon verification, and a JSON-LD `Person` block listing the public profiles.

## How the CV PDF is made

The print stylesheet does all the layout work. It sets A4 pages with 15 mm margins and 9.6 pt text. It hides the section nav, the Now section and the per-project "Site" links, and it prints links as plain black text. The contact row prints as readable addresses because each link's text is the address itself, `github.com/GeiserX` rather than "GitHub". Printed from headless Chromium today, it comes out at exactly two pages.

Cmd+P works, but a hand-made PDF drifts from the site as soon as I forget to redo it. So the plan is a GitHub Action that prints the PDF on every push and ships it with the site:

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
      - uses: actions/checkout@v5
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

Chrome is preinstalled on `ubuntu-latest`, and `pdfinfo` comes from `poppler-utils`. The page-count check makes the build fail if an edit pushes the CV onto a third page. The PDF is never committed. It exists only in the deployed site at `/sergio-fernandez-cv.pdf`, so it can't go stale.

Switching over means changing the repo's Pages source from "Deploy from a branch" to "GitHub Actions". Once that is done, a plain "PDF" link can go in the contact row.

## Open choices

- Projects shows akou plus the top ten, so eleven rows. If it should be ten in total, smart-covers drops off.
- The phone number stays out, as the brief requires. That means this PDF has no phone number, unlike the hand-made one. If recruiters need it, it could be added to the printed version only, but it would still be in the page source, so it would really be public.
