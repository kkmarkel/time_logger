# Pitfalls Research — Time Logger App

## Common Mistakes

What desktop time tracking apps commonly get wrong:

### 1. Timer Drift
**Warning Signs:** Timer shows different time than system clock after hours
**Prevention:** Use QTimer with system time delta, not accumulated ticks
**Phase:** Phase 1 (timer implementation)

### 2. UI Freezes During Long Sessions
**Warning Signs:** App becomes unresponsive after running for hours
**Prevention:** Use separate timer thread, event-driven updates
**Phase:** Phase 1 (timer implementation)

### 3. Data Lost on Crash
**Warning Signs:** Timer running, app crashes, time lost
**Prevention:** Save to JSON on each stop, not just on exit
**Phase:** Phase 2 (persistence)

### 4. Color Not Saved
**Warning Signs:** Activity loses color after restart
**Prevention:** Persist color with activity in JSON
**Phase:** Phase 2 (persistence)

### 5. Window Gets Covered
**Warning Signs:** Fixed position app gets hidden by other windows
**Prevention:** Use Qt.Tool window flag, raise on hover, or always-on-top option
**Phase:** Phase 1 (basic window)

### 6. Activity Name Not Unique
**Warning Signs:** Multiple entries for "Meeting", "meeting", "Meeting "
**Prevention:** Normalize names (strip, case-insensitive lookup)
**Phase:** Phase 2 (activity management)

## Phase Mapping

- Phase 1: Timer drift, UI freezes, window covering
- Phase 2: Data loss, color not saved, name uniqueness

---

*Pitfalls researched: 2026-04-18*
*Source: pythonguis.com, learnpyqt.com*