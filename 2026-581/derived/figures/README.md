# Figures drawn from the counter's daily table (`../kensington_daily_borough_release_2025-07_2026-08.csv`)

Each subfolder holds one figure type, its script, and the PNG and SVG in English (`_en`) and French (`_fr`). Run a script inside its own folder; it reads the CSV two levels up and rewrites its figures.

| Folder | Figure |
|---|---|
| `kensington-monthly/` | Mean bicycle passages per day by calendar month, August 2025 to July 2026, with the December–March window marked |
| `kensington-histograms/` | Histograms of the daily totals, winter days over the rest of the first year: absolute (days per bin) and normalized (share of each season's days) |
| `kensington-violins/` | Violin plots of the daily totals: winter beside the rest of the year on one axis; and each season alone on its own axis |
