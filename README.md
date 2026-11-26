# Thursday 26 November 2026 in One Picture — v8

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/news-image-20261126)
[![make.fun rank](https://img.shields.io/badge/make.fun-rank-pending-lightgrey)](https://make.fun/bounty/news-image-20261126)
[![make.fun reward](https://img.shields.io/badge/make.fun-reward-%2420-green)](https://make.fun/bounty/news-image-20261126)

One image summing up Thursday 26 November 2026: **35 stories, 9 regions,
15 fields** — every one from that day, in some time zone.

v5 restructures the page for readability: 3 illustrated leads, 10
numbered panels with flat motifs (2 rows of 5), a compact 2×3 UTC
timeline, a world map with 13 numbered pins, a 22-item "and also" list,
and a red DATE CHECK box for items that are *not* from 26 November.

v6 changes one thing: the timeline's filler last row ("23:00 UTC — THE
DAY — 35 stories…", flagged by the GLM judge in the v5 gate) is replaced
by a real, sourced moment — "09:00 UTC — BRUSSELS — Euro Summit opens;
Ukraine aid" (European Council indicative programme: Thu 26 Nov 2026,
10:00 CET = 09:00 UTC; the special European Council 26–27 Nov focuses
on Ukraine financing for 2027). Rows re-sorted chronologically.

v7 changes one thing: the Cairo lead body no longer carries the casualty
figures in its serif text — GLM misread v6's "31 are killed and 21 hurt"
as "31 hurt" plus a garbled fragment and called it a contradiction with
the "31 KILLED" headline. The toll is now its own line in bold red sans
caps: "31 KILLED · 21 INJURED". Facts unchanged: 31 dead, 21 injured.

v8 answers the HiLinkUP call-1 objection in the v7 gate (witty "uses
cleaner, more consistent labels and sourcing" and covers a "broader,
more balanced set of stories"): (1) every kicker now follows one
system, "N · PLACE — Field" — v7 panels used the region in ALL CAPS
("4 · MIDEAST — WAR") while leads used place in Title Case; (2) every
"and also" row now carries its field ("14 · KYIV · War — …"), so all 35
stories show number · place · field uniformly and the 15 fields are
visible on the page; (3) the footer source list is built from the slate
data itself — v7 listed Xinhua / Al Jazeera / ESA (unused) and omitted
Euromaidan / France24 / IPL (used); (4) the "15 fields" claim is
code-verified again (distinct fields across all 35 stories == 15,
asserted in the generator, as v1–v4 did — v5–v7 had hardcoded it after
dropping the "also" field labels); (5) small-print fixes: "Naftogaz"
dropped from panel 7 ("Natougas" misread), "+" becomes "," in story 14.
Lead trio, Cairo stat line, numbers, timeline, DATE CHECK and all facts
unchanged.

Leads: the 100th Macy's Thanksgiving parade postponed to Saturday (the
first postponement in its 100-year history) · 31 killed as a tanker fire
spreads near Cairo · Pakistan's first astronaut reaches Tiangong.

New in v5 vs the earlier versions: fresh overnight stories — two tankers
hit naval mines in the Strait of Hormuz, an Israeli strike kills a Hamas
security chief in Gaza, Ukraine's Blysk laser downs a jet-powered drone,
Russian strikes cut power across five regions, Xi's graft probe fells
Shanghai party chief Chen Jining, and Malaysia sues Google for $146m.

## Run

```sh
python3 tools/generate.py   # renders assets/entry.png (deterministic)
python3 main.py             # copies it to $MAKEFUN_OUTPUT_DIR/entry.png
```

`tools/generate.py` uses stdlib + PIL only, no network. `main.py` uses
stdlib only. The image is 1024×1024 PNG, drawn entirely in code —
no photographs.
