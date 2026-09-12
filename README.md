# Australian Racing Open Data

Open, machine-readable datasets for Australian racing — the kind of data that
normally sits behind a login, a paywall, or nowhere at all.

Two of these datasets, as far as we can tell, have never existed publicly
before: **track geometry** (turn radii, cambers, straight lengths, first-split
distances — gathered by writing to 111 racing clubs and state bodies) and
**greyhound GPS sectionals** at 50-metre resolution.

Everything here is rebuilt and pushed **every day**. Nothing here is derived
from a source that forbids republication — see
[What is deliberately not here](#what-is-deliberately-not-here).

> **Read this first:** this data is **incomplete by nature** and published as
> it is, not as it ought to be. Coverage is partial, empty cells mean *unknown*
> (never zero), values are as supplied by their source and not independently
> verified, there is **no warranty**, and none of it is betting advice.
> Full terms: **[DISCLAIMER.md](DISCLAIMER.md)**.

<!-- AUTOSTATS:BEGIN -->
**142,688 rows across 152 venues, 3,446 greyhounds and 116,832 venue-days of weather** — 9.6 MB of CSV, rebuilt 2026-09-12.

| Dataset | Rows | Coverage |
|---|---|---|
| Track geometry | 152 venues, 675 sourced values | 102 club/body-confirmed |
| Greyhound sectionals (QLD) | 24,446 runs | 2025-10-01 → 2026-09-10 |
| Greyhound weights (VIC) | 457 weigh-ins | 1 race day(s), forward-only |
| Track weather | 116,832 venue-days | 2020-01-01 → 2026-08-30 |
<!-- AUTOSTATS:END -->

## The datasets

| Dataset | What it is | Why it's hard to get elsewhere |
|---|---|---|
| [`track_geometry`](datasets/track_geometry/) | Turn radii, circumferences, home-straight lengths, cambers, surfaces, sprint lanes and GRV first-split distances for Australian greyhound, harness and thoroughbred venues | No public source exists. Every value was supplied by a club or state body, or derived from OpenStreetMap, and **each one carries its own provenance string** |
| [`greyhound_sectionals_qld`](datasets/greyhound_sectionals_qld/) | Per-run GPS sectionals from Racing Queensland: 50 m split time, position, distance off the rail, top speed | Published as one CSV per meeting, in a format nobody aggregates |
| [`greyhound_weights_vic`](datasets/greyhound_weights_vic/) | Race-day weigh-in weights to 0.1 kg, Victoria | The source page is overwritten daily — miss a day and it is gone forever. This archive only grows forward |
| [`track_weather`](datasets/track_weather/) | Daily weather at racing venues since 2020: rain, temperature range, wind and gust maxima | Weather archives are not keyed to racetracks; these are joined to sourced venue coordinates |

Each dataset directory has its own README with the full schema, coverage,
collection method, known gaps and licence.

## Quickstart

```bash
git clone https://github.com/brucem1967/au-racing-open-data.git
cd au-racing-open-data
python3 examples/quickstart.py
```

With pandas:

```python
import pandas as pd

geom = pd.read_csv("datasets/track_geometry/track_geometry.csv")
sect = pd.read_csv("datasets/greyhound_sectionals_qld/greyhound_sectionals_qld.csv")

# Does a tighter first turn slow the 50 m split?
qld = sect.merge(geom, left_on="track", right_on="track_id", how="left")
print(qld.groupby("track")[["split_50m_sec", "turn_radius_m"]].mean())
```

There is also a dependency-free loader in [`python/`](python/) if you would
rather not install anything:

```python
from au_racing_open import load
rows = load("greyhound_sectionals_qld")   # list[dict], stdlib only
```

## Licence and attribution

- **Data: [ODC-BY 1.0](LICENSES/ODC-BY-1.0.txt)** — use it commercially, build
  on it, just credit it.
- **Code in this repo: MIT.**
- **Attribution string:** `Australian Racing Open Data (PandaVision), ODC-BY 1.0`

One important carve-out: `track_geometry_osm_derived.csv` contains values
derived from **OpenStreetMap** and is therefore **ODbL**, not ODC-BY. It is a
separate file precisely so you can take the club-sourced measurements without
inheriting share-alike terms. Details in the
[dataset card](datasets/track_geometry/).

Under Australian law facts are not copyrightable and computer-generated
compilations attract no copyright at all. The licence here is therefore best
read as **the credit norm we ask you to honour**, not a claim of ownership over
the facts.

## What is deliberately not here

Publishing everything we hold would be easy and wrong. These are excluded on
purpose, and the exclusions are enforced in the build script rather than by
good intentions:

- **Anything from a wagering-conditioned API key** — republication would breach
  the terms that key was issued under.
- **UK greyhound (GBGB) data** — the UK has a *sui generis* database right that
  Australia does not, and it binds downstream users too.
- **Betting exchange price/stream data** — expressly prohibited by the
  exchange's terms.
- **Commercial form-site scrapes** — explicit no-republication terms.
- **Source artefacts** — the club PDFs, spreadsheets and vendor reports behind
  these numbers stay private. We publish the **values**, re-keyed into our own
  schema.
- **Personal data** — the people at 111 clubs who answered an email are not
  part of this dataset. Their addresses, phone numbers and names are stripped
  automatically, and the build **fails** if any survive.

## How it stays fresh

The datasets are rebuilt from source every day by a scheduled job and pushed
here automatically. The build refuses to publish if an exporter fails, if a
forbidden source appears in the output, or if anything resembling personal data
survives the scrub — so a stale dataset is visible rather than a wrong one
being silently shipped.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) if you spot an error, have data to
add, or run a club that would like its track measured properly.

## Why this exists

This data was collected to build racing models. Most of the features tested
from it have shown **no betting edge at all** — which is exactly why it should
be public: it is more useful to a community of researchers than it is sitting
on one machine. If you find something in here we missed, we would genuinely
like to hear about it.

## Disclaimer

Short version: incomplete coverage, no warranty, values as supplied and not
independently verified, empty means unknown, not betting advice, no personal
data, corrections welcome and acted on. The full text is in
**[DISCLAIMER.md](DISCLAIMER.md)** — worth two minutes before you build
anything on this.

## Citation

See [`CITATION.cff`](CITATION.cff), or:

> Australian Racing Open Data (PandaVision), ODC-BY 1.0.
> https://github.com/brucem1967/au-racing-open-data
