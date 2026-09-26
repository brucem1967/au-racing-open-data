# Victorian harness sectionals — trip geometry

Per-runner trip data extracted from Harness Racing Victoria's public
sectional reports: where each horse was, and how wide it was, at the 800m
and 400m marks, plus the metres it gained or lost across the third and
fourth quarters of the race. As far as we could determine when researching
this, this is the first time this data has been published openly and in
bulk — it otherwise exists only in per-meeting PDFs, or as a commercial
bulk feed from the timing vendor.

<!-- AUTOSTATS:BEGIN -->
**79,260 runner-rows** · 8,854 races · 24 venues · 2024-01-24 → 2026-09-24 · 3 yearly files

_Last rebuilt 2026-09-26._
<!-- AUTOSTATS:END -->

## Why this exists

In harness racing, the trip — parked outside the leader, one-out-one-back,
stuck three-wide without cover — drives results more than most of what is
publicly modelled. This dataset is a direct trip reconstruction: position
and width at two points in the race, and how much ground each horse made
or lost between them.

## Source and attribution

Extracted from sectional PDF reports Harness Racing Victoria publishes
publicly, indexed at
[thetrots.com.au/racing/sectionals/](https://www.thetrots.com.au/racing/sectionals/)
and served from an open bucket with no login. The underlying timing data
is produced by PJ Data. **Only the extracted numbers are published here —
never the PDF reports themselves, and no stewards' commentary.**

## Schema

| Column | Type | Units | Notes |
|---|---|---|---|
| `date` | date | ISO `YYYY-MM-DD` | Meeting date |
| `track_id` | string | — | Best-effort join to `track_geometry.track_id`; not guaranteed to match |
| `track` | string | — | Track name as printed on the report |
| `race` | int | — | Race number on the card |
| `distance_m` | int | metres | Race distance |
| `saddlecloth` | int | — | Runner number. Together with track/date/race, this is the reliable join key |
| `place` | int | — | Finishing position |
| `margin_m` | float | metres | Margin behind the winner |
| `position_800m_m`, `position_400m_m` | float | metres | Distance behind the leader at that mark |
| `wide_800m`, `wide_400m` | int | — | How many wide the horse was at that mark (0 = on the pegs) |
| `time` | string | `m:ss.ss` | Race time |
| `own_third_quarter_sec`, `own_fourth_quarter_sec` | float | seconds | That horse's own sectional time for the quarter |
| `gain_loss_q2_q3_m`, `gain_loss_q3_finish_m` | float | metres | Ground gained (+) or lost (−) across that quarter |

Files are sharded by year (`harness_sectionals_vic_YYYY.csv`).

## Limitations

- **No horse identity column, deliberately.** The source PDFs wrap horse
  names across lines in a way our parser cannot reliably reattach to the
  right row — a wrong name on a real result is worse than no name, so it
  is left out rather than guessed. Join to another public form source by
  `track` + `date` + `race` + `saddlecloth` if you need horse identity.
- Only the `pj` vendor layout is parsed. A second vendor (`eod`) publishes
  the same meetings in a different layout and is archived but not yet
  parsed.
- Coverage starts where the archive starts (2023 onward); it does not
  extend the record backward.
- No driver or trainer data — not published, and not extracted by the
  parser in the first place.

## Honest note on usefulness

This is a brand-new dataset in this repository, published alongside the
parser that builds it. We have not yet run the ablation that would tell us
whether trip geometry moves harness betting ROI — most individual features
tested against real settled prices on this project have not. Treat it as
an untested hypothesis with real, checkable numbers behind it, not as a
proven edge.

---

_Coverage here is partial and values are as supplied by their source. Empty means unknown, never zero. No warranty; not betting advice — see [DISCLAIMER.md](../../DISCLAIMER.md)._
