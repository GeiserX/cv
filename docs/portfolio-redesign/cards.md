# Portfolio redesign: cards

Preview: [cards.html](cards.html). The Ghost content is the part between the `ghost-content-start` and `ghost-content-end` markers.

## The idea

The portfolio should read like the CV: short, quiet, and easy to scan. Two sentences at the top, then my ten most starred repos in a two-column grid (one column on phones). Each card has the banner, the repo name linked to GitHub, one line on what it does, the star count as plain text and a link to its site when it has one. One line at the bottom sends people to GitHub for the rest. It is a single Ghost html card with its own scoped `<style>`, the same way the About page does its companies grid.

## Keeping it current

A small job on a home box rebuilds the card: it reads star counts from the GitHub API, takes the top ten (non-fork, non-archived, no awesome lists), keeps the one-liners I wrote by hand, checks each banner, and writes the page through the Ghost Admin API. It has to run at home and talk to the Ghost origin on the LAN, because the WAF in front of the public URL rejects page bodies that contain `<img>` tags. So this is not a GitHub Action.

## What it drops

Today's page is 63 cards made by an npm tool. This one keeps ten and drops the shields.io badges (stars, forks, licence, Docker pulls, docs), the feature lists, the tech stack lines, the long descriptions and the "Total stars" footer. Star counts stay, as text.

## Banners

These eight have a banner at `docs/images/banner.svg` (checked 2026-09-29, all return 200):

- Telegram-Archive
- genieacs-container
- VPN-Bypass
- whisper-subs
- LynxPrompt
- Wayback-Archive
- Pumperly
- smart-covers

Two get a plain tile with the repo name instead:

- CashPilot has no banner (404).
- DeclaRenta has one, but it draws its logo from a relative `logo.png`. Browsers never load files referenced inside an SVG shown through `<img>`, so on this page it always shows an empty box. It is also nearly 2:1, which crops badly into the 9:2 banner shape.
