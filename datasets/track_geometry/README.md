# Track geometry — Australian racing venues

Physical measurements of Australian greyhound, harness and thoroughbred
tracks: turn radii, circumferences, home-straight lengths, cambers, surfaces,
sprint lanes, and Greyhound Racing Victoria's estimated first-split distances.

**We could not find another public dataset of racing-track geometry anywhere.**
If one exists, please open an issue — we would rather link to it than duplicate
it.

<!-- AUTOSTATS:BEGIN -->
**152 venues** · 25 greyhound · 62 harness · 65 thoroughbred · **102 club/body-confirmed** · 675 sourced values (251 direct from a club or controlling body)

| Measurement | Venues with a value |
|---|---|
| Turn radius | 75 (49%) |
| Circumference | 87 (57%) |
| Home straight | 47 (31%) |
| Sprint lane | 49 (32%) |
| Surface | 12 (8%) |
| Camber | 6 (4%) |
| Distance to first turn | 4 (3%) |

Plus **42 GRV first-split distances** across 13 Victorian greyhound venues, and 84 venues with OpenStreetMap-derived geometry (separately licensed).

_Last rebuilt 2026-09-21._
<!-- AUTOSTATS:END -->

## Why this is unusual

Track geometry decides how a race is run — a tight first turn punishes a wide
draw, a long home straight rewards a stayer, camber changes what a fast section
costs — and almost none of it is published. Broadcast graphics show a track
map; nobody publishes the radius of the bend.

So we asked. Between August and September 2026 we wrote to **111 racing clubs
and state controlling bodies** (53 greyhound, 58 harness), explained what was
wanted and why, and asked whether they had it. **Seventy replied; 67 supplied
data**, including Greyhound Racing Victoria, who sent a complete first-split
distance table covering all 13 Victorian greyhound venues. That correspondence
is what the `club_or_body_direct` rows in the sources file represent.

Where no club data exists, some geometry is derived from OpenStreetMap traces
(perimeter, straight bearings and a least-squares circle fit for turn radius).
Those values are kept in a **separate file with a different licence** — see
below.

## Files

| File | Rows | Licence | Contents |
|---|---|---|---|
| `track_geometry.csv` | one per venue | ODC-BY | Club- and body-sourced measurements plus venue identity |
| `track_geometry_sources.csv` | one per field per venue | ODC-BY | **The provenance of every single value** — who supplied it and when |
| `track_first_split_distances.csv` | one per venue per race distance | ODC-BY | GRV estimated first-split distance and split record, 13 VIC greyhound venues |
| `track_turn_radii.csv` | one per turn | ODC-BY | Per-turn radii where a venue supplied more than one |
| `track_geometry_osm_derived.csv` | one per venue with an OSM trace | **ODbL** | OpenStreetMap-derived geometry — see licence note |

## Schema: `track_geometry.csv`

| Column | Type | Units | Notes |
|---|---|---|---|
| `track_id` | string | — | Join key. Greyhound venues are prefixed `GR:` |
| `code` | string | — | `GR` greyhound, `H` harness, `TB` thoroughbred |
| `code_name` | string | — | Long form of `code` |
| `latitude`, `longitude` | float | degrees | Venue centroid where sourced |
| `geometry_trusted` | bool | — | `True` when a club or body confirmed the geometry |
| `circumference_m` | float | metres | Lap distance |
| `turn_radius_m` | float | metres | Bend radius; see `track_turn_radii.csv` for per-turn values |
| `camber_pct` | float | percent | Bank of the turn |
| `home_straight_m` | float | metres | Winning-post straight length |
| `first_turn_m` | float | metres | Distance from a common start to the first turn |
| `run_home_m` | float | metres | Final straight run where distinct from `home_straight_m` |
| `surface` | string | — | e.g. grass, loam, synthetic |
| `sprint_lane` | bool/string | — | Greyhound sprint-lane presence |
| `straight_track` | bool | — | Straight-course venues |
| `geometry_note`, `camber_note`, `first_turn_note` | string | — | Our own notes, usually explaining why a value is absent |

## The rule that makes this dataset trustworthy

**If a value was not sourced, it is absent. It is never estimated,
interpolated, or defaulted.**

That rule came from the models this data feeds: a guessed camber produces a
confident wrong answer, while a missing camber produces an honest refusal. So
expect empty cells — they are information, not damage. `track_geometry_sources.csv`
records the reason, including values recorded as explicitly *not published* by
the club.

Coverage is uneven by design: greyhound and harness venues were the campaign's
focus, thoroughbred venues are mostly OSM-derived, and the campaign is still
running — clubs with missing fields are re-contacted on a 60-day cycle, so
coverage grows.

## Licence note — please read before merging the files

- Everything except `track_geometry_osm_derived.csv` is **ODC-BY 1.0**.
- `track_geometry_osm_derived.csv` is derived from **OpenStreetMap** and is
  therefore **ODbL 1.0**, © OpenStreetMap contributors. ODbL carries a
  share-alike obligation that ODC-BY does not.
- They are separate files so that **merging is your explicit choice**. If you
  join them, treat the result as ODbL.

## Known limitations

- Values come from many sources, measured to different standards and eras. The
  provenance file is there so you can filter to `club_or_body_direct` if you
  want only confirmed measurements.
- OSM-derived turn radii are a circle fit to a hand-traced way. Good enough to
  rank tracks; not survey-grade.
- Venue identity is our own `track_id`, not an official code. GRV venue codes
  appear in `track_first_split_distances.csv` as `venue_codes`.
- Personal names, email addresses and phone numbers are stripped from
  provenance automatically — you will see `[name removed]` where a person
  answered on behalf of a club. The organisation is retained, because the
  organisation deserves the credit.

## Credit where it is owed

This dataset exists because staff at dozens of racing clubs — people with
actual jobs to do — took the time to look up a number for a stranger who
emailed them. If you use this data, that is who you are really thanking.

---

_Coverage here is partial and values are as supplied by their source. Empty means unknown, never zero. No warranty; not betting advice — see [DISCLAIMER.md](../../DISCLAIMER.md)._
