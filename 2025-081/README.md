# Access request 2025-081 — Petitions submitted to the borough against the Terrebonne bike lane

**Public body:** Arrondissement de Côte-des-Neiges–Notre-Dame-de-Grâce, Division du greffe
**Filed:** February 24, 2025
**Answered:** March 6, 2025, by the secrétaire d'arrondissement (documents sent by WeTransfer link)
**Released:** one 87-page scan of the petitions as tabled with the borough, with names, signatures and addresses blacked out; the notice of recourse and the sections of the Act relied on

## What was asked

"Access to one or more petitions submitted to the borough in opposition to the Terrebonne Bike Path" (the borough's wording of the request in its response).

## What was released

| File | Pages | Content |
|---|---|---|
| [`raw/response_2025-03-06_redacted.pdf`](raw/response_2025-03-06_redacted.pdf) | 2 | The borough's response letter (requester's address redacted). It notes that "the last petition, on page 84 in French and 87 in English, only contains 33 names. The same names are repeated on the English petition. There is no address on either the French or English petition," and that "all information of a personal nature was omitted" under sections 53, 54, 56, 57 and 59 of the Act |
| [`raw/Doc_requis_2025-081.pdf`](raw/Doc_requis_2025-081.pdf) | 87 | The petitions as received by the borough, scanned. Pages 1–2: the organizers' cover letters of February 2, 2024 (French and English, marked « par courriel / main à main »), asking the clerk to place the petitions on the agenda of the council meeting of February 5, 2024 (the French letter counts 306 online signatures and 1,102 in all, the English 342 and 1,138). Page 67: a supplementary letter of Monday, February 5, 2024 (e-mailed to the clerk at 12:20 that day, « by courrier with signature upon receipt »), adding 141 handwritten and 15 online signatures « for a total of 937 residents » and 321 online, « in total … 1,258 », with two further files. Pages 3 and 33: the petition text itself, headed « Pétition pour le vivre-ensemble dans le cadre de la configuration de rues, notamment celui de la rue de Terrebonne », with the « Objet » and « Intérêt pour la collectivité » headings of annexe B of by-law 05-056 (droit d'initiative); the minutes of February 5, 2024 record the whole as correspondence (« Deux pétitions ainsi que divers courriels reçus de citoyens »), not as a projet de pétition. Then the handwritten sheets headed "Respectez les résidents de la rue de Terrebonne! / Terrebonne residents matter!" (columns: name, signature, address, postal code; the first three blacked out, the postal code left visible), a printout of the online petition, and the two short petitions noted in the response |
| `raw/act_extracts/` | — | Sections 53, 54, 56, 57 and 59 of the Act and the notice of recourse, as supplied |

The scan is reproduced exactly as released, including the borough's redactions. A recompressed copy of the same scan was published in 2025 in a separate repository (`OpenMobilityData/Petition`, since retired), together with a map of signature counts by six-character postal code; the map will be redone here from the checked codes, with its data source documented.

### What the cover letters say

The letters (pp. 1–2) are addressed to the borough mayor and councillors "aux noms de résidents de cet arrondissement en désaccord avec la mesure" and state that the signatories "protestons contre les mesures prises par l'arrondissement relativement à la reconfiguration de la rue Terrebonne et à l'installation de pistes cyclables ou d'autres aménagements tels que des placettes sans réelle consultation préalable des citoyens, des personnes morales et des institutions concernées". They give the count as "796 citoyens que nous avons rencontrés personnellement" plus the online petition, stated as 306 signatories in the French letter and 342 in the English one, for totals of 1,102 and 1,138 respectively, "and anticipate that we will resubmit prior to the meeting."

## Derived

| File | Content |
|---|---|
| [`derived/petition_signatures_by_postal_code.csv`](derived/petition_signatures_by_postal_code.csv) | Entries per six-character postal code (338 codes, both sources), with the 2025 borough district of the code's centroid and its distance to the lane |
| [`derived/petition_signatures_by_district.csv`](derived/petition_signatures_by_district.csv) | Entries by district of the borough (2025 boundaries), other borough, outside the City, not geocoded |
| [`derived/petition_signatures_by_distance.csv`](derived/petition_signatures_by_distance.csv) | Entries by distance from the lane (100 m, 250 m, 500 m, 1 km, 2 km bands) |
| [`derived/petition_map.png`](derived/petition_map.png) | Map: every postal-code area in the borough, coloured by its number of signatures (grey where none) and labelled with the count, with the 2025 district boundaries and the lane. Boundaries from DMTI Spatial's CanMap Postal Code Suite v2024.3 (commercial; bought by the author; credited, not redistributed) |
| [`derived/petition_filter_levels.csv`](derived/petition_filter_levels.csv) | Counts by filter level and source (see *Counts, step by step* below) |
| [`derived/petition_entries_by_source_and_borough.csv`](derived/petition_entries_by_source_and_borough.csv) | Earlier, coarser table: entries by source sheet and by borough from the forward sortation area (H4A/H4B, H4V/H4X, H3W/H3X, H3S/H3T/H3V classed as CDN–NDG; "ambiguous" = an area straddling CDN–NDG and Ville-Marie). Entries are rows read, not signatures |

