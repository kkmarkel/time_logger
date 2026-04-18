# Time Logger

## What This Is

A Windows desktop application that sits as a fixed icon on the desktop screen, allowing users to track time spent on activities. Users can enter or select activity names, assign colors, start/stop a timer, and view cumulative time with visual bar representations. Data persists between restarts.

## Core Value

Enable personal productivity by helping users understand where their time goes through simple, visual time tracking.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Fixed desktop position — app stays where placed on Windows desktop
- [ ] Activity name input with color selection
- [ ] Activity selection from previously logged activities
- [ ] Start/stop timer button with live display (HH:MM)
- [ ] Cumulative time tracking per activity
- [ ] Visual bar representation of time amounts
- [ ] Clear all recordings
- [ ] Clear last recording
- [ ] JSON file persistence between restarts
- [ ] Manual app start

### Out of Scope

- [Auto-start on Windows boot] — deferred to future version
- [Export to CSV/Excel] — not requested initially
- [Edit/delete past recordings] — not in v1
- [Daily totals view] — weekly reports only for v1

## Context

- Platform: Windows desktop
- Tech stack: PySide6 (Python Qt bindings)
- Storage: JSON file (user preference)
- Primary use: Personal productivity/time awareness

## Constraints

- **Platform**: Windows desktop only — fixed position on screen
- **Persistence**: JSON file in user's app data directory
- **Stack**: PySide6 — user preference over Electron/Tauri

## Key Decisions

| Decision | Rationale | Outcome |
|----------|---------|---------|
| PySide6 stack | User preference for desktop Qt apps | — Pending |
| JSON storage | Simple, human-readable, easy to backup | — Pending |
| Weekly reports | User requested over daily totals | — Pending |

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

*Last updated: 2026-04-18 after initialization*