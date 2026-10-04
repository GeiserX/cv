# CLAUDE.md — cv

Sergio's personal page and CV at https://cv.geiser.cloud/ (GitHub Pages PROJECT site of repo GeiserX/cv with the custom domain; it must never be the user site geiserx.github.io, because a custom domain on the user site is applied to every project site under geiserx.github.io/<repo>/ too. The separate GeiserX/geiserx.github.io repo only redirects here). Repo GeiserX/cv, GPL-3.0-or-later.

- `index.html` is the whole site: one file, inline CSS, system serif stack, no JavaScript, print stylesheet that produces the CV. Keep it that way; do not add a build, a framework or a web font.
- Two blocks are generated and must not be hand-edited: between `<!-- posts:start -->`/`posts:end` (blog RSS) and `<!-- projects:start -->`/`projects:end` (GitHub API, top ten by stars). `scripts/update_content.py index.html` rewrites them; `--check` exits 1 when the page is behind. Hand-written one-liners inside the projects block are kept by the script; a repo new to the list gets GitHub's first sentence.
- `.github/workflows/update-content.yml` runs that script every twelve hours. `.github/workflows/pages.yml` deploys on push to `main` and prints `/sergio-fernandez-cv.pdf` from the page with headless Chrome; the deploy fails past three A4 pages. Pages source is "GitHub Actions", not a branch.
- Facts on the page come from `docs/redesign/CONTENT.md`. Rules from the owner: AI innovator first, the DevOps, Kubernetes, networking, distributed systems and software engineering work is ongoing ("have been doing", twelve years), akou is one project among many, projects strictly by stars, Xebia and Disney named, the San Francisco collaboration stays vague and never names a company, interviews are for Xebia's contractor hires, no hardware lists, no phone number, no em dashes, dates use "to".
- Public repo on GitHub-hosted runners (free). Never move CI to a self-hosted runner.
- No secrets in the repo.


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

## Where the tracker syncs

This repo is public, so its tracker syncs only to the private remote named by `sync.remote` in `.beads/config.yaml`. The block above says sync uses "your git remote". Here that never means this GitHub repo. Don't add it as a Dolt remote and don't push `refs/dolt/*` to it.
