# Measurements

Commit 8d23dd6, measured 2026-10-05 by `python tools/measure.py` in headless Chromium 140.0.7339.16.

| Page | Viewport | Scheme | Words in main | Height (px) | Blocks over 6 lines | Muted share | First-screen elements | Horizontal overflow |
| --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |
| index | 390x844 | dark | 246 | 2,912 | 0 of 16 (longest 4) | 0.12 | header, role, claim, proof, buttons, email, first door name | none |
| index | 390x844 | light | 246 | 2,912 | 0 of 16 (longest 4) | 0.12 | header, role, claim, proof, buttons, email, first door name | none |
| index | 1440x900 | dark | 408 | 3,252 | 0 of 27 (longest 4) | 0.18 | header, role, claim, proof, buttons, email, first door name | none |
| index | 1440x900 | light | 408 | 3,252 | 0 of 27 (longest 4) | 0.18 | header, role, claim, proof, buttons, email, first door name | none |
| max-ai | 390x844 | dark | 1,336 | 10,786 | 0 of 74 (longest 6) | 0.06 | header, name, claim, summary, at-a-glance | none |
| max-ai | 390x844 | light | 1,336 | 10,786 | 0 of 74 (longest 6) | 0.06 | header, name, claim, summary, at-a-glance | none |
| max-ai | 1440x900 | dark | 1,336 | 8,790 | 0 of 74 (longest 5) | 0.06 | header, name, claim, summary, at-a-glance | none |
| max-ai | 1440x900 | light | 1,336 | 8,790 | 0 of 74 (longest 5) | 0.06 | header, name, claim, summary, at-a-glance | none |
| final-docs | 390x844 | dark | 1,112 | 10,075 | 0 of 77 (longest 6) | 0.01 | header, name, claim, summary, at-a-glance | none |
| final-docs | 390x844 | light | 1,112 | 10,075 | 0 of 77 (longest 6) | 0.01 | header, name, claim, summary, at-a-glance | none |
| final-docs | 1440x900 | dark | 1,112 | 8,630 | 0 of 77 (longest 4) | 0.01 | header, name, claim, summary, at-a-glance | none |
| final-docs | 1440x900 | light | 1,112 | 8,630 | 0 of 77 (longest 4) | 0.01 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 390x844 | dark | 668 | 5,693 | 0 of 34 (longest 6) | 0.16 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 390x844 | light | 668 | 5,693 | 0 of 34 (longest 6) | 0.16 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 1440x900 | dark | 668 | 4,308 | 0 of 34 (longest 4) | 0.16 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 1440x900 | light | 668 | 4,308 | 0 of 34 (longest 4) | 0.16 | header, name, claim, summary, at-a-glance | none |
| cv | 390x844 | dark | 767 | 6,660 | 0 of 109 (longest 6) | 0.06 | header, name, role, contact | none |
| cv | 390x844 | light | 767 | 6,660 | 0 of 109 (longest 6) | 0.06 | header, name, role, contact | none |
| cv | 1440x900 | dark | 767 | 5,233 | 0 of 109 (longest 4) | 0.06 | header, name, role, contact | none |
| cv | 1440x900 | light | 767 | 5,233 | 0 of 109 (longest 4) | 0.06 | header, name, role, contact | none |
| letter | 390x844 | dark | 163 | 3,137 | 0 of 4 (longest 6) | 0.23 | header, heading | none |
| letter | 390x844 | light | 163 | 3,137 | 0 of 4 (longest 6) | 0.23 | header, heading | none |
| letter | 1440x900 | dark | 177 | 4,051 | 0 of 4 (longest 4) | 0.23 | header, heading | none |
| letter | 1440x900 | light | 177 | 4,051 | 0 of 4 (longest 4) | 0.23 | header, heading | none |
| 404 | 390x844 | dark | 34 | 844 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |
| 404 | 390x844 | light | 34 | 844 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |
| 404 | 1440x900 | dark | 34 | 900 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |
| 404 | 1440x900 | light | 34 | 900 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |

## Gates

Targets from the brief. Words, height, long blocks and the first screen are judged at 390x844; muted share and overflow across all four runs. "Baseline" targets allow 10% either way.

| Page | Words in main | Height at 390 | Blocks over 6 lines | Muted share | First screen at 390 | Horizontal overflow | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| index | pass 246 (max 500) | pass 2,912 px (max 4,500) | pass 0 | pass 0.18 (max 0.20) | pass all in | pass none | pass |
| max-ai | pass 1,336 (baseline 1,387 +/- 10%) | FAIL 10,786 px (max 7,000) | pass 0 | pass 0.06 (max 0.20) | pass all in | pass none | FAIL |
| final-docs | pass 1,112 (baseline 1,116 +/- 10%) | FAIL 10,075 px (max 7,000) | pass 0 | pass 0.01 (max 0.20) | pass all in | pass none | FAIL |
| encompass-automation | n/a 668 | pass 5,693 px (max 7,000) | pass 0 | pass 0.16 (max 0.20) | pass all in | pass none | pass |
| cv | FAIL 767 (baseline 669 +/- 10%) | FAIL 6,660 px (max 5,500) | pass 0 | n/a 0.06 | pass all in | pass none | FAIL |
| letter | pass 163 (baseline 180 +/- 10%) | pass 3,137 px (baseline 3,193 +/- 10%) | pass 0 | n/a 0.23 | pass all in | pass none | pass |
| 404 | FAIL 34 (baseline 29 +/- 10%) | pass 844 px (baseline 844 +/- 10%) | pass 0 | n/a 0.30 | pass all in | pass none | FAIL |

## Details at 390x844, dark

### index

- Project names: MAX AI at 787 px, Final Docs at 1,019 px, Encompass loan automation at 1,250 px
- Share of body text not in --text (muted plus links): 0.40

### max-ai

- Project names: Final Docs at 10,275 px
- TOC height: 312 px
- Share of body text not in --text (muted plus links): 0.13

### final-docs

- Project names: Encompass loan automation at 9,505 px
- TOC height: 312 px
- Share of body text not in --text (muted plus links): 0.13

### encompass-automation

- Project names: MAX AI at 5,155 px
- Share of body text not in --text (muted plus links): 0.23

### cv

- Share of body text not in --text (muted plus links): 0.19

### letter

- Share of body text not in --text (muted plus links): 0.26

### 404

- Share of body text not in --text (muted plus links): 1.00
