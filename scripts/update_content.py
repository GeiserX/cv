#!/usr/bin/env python3
"""Refresh the two generated blocks of the page: the latest blog posts and the projects list.

Usage: update_content.py [path/to/index.html] [--posts N] [--projects N] [--check]

The page holds two marked blocks:
  <!-- posts:start ... --> ... <!-- posts:end -->        from https://geiser.cloud/rss/
  <!-- projects:start ... --> ... <!-- projects:end -->  from the GitHub API, sorted by stars
Everything outside the markers is left untouched. --check exits 1 if the file would change,
so the same script is a test. The star date in <span id="stars-date"> is updated too.
"""
import html, json, os, re, sys, urllib.request
from datetime import date
from xml.etree import ElementTree

USER = "GeiserX"
FEED = "https://geiser.cloud/rss/"
# Repos that are not projects (awesome lists, Homebrew taps, the profile repo).
SKIP = re.compile(r"^(awesome-|homebrew-|GeiserX$)")
# Repos whose "Site" link is not their GitHub homepage.
SITE_OVERRIDE = {"genieacs-container": ("https://geiser.cloud/how-to-deploy-genieacs/", "Guide")}


def fetch(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "geiserx.github.io update_content", **(headers or {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def posts_block(n):
    root = ElementTree.fromstring(fetch(FEED))
    items = root.findall("./channel/item")[:n]
    lines = ['  <ol class="now-list">']
    for it in items:
        title = html.escape(plain(it.findtext("title", "").strip()), quote=False)
        link = html.escape(it.findtext("link", "").strip())
        lines.append(f'    <li><a href="{link}">{title}</a></li>')
    lines.append("  </ol>")
    return "\n".join(lines)


def github_repos():
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    repos, page = [], 1
    while True:
        batch = json.loads(fetch(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&page={page}", headers))
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def existing_lines(text):
    """Hand-written one-liners already on the page, by repo name. They win over GitHub's description,
    so the curated wording survives a refresh; only a repo new to the list gets GitHub's first sentence."""
    out = {}
    for m in re.finditer(r'<a class="name" href="https://github\.com/[^/]+/([^"]+)">.*?<span class="line">(.*?)</span></div>', text, re.S):
        out[m.group(1)] = m.group(2).strip()
    return out


def projects_block(n, keep):
    repos = [r for r in github_repos() if not r["fork"] and not r["archived"] and not SKIP.match(r["name"])]
    repos.sort(key=lambda r: (-r["stargazers_count"], r["name"].lower()))
    lines = ['  <ul class="projects">']
    for r in repos[:n]:
        name = html.escape(r["name"])
        if r["name"] in keep:
            line = keep[r["name"]]
        else:
            desc = html.escape(one_line(r.get("description") or ""), quote=False)
            site = ""
            if r["name"] in SITE_OVERRIDE:
                url, label = SITE_OVERRIDE[r["name"]]
            else:
                url, label = (r.get("homepage") or "").strip(), "Site"
            if url and "github.com/" not in url:
                site = f' <a class="site" href="{html.escape(url)}">{label}</a>'
            line = desc + site
        stars = r["stargazers_count"]
        lines.append("    <li>")
        lines.append(f'      <div><a class="name" href="{html.escape(r["html_url"])}">{name}</a>')
        lines.append(f'        <span class="line">{line}</span></div>')
        lines.append(f'      <span class="stars">{stars} star{"s" if stars != 1 else ""}</span>')
        lines.append("    </li>")
    lines.append("  </ul>")
    return "\n".join(lines)


def plain(text):
    """No emoji, no em or en dashes, straight quotes: the page's own rules apply to fetched text too."""
    text = re.sub(r"[\U0001F300-\U0001FAFF☀-➿]", "", text)
    text = text.replace("—", ",").replace("–", ",").replace(" - ", ", ")
    return text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'").strip()


def one_line(desc):
    """GitHub descriptions can be long marketing lines; keep the first sentence."""
    desc = plain(desc)
    first = re.split(r"(?<=[.!?])\s+", desc.strip(), maxsplit=1)[0]
    if len(first) > 140:
        first = first[:137].rsplit(" ", 1)[0] + "..."
    return (first.rstrip(".") + ".") if first and not first.endswith("...") else first


def replace_block(text, key, body):
    pat = re.compile(rf"(<!-- {key}:start[^>]*-->\n).*?(\n\s*<!-- {key}:end -->)", re.S)
    if not pat.search(text):
        sys.exit(f"marker {key} not found")
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text, count=1)


def main():
    args = sys.argv[1:]
    path = next((a for a in args if not a.startswith("--")), "index.html")
    n_posts = int(args[args.index("--posts") + 1]) if "--posts" in args else 5
    n_projects = int(args[args.index("--projects") + 1]) if "--projects" in args else 10
    old = open(path, encoding="utf-8").read()
    new = replace_block(old, "posts", posts_block(n_posts))
    new = replace_block(new, "projects", projects_block(n_projects, existing_lines(old)))
    block = lambda t, k: re.search(rf"<!-- {k}:start.*?{k}:end -->", t, re.S).group(0)
    changed = [k for k in ("posts", "projects") if block(old, k) != block(new, k)]
    if "projects" in changed:  # the "Stars as of" date moves only when the stars did
        new = re.sub(r'(<span id="stars-date">Stars as of )[0-9-]+', lambda m: m.group(1) + date.today().isoformat(), new)
    if "--check" in args:
        print("would change:", changed or "nothing")
        sys.exit(1 if changed else 0)
    if changed:
        open(path, "w", encoding="utf-8").write(new)
        print(f"updated {path}")
    else:
        print("no change")


if __name__ == "__main__":
    main()
