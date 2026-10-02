# 0003. The wow animates the diagrams, not a data-shaped demo

- Status: accepted 30 September 2026, in the portfolio design refactor brief; implementation deferred to its own brief (Phase 4).
- Context: the first idea was a streaming MAX AI answer and a YAML-dispatch toggle for Final Docs, but even invented content in a fake answer or config row can read as real client data.
- Decision: animate the architecture diagrams the deep dives already contain: MAX AI's query and ingestion paths traced in turn, and Final Docs' hardcoded path against the config-driven one. It plays once on scroll into view with a Replay button, is static under reduced motion, and the page still works with JS off.
- Consequences: no data-shaped demo ships, the diagrams stay abstract so nothing can leak, and the work waits for Richy's own brief with its own phases and gates.
