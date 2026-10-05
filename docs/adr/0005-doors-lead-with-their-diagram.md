# 0005. Doors lead with their diagram

- Status: accepted 5 October 2026, in the October refresh brief; amends ADR 0004 for the home doors.
- Context: the doors still read as text, the strongest material (the architecture diagrams) sat a click away, and each card repeated its link as an underlined "Read the X deep dive" above a hairline.
- Decision: each door leads with a static, decorative miniature of its own deep-dive diagram, cropped to the core path and drawn in theme tokens; its titles drop out where they would render under about 11px. The link moves to the card title and stays stretched over the card; a quiet "Deep dive" cue replaces the underlined action and its hairline, and on phones it shares the title's first line. Hover and focus change the edge, the cue and the miniature's strokes, never position or shadow.
- Consequences: diagrams return to home as decoration only (aria-hidden, hidden below 48rem), so the phone budget in ADR 0001 holds; home carries a few kilobytes of inline SVG; the hover lift is removed site-wide.
