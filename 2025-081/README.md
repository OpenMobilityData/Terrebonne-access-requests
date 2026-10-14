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
| [`raw/Doc_requis_2025-081.pdf`](raw/Doc_requis_2025-081.pdf) | 87 | The petitions as received by the borough, scanned. Pages 1–2: the organizers' cover letters of February 2, 2024 (French and English), delivered by hand, asking the clerk to place the petitions on the agenda of the council meeting of February 5, 2024. Then the handwritten sheets headed "Respectez les résidents de la rue de Terrebonne! / Terrebonne residents matter!" (columns: name, signature, address, postal code; the first three blacked out, the postal code left visible), a printout of the online petition, and the two short petitions noted in the response |
| `raw/act_extracts/` | — | Sections 53, 54, 56, 57 and 59 of the Act and the notice of recourse, as supplied |

The scan is reproduced exactly as released, including the borough's redactions. A recompressed copy of the same scan was published in 2025 in a separate repository (`OpenMobilityData/Petition`, since retired), together with a map of signature counts by six-character postal code; the map will be redone here from the checked codes, with its data source documented.

### What the cover letters say

The letters (pp. 1–2) are addressed to the borough mayor and councillors "aux noms de résidents de cet arrondissement en désaccord avec la mesure" and state that the signatories "protestons contre les mesures prises par l'arrondissement relativement à la reconfiguration de la rue Terrebonne et à l'installation de pistes cyclables ou d'autres aménagements tels que des placettes sans réelle consultation préalable des citoyens, des personnes morales et des institutions concernées". They give the count as "796 citoyens que nous avons rencontrés personnellement" plus the online petition, stated as 306 signatories in the French letter and 342 in the English one, for totals of 1,102 and 1,138 respectively, "and anticipate that we will resubmit prior to the meeting."

## Derived

| File | Content |
|---|---|
| [`derived/petition_signatures_by_postal_code.csv`](derived/petition_signatures_by_postal_code.csv) | Entries per six-character postal code (288 codes), with the 2025 borough district of the code's centroid and its distance to the lane |
| [`derived/petition_signatures_by_district.csv`](derived/petition_signatures_by_district.csv) | Entries by district of the borough (2025 boundaries), other borough, outside the City, not geocoded |
| [`derived/petition_signatures_by_distance.csv`](derived/petition_signatures_by_distance.csv) | Entries by distance from the lane (100 m, 250 m, 500 m, 1 km, 2 km bands) |
| [`derived/petition_map.png`](derived/petition_map.png) | Map: one point per postal code, sized by entries, with the borough's 2025 district boundaries and the lane |
| [`derived/petition_entries_by_source_and_borough.csv`](derived/petition_entries_by_source_and_borough.csv) | Earlier, coarser table: entries by source sheet and by borough from the forward sortation area |

**Method.** The postal codes were read from the released scan in March 2025 (text recognition, checked by hand): 890 rows, 888 with a six-character code, 288 distinct codes. Each code was geocoded to its centroid, placed in a borough electoral district with the City's 2025 polygons, and measured to the nearest point of the lane on the City's géobase. The third-party files are not redistributed; they are named with links in the header of each CSV so that anyone can obtain them (the City's district polygons and géobase are CC-BY 4.0; the geocoding table is Service Objects' free postal-code database, March 2024 edition). The script is `scripts/petition_map.py` in the private repository, a port of the 2025 MATLAB script.

**Results.** 869 of the 888 entries (271 codes) were geocoded; 19 entries carry codes that do not exist or were misread. By district of the borough: Loyola 524 entries (59%), Notre-Dame-de-Grâce 288 (32%), Snowdon 15, Côte-des-Neiges 2, Darlington 1; other boroughs 12; outside the City of Montréal 27 (mostly the adjacent municipalities of Côte-Saint-Luc, Hampstead and Montréal-Ouest). By distance from the lane: 398 entries (46% of those geocoded) are at postal codes within 100 m of it, 57% within 250 m, 79% within 500 m, 92% within 1 km.

**Note on the 2025 reading.** The analysis written in March 2025 classified codes by forward sortation area and treated H4A and H4B as the NDG district; H4B straddles Loyola and NDG, so that method put about 80% of the entries in NDG district and 13% in Loyola. With the district polygons the split is the reverse: the signatures come mostly from the western, Loyola section of the lane. Both districts' councillors therefore have signatories among their residents.

## Timeline

| Date | Event |
|---|---|
| 2024-01 → 02 | Online petition signed (the change.org export in the scan carries a "Signed On" date per entry, from January 12, 2024) |
| 2024-02-02 | Cover letters and petitions delivered by hand to the borough clerk |
| 2024-02-05 | Borough council meeting for which the petitions were tabled |
| 2025-02-24 | Request filed |
| 2025-03-06 | Response |
