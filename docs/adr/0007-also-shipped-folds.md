# 0007. Also shipped folds

- Status: accepted 6 October 2026, at Richy's request after reviewing the October refresh; amends ADR 0006 (Also shipped as one open card).
- Context: open at every width, Also shipped ran about 900 px on a phone and pushed "Ping me" well down the page, though it is the least important block on home.
- Decision: Also shipped is one card in the door family holding a native details element, closed by default at every width, so it works without JS. Closed, it shows a summary line with a chevron and two highlights (the 13 automations and HydroQ); open, the full rows appear and the highlights hide, since the rows say the same in full. The summary is muted and takes the link colour on hover and focus, with the site focus ring and no underline; the chevron turns only without reduced motion.
- Consequences: home falls from 3,797 to 2,922 px at 390 px and from 3,574 to 3,013 px at 1440 px; the folded rows leave the word count and the muted share; the highlights must stay true to the rows they summarise, so the summary carries no count and the HydroQ line keeps the recorded 2-4 hours.
