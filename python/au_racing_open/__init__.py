"""au_racing_open — a dependency-free loader for Australian Racing Open Data.

Stdlib only, on purpose: plenty of people want to look at a racing dataset
without creating a virtualenv and installing pandas first.

    from au_racing_open import load, datasets, describe

    datasets()                       # what's available
    rows = load("track_geometry")    # list[dict], numbers already parsed
    describe("greyhound_sectionals_qld")

Every value that looks numeric is converted to int/float; an empty cell becomes
None rather than 0 or "" — in these datasets absent genuinely means absent, and
collapsing that distinction is the single easiest way to get a wrong answer.
"""
from __future__ import annotations

import csv
import glob
import os

__version__ = "1.0.0"

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_DATASETS = {
    "track_geometry": "datasets/track_geometry/track_geometry.csv",
    "track_geometry_sources": "datasets/track_geometry/track_geometry_sources.csv",
    "track_geometry_osm": "datasets/track_geometry/track_geometry_osm_derived.csv",
    "track_first_split_distances": "datasets/track_geometry/track_first_split_distances.csv",
    "track_turn_radii": "datasets/track_geometry/track_turn_radii.csv",
    "greyhound_sectionals_qld": "datasets/greyhound_sectionals_qld/greyhound_sectionals_qld.csv",
    "greyhound_weights_vic": "datasets/greyhound_weights_vic/greyhound_weights_vic.csv",
    # Sharded by year; load() concatenates them in date order.
    "track_weather": "datasets/track_weather/track_weather_*.csv",
}


def datasets() -> list[str]:
    """Names accepted by load()."""
    return sorted(_DATASETS)


def _coerce(value: str):
    if value == "":
        return None
    low = value.strip().lower()
    if low in ("true", "false"):
        return low == "true"
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def paths(name: str) -> list[str]:
    if name not in _DATASETS:
        raise KeyError(f"unknown dataset {name!r}; try one of {datasets()}")
    pattern = os.path.join(_ROOT, _DATASETS[name])
    found = sorted(glob.glob(pattern))
    if not found:
        raise FileNotFoundError(
            f"no files for {name!r} at {pattern} — run this from a clone of "
            f"the repository, or pass the path directly to csv.DictReader")
    return found


def load(name: str, raw: bool = False) -> list[dict]:
    """Load a dataset as a list of dicts. `raw=True` keeps every value a str."""
    rows: list[dict] = []
    for path in paths(name):
        with open(path, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                rows.append(row if raw else
                            {k: _coerce(v) for k, v in row.items()})
    return rows


def describe(name: str) -> dict:
    """Row count, columns, and how populated each column actually is.

    Coverage is printed because these datasets are deliberately sparse: a
    column that is 12% populated is telling you something true about how much
    of Australian racing publishes that measurement.
    """
    rows = load(name)
    cols = list(rows[0]) if rows else []
    filled = {c: sum(1 for r in rows if r.get(c) is not None) for c in cols}
    info = {
        "dataset": name,
        "rows": len(rows),
        "columns": cols,
        "populated_pct": {c: round(100.0 * n / len(rows), 1) if rows else 0.0
                          for c, n in filled.items()},
        "files": [os.path.relpath(p, _ROOT) for p in paths(name)],
    }
    return info
