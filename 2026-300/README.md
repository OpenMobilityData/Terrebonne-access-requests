# Access request 2026-300 — Terrebonne / Kensington counter, hourly record by direction

**Public body:** Arrondissement de Côte-des-Neiges–Notre-Dame-de-Grâce, Division du greffe
**Filed:** May 6, 2026
**Answered:** June 4, 2026, by the secrétaire d'arrondissement
**Released:** one spreadsheet (hourly counts) with the response letter and the notice of recourse

## What was asked

All traffic count data held by the borough for any location along rue de Terrebonne, for all vehicle types recorded, from July 26, 2025 to May 11, 2026. The request continues [2025-697](../2025-697/), which obtained the same counter's record to December 2025 and the equipment documentation.

## What was released

| File | Content |
|---|---|
| [`raw/response_2026-06-04.pdf`](raw/response_2026-06-04.pdf) | The borough's response letter |
| [`raw/26072025_11052026.xlsx`](raw/26072025_11052026.xlsx) | "Comptage permanent Terrebonne": hourly counts from the Eco-Counter ZELT EVO inductive-loop counter on Terrebonne at Kensington, July 26, 2025 08:58 to May 11, 2026 08:58 — bicycles total, bicycles eastbound (`IN_est`), bicycles westbound (`OUT_ouest`), motor vehicles |

Nothing was withheld. The response was given within the statutory delay.

## What the record shows, in brief

- Summed to days, the hourly record reconciles exactly with the daily totals the borough released on October 9, 2026 in [2026-581](../2026-581/) (bundle 01, [pp. 74–81](https://openmobilitydata.github.io/Terrebonne-access-requests/2026-581/raw/01_emails_mandate_counts.pdf#page=74)): December 1 – March 31, 4,891 bicycle trips, 2,783 eastbound and 2,108 westbound.
- The eastbound/westbound split is balanced (49–53 % eastbound) in every month from July 2025 to February 2026 and shifts to 59–70 % eastbound from March 2026. A citizen Telraam camera on the same street at King-Edward agrees with the loop's eastbound channel through March but records westbound days of 80–190 bicycles where the loop records 10–40. The loop's westbound detection appears to have degraded around March 1, 2026; counts from that date should be read as lower bounds. Asked on October 13, 2026 whether the counter was serviced, moved or re-tuned, the borough's engineering division replied on October 15 that nothing was done to the loop between mid-February and mid-March 2026, that the only recorded intervention is a battery replacement in early June, and that a snowbank on the westbound side may have altered where people rode; the westbound counts from March 1 remain lower bounds (see the note's Limits section).
- Motor vehicles: about 1,360 a day over the first year (monthly means 1,090–1,600), one-way.

## Derived files

The analysis *Winter cycling on rue de Terrebonne and the days snow is loaded* joins this record to Environment Canada daily weather and to the City's open record of snow-removal truckloads, and measures how many eastbound trips would have been ridden in mixed traffic under an all-winter lane conversion and under a closure limited to snow-loading days. Each derived document carries a version tag `YYYY-MM-DD-hh-mm-ss` (America/Toronto) in the page footer and the PDF Subject.

| File | Content |
|---|---|
| [`derived/Terrebonne_2026-300_winter_exposure_en.pdf`](derived/Terrebonne_2026-300_winter_exposure_en.pdf) (+ `.tex`) | The analysis, English (original, six pages) |
| [`derived/Terrebonne_2026-300_winter_exposure_fr.pdf`](derived/Terrebonne_2026-300_winter_exposure_fr.pdf) (+ `.tex`) | L'analyse, version française (traduction ; l'anglais fait foi) |
| `derived/exposure_analysis.py` | Regenerates every table and the figure from the files below (`python3 exposure_analysis.py`; needs pandas, openpyxl, matplotlib) |
| `derived/exposure_tables.txt` | The script's printed output |
| `derived/exposure_winter_2025-26.pdf` / `.png` | Figure 1: daily eastbound trips and snowfall, Dec 1 2025 – Mar 31 2026 |
| `derived/kensington_daily_directional.csv` | The hourly record summed to days: bicycles total, eastbound, westbound, motor vehicles |
| `derived/kensington_weather_loading_daily_2025-12_2026-03.csv` | Daily working table: directional counts, ECCC snowfall / snow on ground / temperature, borough and sector CDN-301 loading activity |
| `derived/loading_daily.csv` | City snow-removal transactions summed to loads and m³ per season × day × borough × sector, 2015-16 to 2025-26 (source: [Contrats et transactions de déneigement](https://donnees.montreal.ca/dataset/contrats-transaction-deneigement), CC-BY 4.0) |
| `derived/en_climate_daily_QC_7025251_2025_P1D.csv`, `..._2026_P1D.csv` | Environment and Climate Change Canada daily data, Montréal/Pierre Elliott Trudeau Intl A, as downloaded |
| `derived/terrebonne_sector.py` | Point-in-polygon lookup of the City's snow-removal sector containing Terrebonne (sector polygons from [Secteurs de déneigement](https://donnees.montreal.ca/dataset/secteur-deneigement); download the season's GeoJSON separately) |

## Timeline

| Date | Event |
|---|---|
| 2025-07-26 | Counter in service at Kensington |
| 2025-11-27 / 2025-12-19 | Request 2025-697 filed / answered (record to December 2025, equipment sheets) |
| 2026-05-06 | This request filed |
| 2026-06-04 | This response |
| 2026-10-09 | Daily totals from the same counter released again in 2026-581, bundle 01, pp. 74–81 |
