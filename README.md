# The World Today — 19 November 2026 (round 2)

A 1024x1024 newspaper front page summing up Thursday 19 November 2026 in
six stories, drawn flat with Python's Pillow library. No AI imagery, no faces.

## Stories

1. **Diplomacy** — Trump, Xi and Putin meet in Shenzhen, the first three-way
   talks of the nuclear powers. No deal is expected.
2. **Justice** — The ICJ delivers its judgment in The Gambia v. Myanmar today,
   the first time a state could be found guilty of genocide. No outcome is
   claimed: the judgment was still being read when this page was made.
3. **Culture** — GTA VI launches worldwide: 99 on Metacritic, a record 17m
   pre-orders worth $1.65bn before launch day.
4. **Gulf** — Iranian drones target US sites in Kuwait and Bahrain overnight;
   both are intercepted after the US hit Qeshm Island.
5. **Ukraine** — The Crimean Bridge is struck a third time in a week; traffic
   halts hours before Putin's Shenzhen talks.
6. **Tech** — Anthropic debuts on Nasdaq as ANT after a record $81.3bn IPO
   priced at $83 a share, valuing the company at about $1.5tn.

Sources: Reuters, BBC, AP, Sensor Tower, PYMNTS, The Guardian.

## Run

`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`), verifying its sha256 first. Python standard library
only, no network access, deterministic: running it twice produces
byte-identical output.
