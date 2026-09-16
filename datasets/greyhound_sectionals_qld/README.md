# Greyhound GPS sectionals — Queensland

Per-run GPS tracking data for Queensland greyhound racing: the 50-metre split
time, the dog's position at that point, **how far off the rail it was running**,
and its top speed for the run.

<!-- AUTOSTATS:BEGIN -->
**24,594 runs** · 3,462 greyhounds · 5 venues · 2025-10-01 → 2026-09-14

_Last rebuilt 2026-09-16._
<!-- AUTOSTATS:END -->

## Why it matters

Sectional times tell you how fast; **distance off the rail** tells you how far.
A dog that runs 2.9 m off the rail through the first turn covers measurably
more ground than one hugging it, and that difference is invisible in a finish
time. Queensland publishes this from trackside GPS, one CSV per meeting — so
the data is public, but nobody aggregates it into something you can model with.
This is that aggregation.

## Source and terms

Racing Queensland publishes these as open data — their own terms state the data
is free to use without copyright restriction. We fetch the per-meeting CSVs,
re-key them into the schema below, and publish the values. We do not mirror
their files.

## Schema

| Column | Type | Units | Notes |
|---|---|---|---|
| `date` | date | ISO `YYYY-MM-DD` | Meeting date |
| `track` | string | — | RQ venue identifier |
| `race` | string | — | Race number as published, e.g. `Race 08` |
| `greyhound` | string | — | Dog name, uppercase as published |
| `box` | int | — | Starting box |
| `split_50m_sec` | float | seconds | Time to the 50 m mark |
| `position_50m` | int | — | Running position at 50 m |
| `rail_distance_50m_m` | float | metres | Distance off the rail at 50 m |
| `top_speed_kmh` | float | km/h | Peak speed recorded for the run |
| `finish_position` | int | — | Final placing |

One row per greyhound per run. Sorted by date, track, race, dog.

## Coverage and limitations

- Five Queensland venues carry the GPS system; other RQ meetings are absent.
- Coverage begins late 2025 and continues forward; it is refreshed daily with a
  short lookback, so recent meetings can appear a day or two after running.
- Empty cells mean the value was not in the source file. Nothing is imputed.
- Dog names are the join key and are not unique across time — two dogs can share
  a name years apart. Join on `date` + `track` + `race` + `greyhound` for a run.
- We publish what the source published. Where the GPS dropped a reading, the
  row carries a gap rather than a guess.

## Ideas nobody has tested publicly

- Does rail distance at 50 m predict the final margin once box and track are
  controlled for?
- Do some tracks systematically punish wide runners more than others? Join to
  `track_geometry` on `track` → `track_id`.
- Is top speed or time-to-50m the better early-form signal?

We tested variants of the first two on our own book and found **no profitable
edge** — which is a result worth publishing, and worth someone else checking
with better methods.

---

_Coverage here is partial and values are as supplied by their source. Empty means unknown, never zero. No warranty; not betting advice — see [DISCLAIMER.md](../../DISCLAIMER.md)._
