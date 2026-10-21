# The Kensington counter: supplier revisions, the westbound channel, and what they change in the released figures

*Note of October 21, 2026, on the loop counter at Terrebonne/Kensington (Eco-Counter ZELT EVO) whose daily table was released under this request (bundle 01, [pp. 74–81](https://openmobilitydata.github.io/Terrebonne-access-requests/2026-581/raw/01_emails_mandate_counts.pdf#page=74)) and whose hourly directional record was released under [2026-300](../../2026-300/). It records an exchange with the borough's engineering division and, through it, with the counter's supplier, and states the effect of what was learned on every figure drawn from the two releases.*

## 1. The question put to the borough

The counter reports bicycles in two directions. From July 2025 to February 2026 the two were balanced: 49 to 53 % eastbound every month. From the week of March 2, 2026 the eastbound share rose to about 70 % in March and stayed at 58 to 61 % in April and early May, after the snow was gone. Over the same months a citizen Telraam camera at King-Edward, 700 m west on the same street, kept a steady split between its two directions and recorded March days of 80 to 190 westbound bicycles where the loop recorded 10 to 40 (the camera's absolute levels are not comparable with the loop's; its directional share is). On October 13, 2026 the author asked the division, as a resident, whether the counter had been serviced, moved or re-tuned between mid-February and mid-March, and whether the borough had seen the same thing.

## 2. The division's reply of October 15, 2026

The division confirmed the wider gap from March 2026 and noted that eastbound had been slightly higher than westbound since July 2025. No maintenance, adjustment, relocation or works took place near the loop between mid-February and mid-March 2026. The only recorded intervention is a battery replacement in early June 2026, with a brief interruption whose data were reconstructed by the supplier. The division saw no evidence of a technical fault and offered a field hypothesis: a snowbank, ice or another local obstacle on the westbound side, which is the side with parked cars and, on a site visit in February 2025, the harder side to clear. It had no photographs of the site from winter 2026. (Already summarized in the [2026-300 README](../../2026-300/README.md).)

The author's follow-up of the same day sent the comparison table and asked three questions: which dates had been reconstructed after the battery replacement and by what method (the released daily table still shows May 29–31 at zero); whether the directional data since May 11, 2026 show the same split; and whether the two channels are two separate loops, one per lane.

## 3. Eco-Counter's reply of October 21, 2026, relayed by the division

The division put the questions to the supplier on October 20 and forwarded the reply of its data analyst on October 21.

**Reconstructions since July 2025, five in all:**

| Period | Kind | Series |
|---|---|---|
| Nov 21–26, 2025 (5 days) | redistribution between the IN and OUT directions | bicycles |
| Dec 25, 2025 | hourly reconstruction | bicycles |
| Mar 9–10, 2026 (2 days) | redistribution between IN and OUT | bicycles |
| May 29–31, 2026 | missing data reconstructed | bicycles |
| June 8–9, 2026 | missing data reconstructed | motor vehicles |

**Method.** For a redistribution, the site's historical ratio between IN and OUT for each day of the week is applied to the abnormal period; the daily total is kept. For missing data, the passages are estimated from nearby counters highly correlated with this one, here two counters in Verdun (Hickson/Wellington and 1re Avenue/Wellington; linear correlations of 96 % and 95 %).

**On the gap between directions.** The analyst sees no abnormal gap between the two directions of the kind described, apart from the five days of November 2025, and asks whether the observation could come from a difference with the data transmitted to the author. The site has four bicycle loops, two eastbound and two westbound. The missing data of May 2026 have been reconstructed and are in the borough's EcoVisio account; it is "pas normal" that they are still missing from the export the author received.

**What the screenshots show.** The platform holds four bicycle channels: « Rue Terrebonne Piste cyclable côté sud – vélos vers est », « … vélos vers ouest », « Rue Terrebonne – ZELT Evo Vélos IN_est » and « … OUT_ouest ». The analyst's November chart compares « côté sud – vers est » with « ZELT Evo OUT_ouest », labelled as today's data; its dashed original series shows November 21 at roughly 320 eastbound against 45 westbound before the redistribution. In the reconstruction of May 29–31 the traffic is carried by « côté sud – vers est » and « ZELT Evo OUT_ouest », while « côté sud – vers ouest » and « ZELT Evo IN_est » stay near zero.

## 4. Check against the two releases

The hourly export of June 4, 2026 ([2026-300](../../2026-300/), `raw/26072025_11052026.xlsx`, columns « Rue Terrebonne Cyclist IN_est » and « OUT_ouest ») and the daily table released October 9, 2026 under this request were compared with the supplier's list.

- **The June export contains the November redistribution.** November 21–26 show eastbound shares of 50–53 %, equal to the site's historical weekday ratio (51–53 % over July 26 – November 20), where the original series had November 21 at about 88 % eastbound. November 27 (66 %), outside the redistributed window, stands as recorded.
- **The June export does not contain the March redistribution.** March 9 and 10 stand at 82 % and 80 % eastbound (95/21 and 93/23), like the days around them (March 5: 82 %; March 7: 92 %; March 12: 84 %; March 13: 78 %). The supplier treated those two days; the sustained shift from the week of March 2 was not flagged by its validation.
- **The October table does not contain the May and June reconstructions.** May 29–31 show 0, 0 and 0 bicycles with 1,533, 1,498 and 1,320 motor vehicles: the bicycle channels were silent while the motor channel counted. June 8–9 show 267 and 783 motor vehicles, the gapped original values visible in the analyst's chart (neighbouring weekdays run 1,500–1,700).
- March 11, 2026 shows 12 bicycles and 672 motor vehicles, about half a day on the motor channel: a possible interruption not on the supplier's list.
- December 25, 2025: 10 bicycles (5 and 5) and 640 motor vehicles in both releases; whether this is the reconstructed value cannot be told from the releases.

The two releases are therefore of different vintages, and neither is identical to the supplier's current validated series.

## 5. Effect on the figures drawn from the releases

| Figure in use | Source | Effect of the listed revisions | If the westbound channel did under-record from March 2 |
|---|---|---|---|
| 4,891 bicycles, Dec 1 – Mar 31 (41 a day) | daily table | None. Redistributions keep daily totals; the December 25 value (10) is the same in both releases. | Understated in March only (December–February were balanced). March's 1,659 could be low by a few hundred. |
| 7,460, Nov 16 – Mar 31 (55 a day) | daily table | None (the November redistribution keeps totals). | As above. |
| 135,276 in the first year, Jul 26, 2025 – Jul 25, 2026 (371 a day) | daily table | Understated by the three missing days of May 29–31; neighbouring days run 650–850, so about 2,000 passages; roughly 137,000 once reconstructed. Already published as a lower bound. | Understated further. If the true split stayed near 52/48 while the record shows 58–61 % eastbound, April–May are low by about 15 %; whether that continued to July is unknown (directional data end May 11). The year could be 145,000–150,000. |
| 501,817 motor vehicles; bicycles = 27 % of motor | daily table | Motor understated by about 2,000 on June 8–9 (0.4 %). The 27 % holds. | No effect on motor; the bicycle share rises slightly. |
| 3.6 % = winter's share of the year | both | 4,891 ÷ 137,000 = 3.6 %. Unchanged at one decimal. | Falls toward 3.3 % (the denominator grows). |
| Exposure analysis (eastbound only, Dec–Mar): 2,783 eastbound; 72 % of them outside sector snow-constraint days | hourly export | The March 9–10 redistribution moves about 67 passages from eastbound to westbound on two days with no snowfall and no loading. Eastbound becomes about 2,716; the share outside constraint days 71.6 %, still 72 % as published. The December–February window (1,626 eastbound) is untouched. | None: the analysis was restricted to the eastbound channel for this reason. |
| Monthly bikes a day (Aug 658 … Mar 54, Apr 275, May 472, Jun 747, Jul 691) | daily table | May understated by the three zero days (about 60 a day on the monthly mean). | March to July understated in the westbound direction. |
| No winter day at zero (minimum 2); 60 days with 40 or more | daily table | None. | None, or more days at 40 or more. |
| Comparison with the "8" and "99 %" (camera count of January 29, 2025, against the counter) | both | None: the comparison uses January 2026, before the shift. | None. |
| Telraam against the loop (directional shares) | — | None. | This comparison is the evidence of the question itself. |

In sum: no revision on the supplier's list changes a published winter figure; the annual total was already published as a lower bound and rises by about 2,000 once the May gap is filled; the one figure that moves is the eastbound count in the exposure analysis, by about 2 %, without changing the published percentage. Every identified or suspected error runs the same way: the record understates, and it understates the year more than the winter.

## 6. The nature of the revisions

The supplier's validation is a routine service for every permanent counter it hosts. The platform keeps the original series and the validated series side by side (the dashed "Original data" in the analyst's charts). A release under the Access Act is a copy of what the borough exported on the day of the export; the borough does not revise the series itself, and later exports reflect later validation. Two kinds of revision are involved:

1. **Redistribution between directions.** The daily total is kept; the split is replaced by the site's historical weekday ratio. A redistributed day is a modelled split, not a measurement. It changes no total and affects directional figures only on the days named.
2. **Imputation of gaps.** Hours or days the logger did not record are estimated from correlated counters elsewhere. In the releases these days are visible as zeros or half-days, and the analyses here have treated them as gaps, not as counts.

Totals over windows without gaps are therefore not affected by validation; gaps are visible in the released data and can be excluded; a revision after release can only fill a gap or move passages between directions. What validation does not address is the question of section 1: a sustained change in one channel's sensitivity would, over time, be absorbed into the historical ratio, and the supplier's checks did not flag the shift from March 2. That question turns on the channel mapping, not on further validation.

Two consequences for the documents in these repositories: each figure carries the date of the release it comes from, and each README lists the revisions known at the time of writing. The same caveat applies to every number drawn from the platform by anyone, including the daily figures cited publicly by the borough.

## 7. Open, as of October 21, 2026

Put to the division in reply on October 21: an hourly export of the four bicycle channels and the motor channel from July 26, 2025 to date, with the validated values and the reconstructed periods identified; which loop lies under which lane, and which channels the two columns of the releases correspond to; and whether the analyst's comparison for March to May concerns the pair « côté sud – vers est » / « ZELT Evo OUT_ouest ». The directional split since May 11, 2026 remains unanswered. The author noted that the data had so far been obtained under the Act and left the division to choose between a direct transmission and a formal request. This note will be updated when the answers arrive.
