# The World Today — 19 November 2026

make.fun `news-image-20261119` entry: one image summing up the world's news of
Thursday 19 November 2026.

## The image

`entry.png` (1024×1024, 96,778 bytes) is a hand-drawn newspaper front page —
navy masthead "THE WORLD TODAY" with the date, then six story tiles:

1. **Diplomacy · Shenzhen** — Trump, Xi and Putin meet at APEC, the summit's
   first three-way talks.
2. **Justice · The Hague** — the ICJ delivers its verdict in The Gambia v.
   Myanmar over the Rohingya.
3. **Culture · Worldwide** — Grand Theft Auto VI launches after a 13-year wait.
4. **Economy · London** — UK inflation eases to 3.6%, the first fall in five
   months, ahead of next week's Budget.
5. **Defence · UK waters** — Russian vessel Yantar tracked off UK waters;
   lasers aimed at RAF pilots.
6. **Space · NASA** — NASA confirms Voyager 1 is one light-day away, 16bn
   miles out.

Every story is an event of 19 November 2026, verified against that day's
reporting (BBC, AP, Reuters, NASA, ICJ, ONS, The Guardian). The image was
drawn with PIL from a throwaway script; no AI imagery, no faces.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), checking the file's
sha256 before writing. No network; both runs write the same bytes.

Run it with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.
