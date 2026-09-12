# Contributing

Contributions are welcome, and corrections are welcome most of all.

## If a number looks wrong

Open an issue with the `track_id` (or the date and dog) and what you believe
the right value is. Every value in `track_geometry` carries a provenance string
in `track_geometry_sources.csv` — quote it in the issue and we can go back to
the source. If the source itself is wrong, we would like to know that too.

## If you run a racing club

We would genuinely like to include your track properly, and we will credit your
club by name. Useful fields: circumference, turn radius (per turn if they
differ), camber, home-straight length, distance to the first turn, surface, and
for greyhound venues the sprint-lane arrangement and estimated first-split
distances.

Your personal details will never be published — provenance records the
organisation and the date, and the build automatically strips names, email
addresses and phone numbers.

## If you have historical data

The Victorian greyhound weights dataset can only grow forward, because the
source page is overwritten daily. If you archived those pages, your archive is
more valuable than anything we can collect now. Same for older Queensland
sectionals.

## If you want to add a dataset

Open an issue first, because the bar is deliberately specific:

1. It must be lawfully republishable. Anything under a wagering-conditioned API
   key, a UK database right, exchange terms, or an explicit no-republication
   term is out — see the exclusions in the main README.
2. It must carry provenance. A value with no source does not go in.
3. Absent must mean absent. No imputation, no defaults, no filling a gap to
   make a table look complete.

## Code

Code is MIT. Keep the loader dependency-free — plenty of people want the data
without a pandas install.