**Method.** The postal codes were read from the released scan in March 2025. The handwritten sheets were stamped line by line in Acrobat (893 counter stamps) and read by hand into a table of 890 rows in stamp order; the change.org printout was read by text recognition into 304 rows (the printout reproduces the postal code as each signer typed it, often the three-character prefix alone). Since October 22, 2026 the map and the tables use both sources under one rule: every entry whose postal code is a well-formed six-character code is kept (881 handwritten, 106 online, 987 in all, 338 distinct codes); prefix-only, ill-formed and blank entries are counted and left out. Until then the map showed the handwritten sheets alone (888 entries, 869 geocoded). Each code was geocoded to its centroid, placed in a borough electoral district with the City's 2025 polygons, and measured to the nearest point of the lane on the City's géobase. The third-party files are not redistributed; they are named with links in the header of each CSV so that anyone can obtain them (the City's district polygons and géobase are CC-BY 4.0; the geocoding table is Service Objects' free postal-code database, March 2024 edition; the postal-code boundaries on the map are DMTI Spatial's CanMap Postal Code Suite v2024.3, a commercial product used under the author's licence). In the map's count, 272 of the borough's 2,298 postal-code areas have at least one signature. The script is `scripts/petition_map.py` in the private repository, a port of the 2025 MATLAB script.

**Results.** 975 of the 987 entries (328 codes) were geocoded; 12 entries carry codes that do not exist in the postal-code table (misread or invented). By district of the borough: Loyola 553 entries (56%), Notre-Dame-de-Grâce 331 (34%), Snowdon 17, Darlington 3, Côte-des-Neiges 2, in all 906 (93% of those geocoded); other boroughs 28; outside the City of Montréal 41 (mostly the adjacent municipalities of Côte-Saint-Luc, Hampstead and Montréal-Ouest). By distance from the lane: 425 entries (44% of those geocoded) are at postal codes within 100 m of it, 55% within 250 m, 76% within 500 m, 89% within 1 km. For the handwritten sheets alone, the figures that stood until October 2026: 869 geocoded, 830 in the borough (Loyola 524, NDG 288), 79% within 500 m.

**Note on the 2025 reading.** The analysis written in March 2025 classified codes by forward sortation area and treated H4A and H4B as the NDG district; H4B straddles Loyola and NDG, so that method put about 80% of the entries in NDG district and 13% in Loyola. With the district polygons the split is the reverse: the signatures come mostly from the western, Loyola section of the lane. Both districts' councillors therefore have signatories among their residents.

## Counts, step by step

The organizers' cover letter (p. 2) gives 1,138 signatures: « petitions signed by 796 citizens whom we met personally » and « the PDF of those 342 who have signed the petition online ». What the released scan supports, by filter level (`derived/petition_filter_levels.csv`; the corridor is the band between Monkland and Somerled, about 270 m either side of the lane, over its 2.4 km, by postal-code centroid):

| Level | Handwritten sheets | Change.org printout | Both |
|---|---:|---:|---:|
| 1. Lines on the sheets (counter stamps of March 2025) | 893 | 310 | 1,203 |
| 1b. Lines read into a table | 890 | 304 | 1,194 |
| 2. Any postal-code entry | 890 | 301 | 1,191 |
| 3. Well-formed prefix (A1A), with or without the rest | 887 | 300 | 1,187 |
| 4. Well-formed full code (A1A 1A1) | 881 | 106 | 987 |
| 5. Full code inside Côte-des-Neiges–Notre-Dame-de-Grâce | 830 | 76 | 906 |
| 6. Full code in the Terrebonne corridor | 555 | 44 | 599 |

Among the well-formed full codes: Canada outside Québec 3 (all online); Québec outside the City of Montréal 38 (27 + 11); Montréal outside the borough 28 (12 + 16); codes absent from the postal-code table 12 (all handwritten); no US ZIP pattern. Ill-formed entries: 4 (for instance H4B 244, H4V 2JS: one-character slips). The handwritten master drops from 893 stamped lines to 869 geocoded in four steps: 3 lines with nothing readable, 2 prefix-only entries, 7 ill-formed codes, 12 codes absent from the table.

Why the online rows were left off the map until October 2026: the change.org printout gives the postal code as typed by the signer, unvalidated; 192 of its 304 entries are a prefix alone and cannot be placed at six-character precision. The 106 that can be placed are now included under the same rule as the handwritten entries.

## Timeline

| Date | Event |
|---|---|
| 2024-01-12 → 02-04 | Online petition signed (the change.org printout carries a "Signed On" date per entry: 54 on January 12, 168 in the first four days, then a trickle to February 4; [`derived/online_signatures_by_day.csv`](derived/online_signatures_by_day.csv), 275 of 304 dates read by OCR) |
| 2024-02-02 | Cover letters and petitions sent to the borough clerk (« par courriel / main à main »), asking for a place on the February 5 agenda |
| 2024-02-05 | Supplementary letter e-mailed to the clerk at 12:20: +141 handwritten, +15 online, « 1,258 » in all (p. 67) |
| 2024-02-05 | Borough council meeting for which the petitions were tabled |
| 2025-02-24 | Request filed |
| 2025-03-06 | Response |

---

*Use of AI: this README and the derived files beside it were prepared with an AI assistant under the author's direction and review, and checked against the documents; see the repository's [Use of AI statement](../README.md#use-of-ai).*
