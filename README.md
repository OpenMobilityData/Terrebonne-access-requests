# Terrebonne access requests

Records released under Quebec's *Act respecting Access to documents held by public bodies and the Protection of personal information* (CQLR, c. A-2.1) concerning the protected bike lane on rue de Terrebonne in the borough of Côte-des-Neiges–Notre-Dame-de-Grâce, Montréal.

The lane was built in 2024 along about 2.5 km of Terrebonne (St-Ignatius to Girouard). In October 2026 the borough announced that one direction would be converted to parking each winter. The requests collected here were filed by a resident to obtain the data and documents behind that decision, and the releases are published here exactly as received so that anyone can check what the borough's own files say. Material we derive from them — executive summaries (in English and French), parsed tables, scripts — is kept apart under each request's `derived/` folder so that the record and the reading of it are never confused.

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
- Every derived file names its source: the release number, bundle and pages (a CSV carries this as a first-line comment).
- The PDF of a derived document is committed next to its source so the version cited is the version in the repository.

## Requests

| File no. | Filed | Answered | Subject | Folder |
|---|---|---|---|---|
| 2025-697 | 2025 | 2025 | Hourly bicycle and motor-vehicle counts from the loop counter at Terrebonne / Kensington | *(to be added)* |
| 2026-581 | 2026-09-11 | 2026-10-09 | Origin, procurement, scope, data and deliverables of the 2026 engineering study on Terrebonne (Les Services EXP inc.) | [`2026-581/`](2026-581/) |
| — | 2026-10-08 | pending | Final report of the 2026 study and the slides referred to at the council meeting of 2026-10-06 | *(to be added)* |

## Provenance and use

The documents are reproduced exactly as released by the borough, including its redactions. Names and work addresses of public officials and of the consultant's staff appear as the borough left them. The releases are public records. The READMEs and the contents of the `derived/` folders are published under CC BY 4.0 (code under MIT).

Quotations from these documents in other work should cite the file number and the PDF page of the released bundle, e.g. "2026-581, bundle 01, p. 8".

## Related

- [`Terrebonne-EXP-Report`](https://github.com/OpenMobilityData/Terrebonne-EXP-Report) — the 2023 EXP study, released by the borough on its own initiative before the original project vote.
- [`Terrebonne-working-committee`](https://github.com/OpenMobilityData/Terrebonne-working-committee) — planning documents for the 2024 project.
- [`BikeStat`](https://github.com/OpenMobilityData/BikeStat) — web app for the counter data.

## About the author

The requests were filed, and the derived documents written, by Rick Hoge, a resident of Côte-des-Neiges–Notre-Dame-de-Grâce who cycles on Terrebonne in every season. He works as a data scientist and is a professor in the Faculty of Medicine at McGill University, where his research is in neuroscience and biomedical engineering, including the effects of physical activity on brain health. The work in this repository is personal: it was done as a resident, on his own time, from public records, and represents no position of McGill University or of any other organization; the affiliation is given for identification only. Corrections are welcome through the repository's issue tracker.
