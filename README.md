# Terrebonne access requests

Records released under Quebec's *Act respecting Access to documents held by public bodies and the Protection of personal information* (CQLR, c. A-2.1) concerning the protected bike lane on rue de Terrebonne in the borough of Côte-des-Neiges–Notre-Dame-de-Grâce, Montréal.

The lane was built in 2024 along about 2.5 km of Terrebonne (St-Ignatius to Girouard). In its first year, July 26, 2025 to July 25, 2026, the borough's loop counter at Kensington recorded 135,276 bicycle passages and 501,817 motor vehicles on the street (summed from the daily totals the borough released under 2026-581, bundle 01, pp. 74–81, as parsed in [`2026-581/derived/`](2026-581/derived/)). In October 2026 the borough announced that one direction would be converted to parking each winter. The requests collected here were filed by a resident to obtain the data and documents behind that proposal, and the releases are published here exactly as received so that anyone can check what the borough's own files, and the City's, say. Material we derive from them — executive summaries (in English and French), parsed tables, scripts — is kept apart under each request's `derived/` folder so that the record and the reading of it are never confused.

## How the repository is organized

```
<file no.>/            one folder per access request
    README.md          context, page map, what was withheld and on what grounds
    raw/               documents exactly as received; never edited
        act_extracts/  statutory extracts and notice of recourse supplied with the response
    derived/           anything made from the raw release: summaries (_en/_fr), parsed data, scripts
```

Rules:

- Nothing in `raw/` is ever modified; a correction to a derived file is a new version with a note.
- Every derived file names its source: the release number, bundle and pages. A CSV carries no comment lines, so that it parses in any tool; its source is given in the folder README's table.
- The PDF of a derived document is committed next to its source so the version cited is the version in the repository.

## Requests

| File no. | Filed | Answered | Subject | Folder |
|---|---|---|---|---|
| 2025-081 | 2025-02-24 | 2025-03-06 | The petitions against the lane as tabled with the borough on February 2, 2024 (87-page scan, personal information blacked out); derived counts by source and borough | [`2025-081/`](2025-081/) |
| 2025-12847 | 2025-11-26/27 (borough file 2025-695, transferred to the City 2025-11-27 under s. 46) | 2026-01-06 | *City of Montréal.* The "audit" by the SUM referred to by the borough mayor at the council meeting of November 26, 2025: an internal note of November 10, 2025 ("Réseau cyclable – Audits correctifs et préventifs") and six annexes | [`2025-12847/`](2025-12847/) |
| 2025-697 | 2025-11-27 | 2025-12-19 | All traffic count data held by the borough for rue de Terrebonne from June 1, 2024, and the make, model and location of the counting equipment (loop counter at Kensington; Eco-Counter ZELT EVO) | [`2025-697/`](2025-697/) |
| 2026-300 | 2026-05-06 | 2026-06-04 | Hourly bicycle (by direction) and motor-vehicle counts from the Kensington loop counter, July 26, 2025 – May 11, 2026; derived analysis of winter use against snow-loading days | [`2026-300/`](2026-300/) |
| 2026-581 | 2026-09-11 | 2026-10-09 | Origin, procurement, scope, data and deliverables of the 2026 engineering study on Terrebonne (Les Services EXP inc.) | [`2026-581/`](2026-581/) |
| 2026-634 | 2026-10-08 | due 2026-11-07 | Final report of the 2026 study and the material referred to at the council meeting of 2026-10-06 (acknowledged 2026-10-13; 20-day limit extended by 10 days under s. 47) | *(to be added)* |

## Provenance and use

The documents are reproduced exactly as released by the borough, including its redactions. Names and work addresses of public officials and of the consultant's staff appear as the borough left them. The releases are public records. The READMEs and the contents of the `derived/` folders are published under CC BY 4.0 (code under MIT).

Quotations from these documents in other work should cite the file number and the PDF page of the released bundle, e.g. "2026-581, bundle 01, p. 8".

### Edit history

Everything in this repository was written in the open. The complete edit history of every file, including the derived documents, is public through the [commit log](https://github.com/OpenMobilityData/Terrebonne-access-requests/commits/main) and the diffs: each change to a summary can be traced to the commit that made it, with the reason given in the commit message, and earlier versions can be retrieved by their version tag (the `YYYY-MM-DD-hh-mm-ss` stamp in each document's footer and PDF metadata). Corrections made along the way, such as the re-sourcing of the "99%" figure on October 10, are in that record rather than silently overwritten. The derived documents were drafted and revised with the help of an AI assistant (Anthropic's Claude), which is named as co-author on the commits where it was used; the author checked every quotation and page reference against the released documents and is responsible for the content.

## Related

- [`Terrebonne-open-sources`](https://github.com/OpenMobilityData/Terrebonne-open-sources) — public documents on the lane obtained from open sources rather than under the Act: the 2023 EXP mobility study, the 2020–2021 working committee's documents, the 2024 council approvals, and others, with their provenance; also the transcript and fact check of the councillor's CBC *Daybreak* interview of October 9, 2026.
- [`BikeStat`](https://github.com/OpenMobilityData/BikeStat) — web app for the counter data.

## About the author

The requests were filed, and the derived documents written, by Rick Hoge, a resident of Côte-des-Neiges–Notre-Dame-de-Grâce who cycles on Terrebonne in every season. He works as a data scientist and is a professor in the Faculty of Medicine at McGill University, where his research is in neuroscience and biomedical engineering, including the effects of physical activity on brain health. The work in this repository is personal: it was done as a resident, on his own time, from public records, and represents no position of McGill University or of any other organization; the affiliation is given for identification only. Corrections are welcome through the repository's issue tracker.
