# Measurements

Commit c10c193, measured 2026-10-02 by `python tools/measure.py` in headless Chromium 140.0.7339.16.

| Page | Viewport | Scheme | Words in main | Height (px) | Blocks over 6 lines | Muted share | First-screen elements | Horizontal overflow |
| --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |
| index | 390x844 | dark | 973 | 8,147 | 4 of 53 (longest 8) | 0.86 | header, role, claim, proof, buttons, email missing, first door name below, at 891 px | none |
| index | 390x844 | light | 973 | 8,147 | 4 of 53 (longest 8) | 0.86 | header, role, claim, proof, buttons, email missing, first door name below, at 891 px | none |
| index | 1440x900 | dark | 1,000 | 6,037 | 0 of 53 (longest 5) | 0.86 | header, role, claim, proof, buttons, email missing, first door name | none |
| index | 1440x900 | light | 1,000 | 6,037 | 0 of 53 (longest 5) | 0.86 | header, role, claim, proof, buttons, email missing, first door name | none |
| max-ai | 390x844 | dark | 1,387 | 8,721 | 12 of 29 (longest 17) | 0.11 | header, name, claim, summary missing, at-a-glance cut off at 594 px | figure 1 +516px |
| max-ai | 390x844 | light | 1,387 | 8,721 | 12 of 29 (longest 17) | 0.11 | header, name, claim, summary missing, at-a-glance cut off at 594 px | figure 1 +516px |
| max-ai | 1440x900 | dark | 1,387 | 6,407 | 5 of 29 (longest 9) | 0.11 | header, name, claim, summary missing, at-a-glance | none |
| max-ai | 1440x900 | light | 1,387 | 6,407 | 5 of 29 (longest 9) | 0.11 | header, name, claim, summary missing, at-a-glance | none |
| final-docs | 390x844 | dark | 1,116 | 8,169 | 13 of 30 (longest 18) | 0.01 | header, name, claim, summary missing, at-a-glance cut off at 616 px | figure 1 +516px |
| final-docs | 390x844 | light | 1,116 | 8,169 | 13 of 30 (longest 18) | 0.01 | header, name, claim, summary missing, at-a-glance cut off at 616 px | figure 1 +516px |
| final-docs | 1440x900 | dark | 1,116 | 6,247 | 3 of 30 (longest 9) | 0.01 | header, name, claim, summary missing, at-a-glance | none |
| final-docs | 1440x900 | light | 1,116 | 6,247 | 3 of 30 (longest 9) | 0.01 | header, name, claim, summary missing, at-a-glance | none |
| cv | 390x844 | dark | 669 | 5,711 | 7 of 35 (longest 10) | 0.21 | header, name, role, contact | none |
| cv | 390x844 | light | 669 | 5,711 | 7 of 35 (longest 10) | 0.21 | header, name, role, contact | none |
| cv | 1440x900 | dark | 669 | 4,031 | 0 of 35 (longest 5) | 0.21 | header, name, role, contact | none |
| cv | 1440x900 | light | 669 | 4,031 | 0 of 35 (longest 5) | 0.21 | header, name, role, contact | none |
| letter | 390x844 | dark | 180 | 3,193 | 0 of 4 (longest 6) | 0.23 | header, heading | none |
| letter | 390x844 | light | 180 | 3,193 | 0 of 4 (longest 6) | 0.23 | header, heading | none |
| letter | 1440x900 | dark | 180 | 3,965 | 0 of 4 (longest 3) | 0.23 | header, heading | none |
| letter | 1440x900 | light | 180 | 3,965 | 0 of 4 (longest 3) | 0.23 | header, heading | none |
| 404 | 390x844 | dark | 29 | 844 | 0 of 4 (longest 2) | 0.38 | header, heading, button | none |
| 404 | 390x844 | light | 29 | 844 | 0 of 4 (longest 2) | 0.38 | header, heading, button | none |
| 404 | 1440x900 | dark | 29 | 900 | 0 of 4 (longest 2) | 0.38 | header, heading, button | none |
| 404 | 1440x900 | light | 29 | 900 | 0 of 4 (longest 2) | 0.38 | header, heading, button | none |

## Gates

Targets from the brief. Words, height, long blocks and the first screen are judged at 390x844; muted share and overflow across all four runs. "Baseline" targets allow 10% either way.

