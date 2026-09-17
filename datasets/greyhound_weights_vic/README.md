# Greyhound race-day weights — Victoria

Race-day weigh-in weights, to 0.1 kg, for Victorian greyhound racing.

<!-- AUTOSTATS:BEGIN -->
**2,701 weigh-ins** · 1,428 greyhounds · 6 race day(s) · 2026-09-12 → 2026-09-17

> This dataset grows forward only — the source page is overwritten daily, so every day collected is a day that would otherwise have been lost.

_Last rebuilt 2026-09-17._
<!-- AUTOSTATS:END -->

## Why this archive exists at all

Weight matters in greyhound racing — a dog racing 1 kg above or below its
recent racing weight is a genuine form signal — and the decimal weigh-in figure
is **not published in any public form guide**. We tested that claim rather than
assuming it: a probe ran every 30 minutes across live race windows for weeks
against the public form sites, and found decimal weights in exactly none of
them.

The figures are published on race day on the controlling body's weight-sheet
pages, and then **overwritten**. There is no historical archive anywhere. Miss
a day and it is gone.

So this dataset **only grows forward**. It starts the day the collection
started and it will never contain the days before it. That is a limitation we
cannot fix; publishing it is the only way to stop it happening again.

## Schema

| Column | Type | Units | Notes |
|---|---|---|---|
| `date` | date | ISO `YYYY-MM-DD` | The race day the weights were published |
| `greyhound` | string | — | Dog name, uppercase as published |
| `weight_kg` | float | kilograms | Weigh-in weight, 0.1 kg precision |

`greyhound_weights_vic.csv` is every day concatenated. `daily/YYYY-MM-DD.csv`
holds each day as captured, so a bad capture can be identified rather than
silently smeared through the combined file.

## Limitations, stated plainly

- **Victoria only.**
- **No history before the start date above** — see the explanation above.
- The date is the day the source page was captured. A capture failure means a
  missing day, which you can see in `daily/`.
- Dog names are not unique identifiers across years.
- No race or box is attached — the source publishes weights by dog for the
  meeting. Join to results data on `date` + `greyhound`.

## Contributing history

If you have archived weight sheets from before this dataset starts, that is
genuinely valuable and we would like to include them with credit. Open an
issue.

---

_Coverage here is partial and values are as supplied by their source. Empty means unknown, never zero. No warranty; not betting advice — see [DISCLAIMER.md](../../DISCLAIMER.md)._
