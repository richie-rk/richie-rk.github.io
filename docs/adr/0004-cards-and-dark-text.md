# 0004. Cards, and three steps of dark-mode text

- Status: accepted 2 October 2026, at Richy's request after the Phase 2b checkpoint.
- Context: the home doors (hairline columns, ADR 0001) and the text-only deep dives still read as a wall of text, above all on phones; full-white body text glared and the earlier grey looked dull.
- Decision: content that stands alone becomes a flat card (surface, hairline, 0.5rem radius, no shadow): the doors as tappable cards with one stretched link, the testimonial, Also shipped, and the deep dives' overview, contents, panels, figures and next-deep-dive card. Dark-mode headings and bold keywords are #FFFFFF, body text #DDE7E4 (APCA Lc 90), muted text #AEC3BE; links keep #83E3C6.
- Consequences: the doors keep equal weight but become boxes, replacing the brief's hairline columns; phone pages grow taller, so the deep dives miss the 7,000 px height target; trimmed comments keep the CSS under 50 KB.
