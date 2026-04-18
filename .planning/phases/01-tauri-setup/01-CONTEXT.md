# Phase 1: Tauri Setup - Context

**Gathered:** 2026-04-19
**Status:** Ready for planning

<domain>
## Phase Boundary

Initialize Tauri project with working dev environment. Phase delivers scaffolded project with dev server running and empty window display.

</domain>

<decisions>
## Implementation Decisions

### Frontend Framework
- **D-01:** Svelte — chosen for compile-away minimal runtime, fast performance

### Project Structure
- **D-02:** `/commands` — Rust backend modular organization (Tauri commands)
- **D-03:** `services/` — Frontend layer wrapping all Tauri invoke calls (no direct Tauri API in components)
- **D-04:** `widget/` — Domain layer treating UI like mini game engine
- **D-05:** `src/app/widget/animations/` — Explicit animation layer (idle.ts, click.ts, loop.ts)
- **D-06:** No direct Tauri API calls in frontend components

### Module Organization (detailed)
- **D-07:** `/commands` — Rust backend Tauri commands (modular)
- **D-08:** `frontend/services/` — Tauri invoke wrappers (all calls go through services)
- **D-09:** `frontend/widget/` — Domain layer (treat like mini game engine)
- **D-10:** `frontend/shared/` — Shared types and contracts
- **D-11:** `frontend/app/widget/animations/` — Explicit animations (idle.ts, click.ts, loop.ts)

### Shared Contracts
- **D-12:** WidgetState type = "idle" | "active" | "sleep"

### Anti-Patterns
- **D-13:** No direct Tauri API calls in components — go through services
- **D-14:** Nothing in main.rs — modular command organization

</decisions>

<specifics>
## Specific Ideas

- "Treat widget like a mini game engine" — animation layer explicitly in domain
- "Add animation layer explicitly" — animations/ folder with idle, click, loop files
- Avoid main.rs bloat — modular command organization

</specifics>

<canonical_refs>
## Canonical References

### Tauri
- `docs.tauri.io` — Official Tauri documentation
- No external specs — requirements captured in decisions above

</canonical_refs>

 代码参考>
## Existing Code Insights

### Reusable Assets (from PySide6)
- `data/storage.py` — JSON storage logic (port to Rust commands)
- `main.py` — App initialization pattern

### Established Patterns
- Activity tracking model (name, color, total_seconds)
- JSON persistence in user app data directory

### Integration Points
- Storage commands map to Rust backend
- Frontend services call Tauri invoke

</code_context>

<deferred>
## Deferred Ideas

- Widget-specific visual polish — Phase 2+
- Weekly reports — Phase 3
- Color picker enhancements — Phase 2

</deferred>

---

*Phase: 01-tauri-setup*
*Context gathered: 2026-04-19*