# Measurements

Commit 3ee2637, measured 2026-10-06 by `python tools/measure.py` in headless Chromium 140.0.7339.16.

| Page | Viewport | Scheme | Words in main | Height (px) | Blocks over 6 lines | Muted share | First-screen elements | Horizontal overflow |
| --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |
| index | 390x844 | dark | 290 | 2,922 | 0 of 18 (longest 4) | 0.12 | header, role, claim, proof, buttons, first door name | none |
| index | 390x844 | light | 290 | 2,922 | 0 of 18 (longest 4) | 0.12 | header, role, claim, proof, buttons, first door name | none |
| index | 1440x900 | dark | 304 | 3,013 | 0 of 18 (longest 6) | 0.12 | header, role, claim, proof, buttons, first door name | none |
| index | 1440x900 | light | 304 | 3,013 | 0 of 18 (longest 6) | 0.12 | header, role, claim, proof, buttons, first door name | none |
| max-ai | 390x844 | dark | 1,624 | 12,540 | 0 of 84 (longest 6) | 0.05 | header, name, claim, summary, at-a-glance | none |
| max-ai | 390x844 | light | 1,624 | 12,540 | 0 of 84 (longest 6) | 0.05 | header, name, claim, summary, at-a-glance | none |
| max-ai | 1440x900 | dark | 1,624 | 10,157 | 0 of 84 (longest 5) | 0.05 | header, name, claim, summary, at-a-glance | none |
| max-ai | 1440x900 | light | 1,624 | 10,157 | 0 of 84 (longest 5) | 0.05 | header, name, claim, summary, at-a-glance | none |
| final-docs | 390x844 | dark | 1,494 | 12,220 | 0 of 93 (longest 6) | 0.01 | header, name, claim, summary, at-a-glance | none |
| final-docs | 390x844 | light | 1,494 | 12,220 | 0 of 93 (longest 6) | 0.01 | header, name, claim, summary, at-a-glance | none |
| final-docs | 1440x900 | dark | 1,494 | 9,737 | 0 of 93 (longest 4) | 0.01 | header, name, claim, summary, at-a-glance | none |
| final-docs | 1440x900 | light | 1,494 | 9,737 | 0 of 93 (longest 4) | 0.01 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 390x844 | dark | 822 | 6,490 | 0 of 38 (longest 6) | 0.13 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 390x844 | light | 822 | 6,490 | 0 of 38 (longest 6) | 0.13 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 1440x900 | dark | 822 | 4,946 | 0 of 38 (longest 4) | 0.13 | header, name, claim, summary, at-a-glance | none |
| encompass-automation | 1440x900 | light | 822 | 4,946 | 0 of 38 (longest 4) | 0.13 | header, name, claim, summary, at-a-glance | none |
| cv | 390x844 | dark | 784 | 6,663 | 0 of 109 (longest 6) | 0.06 | header, name, role, contact | none |
| cv | 390x844 | light | 784 | 6,663 | 0 of 109 (longest 6) | 0.06 | header, name, role, contact | none |
| cv | 1440x900 | dark | 784 | 5,262 | 0 of 109 (longest 4) | 0.06 | header, name, role, contact | none |
| cv | 1440x900 | light | 784 | 5,262 | 0 of 109 (longest 4) | 0.06 | header, name, role, contact | none |
| letter | 390x844 | dark | 122 | 2,536 | 0 of 4 (longest 6) | 0.24 | header, heading | none |
| letter | 390x844 | light | 122 | 2,536 | 0 of 4 (longest 6) | 0.24 | header, heading | none |
| letter | 1440x900 | dark | 122 | 3,509 | 0 of 4 (longest 4) | 0.24 | header, heading | none |
| letter | 1440x900 | light | 122 | 3,509 | 0 of 4 (longest 4) | 0.24 | header, heading | none |
| 404 | 390x844 | dark | 34 | 844 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |
| 404 | 390x844 | light | 34 | 844 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |
| 404 | 1440x900 | dark | 34 | 900 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |
| 404 | 1440x900 | light | 34 | 900 | 0 of 5 (longest 2) | 0.30 | header, heading, button | none |

## Gates

Targets from the brief. Words, height, long blocks and the first screen are judged at 390x844; muted share and overflow across all four runs. "Baseline" targets allow 10% either way.

| Page | Words in main | Height at 390 | Blocks over 6 lines | Muted share | First screen at 390 | Horizontal overflow | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| index | pass 290 (max 500) | pass 2,922 px (max 4,500) | pass 0 | pass 0.12 (max 0.20) | pass all in | pass none | pass |
| max-ai | FAIL 1,624 (baseline 1,387 +/- 10%) | FAIL 12,540 px (max 7,000) | pass 0 | pass 0.05 (max 0.20) | pass all in | pass none | FAIL |
| final-docs | FAIL 1,494 (baseline 1,116 +/- 10%) | FAIL 12,220 px (max 7,000) | pass 0 | pass 0.01 (max 0.20) | pass all in | pass none | FAIL |
| encompass-automation | n/a 822 | pass 6,490 px (max 7,000) | pass 0 | pass 0.13 (max 0.20) | pass all in | pass none | pass |
| cv | FAIL 784 (baseline 669 +/- 10%) | FAIL 6,663 px (max 5,500) | pass 0 | n/a 0.06 | pass all in | pass none | FAIL |
| letter | FAIL 122 (baseline 180 +/- 10%) | FAIL 2,536 px (baseline 3,193 +/- 10%) | pass 0 | n/a 0.24 | pass all in | pass none | FAIL |
| 404 | FAIL 34 (baseline 29 +/- 10%) | pass 844 px (baseline 844 +/- 10%) | pass 0 | n/a 0.30 | pass all in | pass none | FAIL |

## Details at 390x844, dark

### index

- Project names: MAX AI at 787 px, Final Docs at 1,038 px, Encompass loan automation at 1,252 px
- Share of body text not in --text (muted plus links): 0.36

### max-ai

- Project names: Final Docs at 12,029 px
- TOC height: 312 px
- Share of body text not in --text (muted plus links): 0.12

### final-docs

- Project names: Encompass loan automation at 11,650 px
- TOC height: 348 px
- Share of body text not in --text (muted plus links): 0.10

### encompass-automation

- Project names: MAX AI at 5,952 px
- Share of body text not in --text (muted plus links): 0.19

### cv

- Share of body text not in --text (muted plus links): 0.17

### letter

- Share of body text not in --text (muted plus links): 0.27

### 404

- Share of body text not in --text (muted plus links): 1.00