| Page | Words in main | Height at 390 | Blocks over 6 lines | Muted share | First screen at 390 | Horizontal overflow | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| index | FAIL 973 (max 500) | FAIL 8,147 px (max 4,500) | FAIL 4 | FAIL 0.86 (max 0.20) | FAIL not in: email, first door name | pass none | FAIL |
| max-ai | pass 1,387 (baseline 1,387 +/- 10%) | FAIL 8,721 px (max 7,000) | FAIL 12 | pass 0.11 (max 0.20) | FAIL not in: at-a-glance, summary | FAIL figure 1 +516px | FAIL |
| final-docs | pass 1,116 (baseline 1,116 +/- 10%) | FAIL 8,169 px (max 7,000) | FAIL 13 | pass 0.01 (max 0.20) | FAIL not in: at-a-glance, summary | FAIL figure 1 +516px | FAIL |
| cv | pass 669 (baseline 669 +/- 10%) | FAIL 5,711 px (max 5,500) | FAIL 7 | n/a 0.21 | pass all in | pass none | FAIL |
| letter | pass 180 (baseline 180 +/- 10%) | pass 3,193 px (baseline 3,193 +/- 10%) | pass 0 | n/a 0.23 | pass all in | pass none | pass |
| 404 | pass 29 (baseline 29 +/- 10%) | pass 844 px (baseline 844 +/- 10%) | pass 0 | n/a 0.38 | pass all in | pass none | pass |

## Details at 390x844, dark

### index

- Project names: MAX AI at 891 px, Final Docs at 1,864 px
- Share of body text not in --text (muted plus links): 0.87
- 8 lines: Final Docs governs how PRMI assembles and delivers post-closing packages to its investor b
- 7 lines: Approach: treat an investor as data, not code. I rebuilt the monolith into config-driven d
- 7 lines: Result: 4 new investors integrated in a single month, work that previously consumed a full
- 8 lines: REST API for TechSpan Engineering’s remote water-quality monitoring platform, which is mul

### max-ai

- TOC height: 409 px
- Share of body text not in --text (muted plus links): 0.16
- 10 lines: PRMI’s primary knowledge retrieval tool. Mortgage staff ask natural-language questions aga
- 10 lines: A language model’s knowledge is frozen in its weights: a mortgage guideline revised last T
- 15 lines: Fine-tuning solves none of this economically. Re-indexing one changed PDF takes seconds; a
- 13 lines: The durable trio. A single HTTP function cannot index a corpus: the work outlives any HTTP
- 8 lines: The per-file pipeline: download and detect encoding, dispatch by file type to the right lo
- 9 lines: The corpus is not just text: every PDF page is rasterized to a PNG so the UI can show the 
- 10 lines: Retrieval is hybrid, in three layers. BM25 over a lemmatizing English analyzer catches exa
- 17 lines: HyDE closes the gap between short questions and long documents. Queries and documents sit 
- 12 lines: Grounding is a data-formatting decision as much as a prompting one. Each retrieved chunk i
- 16 lines: Streaming is NDJSON: one complete JSON object per line over ordinary chunked HTTP. A singl
- 12 lines: Ingestion is throughput-bound: CPU-heavy, tolerant of hours of latency, and it must surviv
- 9 lines: Provenance, stated plainly: the platform grew out of Microsoft’s open-source RAG reference

### final-docs

- TOC height: 327 px
- Share of body text not in --text (muted plus links): 0.06
- 12 lines: After a mortgage loan closes, PRMI must deliver post-closing document packages to the inve
- 10 lines: Every investor reports final-document exceptions differently: different source files and r
- 7 lines: The original implementation absorbed those differences as branching logic inside a monolit
- 8 lines: Each investor is described by one YAML file: source directory and report name, a column_ma
- 7 lines: The processor reverses the configured mapping, renames the incoming DataFrame into the sta
- 9 lines: Not every investor can be processed by reading a file. Some need custom data generation: o
- 8 lines: The alternative is the familiar failure mode: if investor A, elif investor B, and a centra
- 8 lines: Loan identity. Some investors report only their own loan number. A resolver queries Encomp
- 10 lines: Document vocabulary. Free-text comments are inspected for known keywords to infer a standa
- 12 lines: The consolidated investor data is compared with First American custodian data, joined on t
- 7 lines: The output is an Excel workbook with Missing_Defect, Mismatch and the consolidated investo
- 18 lines: The system separates four responsibilities. Batch orchestration decides which investors to
- 11 lines: Onboarding a new investor fell from 2-4 weeks of bespoke coding to a configuration exercis

### cv

- Share of body text not in --text (muted plus links): 0.28
- 7 lines: 5+ years of Python development, plus a year of industrial automation. Shipped production G
- 7 lines: Retrieval: hybrid vector + semantic ranking on Azure AI Search with HyDE query expansion; 
- 9 lines: Ingestion: Durable Functions pipeline, idempotent via audit-table checkpointing with per-f
- 10 lines: Final Docs refactor. Rebuilt a monolithic automation into config-driven dynamic dispatch: 
- 10 lines: Encompass REST API SDK. Internal Python package consumed by all 13 automations: OAuth2 tok
- 9 lines: 13 production RPA automations (Power Automate + Python) across ECOA adverse action, TRID, 
- 8 lines: HydroQ API. Designed the FastAPI interface for the database CRUD operations of a multi-ten

### letter

- Share of body text not in --text (muted plus links): 0.26

### 404

- Share of body text not in --text (muted plus links): 1.00
