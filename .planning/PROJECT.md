# Time Logger

## What This Is

A Windows desktop application that sits as a fixed icon on the desktop screen, allowing users to track time spent on activities. Users can enter or select activity names, assign colors, start/stop a timer, and view cumulative time with visual bar representations. Data persists between restarts.

## Core Value

Enable personal productivity by helping users understand where their time goes through simple, visual time tracking.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Tauri-based desktop app (rebuild from scratch)
- [ ] Animated main window UI
- [ ] Timer with activity tracking (core logic ported)
- [ ] Cumulative time display with visual bars
- [ ] JSON file persistence between restarts

### Out of Scope

- [Auto-start on Windows boot] — deferred to future version
- [Export to CSV/Excel] — not requested initially
- [Edit/delete past recordings] — not in v1
- [Daily totals view] — weekly reports only for v1

## Context

- Platform: Windows desktop
- Tech stack: Tauri (Rust backend + frontend)
- Storage: JSON file (user preference)
- Primary use: Personal productivity/time awareness
- Status: Pivot from PySide6 to Tauri - rebuilding UI
- Preserved: Storage logic (JSON file handling)

## Constraints

- **Platform**: Windows desktop only — fixed position on screen
- **Persistence**: JSON file in user's app data directory
- **Stack**: Tauri (Rust + WebView) — NEW DIRECTION as of 2026-04-19

## Key Decisions

| Decision | Rationale | Outcome |
|----------|---------|---------|
| Tauri stack | Switch from PySide6 for modern web tech | — Pending |
| JSON storage | Simple, human-readable, easy to backup | — Pending |
| Weekly reports | User requested over daily totals | — Pending |
| Animated main window | NEW: Main window with transition animations | — Pending |
| UI redesign | UI approach flawed - new direction | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

### After each phase transition (via `/gsd-transition`)

1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

### After each milestone (via `/gsd-complete-milestone`)

1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---

*Last updated: 2026-04-19 after pivot to Tauri*