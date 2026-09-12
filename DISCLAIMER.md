# Disclaimer

Please read this before relying on anything in this repository.

## This data is incomplete, and always will be

These datasets are published **as they are**, not as they ought to be. Coverage
is partial in ways that matter:

- **Track geometry covers 152 venues, but no venue has every field.** Turn
  radius exists for about half; camber for a handful. The measurements came
  from asking 111 clubs and state bodies — 70 replied, 67 sent data, and 41
  have never answered. Thoroughbred venues were not part of that campaign at
  all, so their geometry is mostly derived from OpenStreetMap traces.
- **Greyhound sectionals cover five Queensland venues**, not Australian
  greyhound racing generally, and only from late 2025.
- **Victorian weigh-in weights start the day collection started.** The source
  page is overwritten daily, so the history before that does not exist anywhere
  and cannot be recovered.
- **Weather is modelled reanalysis for a point**, not on-course instrument
  readings.

Empty cells are everywhere, and they are deliberate: **if a value was not
sourced, it is absent — never estimated, interpolated or defaulted**. An empty
cell is information. Treat it as "unknown", never as zero.

Coverage grows: the collection campaign is still running and re-contacts venues
with missing fields, and the datasets rebuild nightly. What you see today is a
snapshot, not a finished work.

## Accuracy

Values are published **as supplied by the source**. Where a club told us the
turn radius, that is what is recorded — we have not surveyed any track
ourselves, and we cannot independently verify what a club reports. Different
venues measured different things in different decades to different standards.

`track_geometry_sources.csv` exists precisely so you can judge this for
yourself: every value carries its own provenance, and you can filter to
`club_or_body_direct` if you only want figures confirmed by the organisation
that owns the track. OpenStreetMap-derived geometry is a circle fit to a
hand-traced way — good enough to rank tracks, not survey-grade.

If you find an error, please
[open an issue](https://github.com/brucem1967/au-racing-open-data/issues). If
you are a club and want a value corrected or removed, say so and it will be
done — no argument, same day where possible.

## No warranty

This data is provided "as is", without warranty of any kind, express or
implied. No guarantee is made as to accuracy, completeness, fitness for any
purpose, or continued availability. Use it at your own risk. The publishers
accept no liability for any loss or damage arising from its use.

The daily rebuild can fail, a source can change format, or a feed can
disappear. The build is designed to fail loudly rather than publish something
wrong — but check the dates in the dataset cards before assuming you have
current data.

## Not betting advice

This is raw research data, published for research. It is **not** betting
advice, tipping, a system, or a suggestion that any of it predicts race
outcomes.

Being blunt about our own results: most features tested from this data on a
real book showed **no profitable edge at all**. That is part of why it is
public. If you gamble, gamble with money you can afford to lose. In Australia,
free and confidential help is available on **1800 858 858** or at
[gamblinghelponline.org.au](https://www.gamblinghelponline.org.au/).

## Privacy

No personal data is published. The people at racing clubs who supplied these
figures are not named: email addresses, phone numbers, personal names and
internal file paths are stripped automatically before publication, and the
build **fails** rather than publishes if any survive. Organisations are named,
because organisations deserve the credit.

If you believe any personal information has slipped through, please report it
and it will be removed immediately.

## Sources and third-party terms

Each dataset card names its source and licence. Some data originates from
organisations that publish it openly; the rest was volunteered directly. Data
that could not be lawfully republished is deliberately excluded — see
"What is deliberately not here" in the [README](README.md).

Nothing here is endorsed by, affiliated with, or published on behalf of any
racing club, controlling body, wagering operator or data vendor.

## Licence, in plain terms

Data is [ODC-BY 1.0](LICENSES/ODC-BY-1.0.txt); code is MIT; the
OpenStreetMap-derived geometry file is ODbL. Attribution is the only thing
asked in return — and under Australian law, facts like these carry no
copyright anyway, so that request is a norm rather than a threat.
