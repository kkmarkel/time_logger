# Phase 1: Core Timer - Context

**Gathered:** 2026-04-18
**Status:** Ready for planning

<domain>
## Phase Boundary

Working start/stop timer with activity name input/selection and color picker. Single toggle button controls timer. Timer displays elapsed time in HH:MM:SS format and updates every second. Fixed position window on desktop with compact icon-like form factor.

**Requirements:** TIMER-01, TIMER-02, TIMER-03, TIMER-04, TIMER-05, TIMER-06, TIMER-07, WIND-01, WIND-02

</domain>

<decisions>
## Implementation Decisions

### Activity Input
- **D-01:** Smart ComboBox — dropdown shows recent activities, typing filters the list, combines text input with history access

### Color Picker
- **D-02:** Both Presets + Custom — row of preset color swatches user can click, plus option to open full color picker for custom colors

### Timer Display
- **D-03:** HH:MM:SS format — displays hours, minutes, and seconds (e.g., 01:23:45)

### Toggle Button
- **D-04:** Icons Only — play triangle for Start, stop square for Stop (no text labels)

### Window Appearance
- **D-05:** Frameless window — no title bar border, custom close/min buttons, behaves more like a desktop widget

### Activity-Dropdown Interaction
- **D-06:** Auto-fill on selection — selecting a previous activity fills both the activity name AND its saved color

### Window Starting Position
- **D-07:** Remember position — app remembers last window position and restores it on next launch

### Timer on App Close
- **D-08:** Auto-save on close — if timer is running when app closes, automatically stop and save elapsed time to that activity

### Minimum Window Size
- **D-09:** Compact minimum — enforce minimum window size to maintain desktop icon form factor

### Always on Top
- **D-10:** Toggle option — user can enable/disable always-on-top via right-click menu

### Drag to Reposition
- **D-11:** Full window drag — clicking and dragging anywhere in the window moves it (no dedicated title bar needed in frameless design)

### Empty Activity Handling
- **D-12:** Block empty start — prevent starting timer when activity name is empty, highlight input as required

</decisions>

<canonical_refs>
## Canonical References

### Requirements
- `.planning/REQUIREMENTS.md` — All v1 requirements including TIMER-01 through TIMER-07, WIND-01, WIND-02
- `.planning/ROADMAP.md` — Phase 1 goal and success criteria

### Stack
- `.planning/research/STACK.md` — PySide6 recommended for implementation

### Project
- `.planning/PROJECT.md` — Platform: Windows desktop, Stack: PySide6, Storage: JSON file

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- No existing code in the project — this is a greenfield application

### Established Patterns
- PySide6 Qt framework — standard Qt widget patterns apply
- Qt ComboBox supports editable mode for smart input
- Qt custom window flags for frameless behavior

### Integration Points
- New PySide6 application to be created
- JSON file storage at app initialization

</code_context>

<specifics>
## Specific Ideas

- "Icons only" for toggle — play triangle (▶) for start, stop square (■) for stop
- Frameless window with custom close/min buttons in corner
- Right-click context menu for always-on-top toggle
- Window can be dragged by clicking anywhere in the frameless window

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within Phase 1 scope

</deferred>

---

*Phase: 01-core-timer*
*Context gathered: 2026-04-18*