# 0006. A featured door

- Status: accepted 5 October 2026, in the October refresh brief; amends ADR 0001 (doors of equal weight, one quiet ledger) and ADR 0002 (a third equal column).
- Context: three equal cards made the strongest work look like the rest, and an equal grid gives a skimming eye no anchor.
- Decision: MAX AI is the featured door. From 48rem it runs full width above Final Docs and Encompass, which sit two-up, and its miniature moves beside its text once the card is wide enough to keep the miniature's titles legible; below 48rem the doors stack in that order, MAX AI's name a step larger. The first plan, a two-row span beside the pair from 64rem, left the featured card about 420 px shorter than the pair at 1440. Also shipped becomes one card in the door family, led by the 13 automations.
- Consequences: source, visual and tab order stay the same; the 500-word and 4,500 px caps at 390 px and the 1.5-phone-screen rule still hold, checked with tools/measure.py, which needed tighter phone spacing in the doors.
