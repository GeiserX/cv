# About page: companies grid, three dark variants

The logo grid at the bottom of [geiser.cloud/about](https://geiser.cloud/about/) uses white tiles that clash with the forced dark theme. Each file here is a standalone preview. The Ghost card sits between `<!-- ghost-content-start -->` and `<!-- ghost-content-end -->`. To ship one, paste that block over the existing html card. Every variant is one html card with scoped CSS, only `co-` class names and no JavaScript. Each one holds all 29 logos, the 28 existing ones plus Neutral Base. Screenshots at 1280 and 390 px wide sit next to each file.

## The variants

**Dark tiles** ([tiles-dark.html](tiles-dark.html), [desktop](tiles-dark-desktop.png), [mobile](tiles-dark-mobile.png)). This keeps today's grid but swaps the white tiles for a surface one step lighter than the page (`#1d2024`), with a hairline border. Logos render as light monochrome and take their colour on hover. It is the smallest change from what is live. The weakness is that a square tile suits square marks: KLM, Twitch and Neutral Base read large, while long wordmarks like Airline Assistance, AeroMexico and British Airways end up small inside the same box.

**Logo wall** ([wall.html](wall.html), [desktop](wall-desktop.png), [mobile](wall-mobile.png)). There are no tiles or borders, only centred logos at one height with wide gaps. It is the calmest of the three and sits best in the dark page. Long wordmarks stop at a width cap, so TrustYou and Zeit Online render a little shorter than the rest. The square marks (Mercedes-Benz, Safety 14, Walt Disney, Twitch, Neutral Base) get a slightly taller box, or they look like dots next to the wordmarks. On phones it becomes a three-column grid.

**Employers and clients** ([rows.html](rows.html), [desktop](rows-desktop.png), [mobile](rows-mobile.png)). This has the same monochrome treatment, split into two labelled groups with the company name under each logo. The Employers row holds Neutral Base, Xebia, Claranet, ACSdesk and Innoxess. The Clients row holds the other 24 in alphabetical order. The captions carry the logos that are hard to read at this size, such as Aeroground, Airline Assistance and Userwerk.

**Pick: Employers and clients.** On an About page, the split between the places he worked and the companies he worked for is the useful information. The captions also mean no logo has to be legible on its own. If the captions feel like too much, the wall is the second choice.

## Grouping

- Telcaria is an employer but has no logo on the site, so it does not appear. Adding one means uploading the logo and adding one line to the Employers row.
- Levante Networks stays in Clients. Electrónica Martínez's later name is Cartago Telecom, not Levante Networks.
- Walt Disney is in Clients because that work was a client engagement through Xebia.
- Every logo not listed as an employer went to Clients. None of them was a doubtful case.

## How each logo is treated

The logos arrive in four shapes, and one filter cannot handle them all. Each `<img>` carries one class for its resting look and, where needed, one for hover.

| Class | Logos | Resting look | Hover |
|---|---|---|---|
| none | most transparent PNG and SVG | `brightness(0) invert(.92)`: a light silhouette | original colours |
| `co-detail` | LSG Sky Chefs, Hochbahn Hamburg | inverted greyscale, which keeps the lines inside the round emblems that a silhouette fills in | lifted (see below) |
| `co-paper` | Casacom, Innoxess | these have an opaque white background, so they are inverted and blended with `screen`, which drops the background | lifted, still blended |
| `co-plate` | Walt Disney, Neutral Base, Xebia | these have an opaque black or purple background, so they get greyscale plus contrast and a `screen` blend, which removes the background | original, still blended |
| `co-lift` (hover) | AeroMexico, Aeroground, Airline Assistance, British Airways, Hochbahn, Inform, Kobil, Levante Networks, LSG, Mercedes-Benz, Netpresenter, Panasonic, Starlux, Swissport, TrustYou, Userwerk, Zeit Online, Casacom, Innoxess | | `invert(1) hue-rotate(180deg)`: flips lightness but keeps the hue, so navy and black brand colours stay readable on the dark page |
| `co-still` (hover) | Xebia | | stays monochrome. Its only colour is the purple square behind the wordmark, and showing it filled the tile with a block |

Some source files carry a lot of empty canvas. A `--z` value on the item zooms past it inside a clipped box, and `--k` makes the box itself taller.

| Logo | Setting | Problem in the file |
|---|---|---|
| Netpresenter | wall and rows `--z: 4.6` | 1200x900 canvas with the wordmark on a fifth of its height |
| Xebia | `--z: 3.6`, tiles `2.1` | 400x400 JPG with the wordmark a quarter of the height |
| Airline Assistance | `--z: 1.9` | half the canvas height is empty |
| Innoxess, Userwerk, Aeroground, Mercedes-Benz, Neutral Base, Walt Disney | `--z` from 1.1 to 1.6 | padded canvas |

Trimming and re-exporting those files, plus giving Casacom, Innoxess, Disney and Xebia transparent backgrounds, would let every logo use the default treatment and drop most of the per-logo numbers. That is a separate upload to Ghost and not part of these cards.

On phones there is no hover, so the logos stay monochrome there. That seems right for a page this quiet.
