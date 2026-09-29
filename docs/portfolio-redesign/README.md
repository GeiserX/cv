# The blog's Portfolio page: what runs it today, and two ways to replace it

Written 2026-09-29 for https://geiser.cloud/portfolio/.

## What runs it today

The page is written by [ghost-github-portfolio](https://github.com/GeiserX/ghost-github-portfolio), your own npm package (0.3.5, TypeScript, last commit 2026-04-28). It lists your public repositories by stars, builds one html card per repository with a banner image and a row of shields.io badges (stars, forks, licence, Docker pulls, website), adds a footer with totals, and PUTs the result to the Ghost page over the Admin API. It is meant to run on a schedule, but nothing schedules it: no cron, no Action, no container. It ran by hand on 2026-04-16 and again on 2026-09-28 during the blog renovation.

What the live page holds after that last run: 63 cards, 263 images, 206 shields.io badges, a 103 KB HTML body, and a "Total Stars: 1639+" footer. Six cards have no banner because their repositories have none (CashPilot, tailscale-rs, claude-code-parallel-skills, akou, CashPilot-Desktop, claude-skills), so they sit in the grid as bare text next to cards with images.

Three bugs in the tool, found while regenerating the page:

1. `maxRepos` is applied before `excludeAwesomeLists`, so with the default 50 the fourteen awesome-* repositories use up slots and are then removed, and the page shows 36 cards instead of 50.
2. Archived repositories are never filtered; the only way to drop one is `excludeRepos`.
3. The README says `GHOST_ADMIN_API_KEY` overrides the config file, but the code prefers the file value, so the variable is ignored.

And one thing the tool cannot do any more: its PUT goes to the public URL, and the Coraza WAF in front of the blog rejects any Admin API body that contains `<img`. Every card has one. The 2026-09-28 run only worked because the page was written through the origin on the LAN with a separate script.

## Can it show only the top ten?

Yes, `maxRepos: 10` with `excludeAwesomeLists: true` does it once bug 1 is fixed (today it would show 10 minus the awesome lists that fall in the top 10). The badges, the footer and the per-card layout stay as they are; the tool has no option to drop them.

## Two replacements, with mockups

Both use the same source as https://cv.geiser.cloud/: the top ten by stars from the GitHub API, your hand-written one-liners, star counts as plain text, no badges, no footer, no stats block.

**List**, [list.html](list.html) ([desktop](list-desktop.png), [mobile](list-mobile.png)), notes in [list.md](list.md). Ten rows, no images. Because the body contains no `<img`, `<pre><code` or `<script`, it passes the WAF, so the existing twelve-hourly GitHub Action in this repository can write the Ghost page as well as the CV page: one script, one schedule, two pages that can never disagree. The Ghost Admin key becomes a repository secret.

**Cards**, [cards.html](cards.html) ([desktop](cards-desktop.png), [mobile](cards-mobile.png)), notes in [cards.md](cards.md). Two columns of cards with the repository banner on top, or a plain tile for the ones without a usable banner (CashPilot has none; DeclaRenta's banner references a relative logo file that browsers never load inside an `<img>`, so it comes out empty). Prettier, and closer to what the page is today. Because of the `<img` tags it can only be written through the origin, so it needs a job on a home box (a small container in the geiserback ghost stack, or a launchd job on a Mac mini), not a GitHub Action.

## What was done (2026-09-29, evening)

The owner picked the cards, with three columns and 21 repositories. ghost-github-portfolio 0.4.0 produces exactly that page. The WAF on geiserback's Caddy now skips inspection for Ghost-authenticated Admin API calls (Ghost still checks the token), so the page is rewritten every six hours by `.github/workflows/portfolio.yml` in this repository on a GitHub-hosted runner, with `portfolio/config.yml` holding the one-liners and the key in a repository secret. Nothing runs on a home box. The rest of this file is the analysis as it stood before that decision.

## What I would have done

Ship the list now from the Action and archive ghost-github-portfolio. It has 0 stars, it exists for this one page, its output is the thing you want to get rid of, and its de-slopped README would describe a tool nobody else needs. If you want the banners, the cards variant is one script on geiserback and the same list underneath; the archive decision does not change.

Either way the page loses: 53 cards, 206 badges, the totals footer, the GitHub stats block, and the twice-a-year hand run.
