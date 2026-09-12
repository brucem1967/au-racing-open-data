#!/usr/bin/env python3
"""Five things you can do with this data in under a minute. No dependencies.

    python3 examples/quickstart.py
"""
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "python"))
from au_racing_open import load, describe, datasets   # noqa: E402


def main():
    print("Datasets available:", ", ".join(datasets()), "\n")

    # 1. What is actually in the flagship dataset?
    info = describe("track_geometry")
    print(f"1. track_geometry: {info['rows']} venues")
    interesting = ("turn_radius_m", "circumference_m", "home_straight_m",
                   "camber_pct", "surface")
    for col in interesting:
        print(f"     {col:18s} populated for {info['populated_pct'].get(col, 0):5.1f}% of venues")

    # 2. Turn radius by code — greyhound tracks are tighter than harness tracks.
    geom = load("track_geometry")
    by_code = defaultdict(list)
    for row in geom:
        if row.get("turn_radius_m"):
            by_code[row["code_name"] or row["code"]].append(row["turn_radius_m"])
    print("\n2. Mean turn radius by code")
    for code, vals in sorted(by_code.items()):
        print(f"     {code:14s} {sum(vals)/len(vals):6.1f} m   (n={len(vals)})")

    # 3. GRV first-split distances: how far is the "first split" really?
    splits = load("track_first_split_distances")
    if splits:
        print("\n3. GRV first-split distance by race distance (VIC greyhounds)")
        by_dist = defaultdict(list)
        for row in splits:
            if row.get("first_split_distance_m"):
                by_dist[row["race_distance_m"]].append(row["first_split_distance_m"])
        for dist, vals in sorted(by_dist.items(), key=lambda kv: (kv[0] is None, kv[0]))[:6]:
            print(f"     {dist} m race -> first split at {sum(vals)/len(vals):6.1f} m "
                  f"(n={len(vals)} venues)")

    # 4. Does running wide at 50m cost you? (One line of honest analysis.)
    sect = load("greyhound_sectionals_qld")
    wide, tight = [], []
    for row in sect:
        rail, finish = row.get("rail_distance_50m_m"), row.get("finish_position")
        if rail is None or finish is None:
            continue
        (wide if rail >= 3.0 else tight).append(finish)
    if wide and tight:
        print(f"\n4. Mean finish position, QLD greyhounds ({len(wide)+len(tight)} runs)")
        print(f"     running >=3.0 m off the rail at 50 m: {sum(wide)/len(wide):.2f}  (n={len(wide)})")
        print(f"     running < 3.0 m off the rail at 50 m: {sum(tight)/len(tight):.2f}  (n={len(tight)})")
        print("     (raw means — not controlled for box, track or class. Do it properly!)")

    # 5. Join weather to venues.
    weather = load("track_weather")
    tracks = {row["track_id"] for row in weather}
    days = {row["date"] for row in weather}
    print(f"\n5. track_weather: {len(weather):,} rows, {len(tracks)} venues, "
          f"{len(days):,} days ({min(days)} to {max(days)})")

    print("\nEverything above is stdlib only. With pandas, see the README.")


if __name__ == "__main__":
    main()
