# Daily weather at Australian racing venues

Daily weather observations keyed to racing venue coordinates: rainfall,
temperature range, maximum wind and maximum gust.

<!-- AUTOSTATS:BEGIN -->
**116,832 venue-days** · 48 venues · 2020-01-01 → 2026-08-30 · 7 yearly files

_Last rebuilt 2026-09-20._
<!-- AUTOSTATS:END -->

## Why keyed to venues

Weather archives are keyed to weather stations, not racetracks. Anyone
modelling going, track condition, or wind assistance has to do the join — pick
coordinates for each venue, fetch a series per point, and align the dates. This
dataset is that join, done once, using the same sourced venue coordinates as
the [`track_geometry`](../track_geometry/) dataset.

## Source and attribution

Historical daily weather comes from the **Open-Meteo historical archive API**,
used under its attribution terms. If you use this dataset, credit Open-Meteo as
well as this repository.

## Schema

| Column | Type | Units | Notes |
|---|---|---|---|
| `date` | date | ISO `YYYY-MM-DD` | Observation day |
| `track_id` | string | — | Joins to `track_geometry.track_id` |
| `latitude`, `longitude` | float | degrees | Point the series was fetched for |
| `precip_mm` | float | mm | Total precipitation |
| `rain_mm` | float | mm | Rain component |
| `temp_max_c`, `temp_min_c` | float | °C | Daily extremes |
| `wind_max_kmh` | float | km/h | Maximum sustained wind |
| `gust_max_kmh` | float | km/h | Maximum gust |

Files are sharded by year (`track_weather_YYYY.csv`) so you can load one season
without reading the lot.

## Limitations

- These are **gridded model reanalysis values for a point**, not on-course
  instrument readings. They describe the day's weather at the venue's location,
  not the wind down the home straight at 3:40pm.
- Daily resolution only. Race-time conditions are not in here.
- Venue coordinates carry whatever precision the geometry dataset has; a few
  are town-level rather than exact.
- No track-condition or going rating — that is a separate, differently licensed
  thing and it is not in this repository.

## Honest note on usefulness

We built this to test whether weather predicts results. On our own data it
**did not** — no measurable edge, across several framings. It is published
because a negative result from one modeller is not a negative result for
everyone, and because the venue-keyed join is worth having regardless.

---

_Coverage here is partial and values are as supplied by their source. Empty means unknown, never zero. No warranty; not betting advice — see [DISCLAIMER.md](../../DISCLAIMER.md)._
