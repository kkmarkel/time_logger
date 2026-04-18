# Codebase Concerns

**Analysis Date:** 2026-04-19

## Tech Debt

**Window Frame Rendering:**
- Issue: Black frame appears around the frameless window due to title bar having `border-radius: 8px 8px 0 0` while the main window lacks proper border masking
- Files: `ui/main_window.py`
- Impact: Cosmetic issue - visible black corners when window has rounded top edges
- Fix approach: Add a masking region or adjust the window container to clip the corners properly

**Color Picker Dialog:**
- Issue: Color picker loses focus and has transparent background - the QColorDialog uses `Qt.Dialog` flag but lacks proper parent reference and solid background styling
- Files: `ui/main_window.py` (lines 294-308)
- Impact: User cannot select colors reliably
- Fix approach: Pass `self` as parent to QColorDialog and ensure dialog has opaque background

**Drag Functionality:**
- Issue: Window drag is implemented but triggers from anywhere on the widget instead of just the title bar area, causing unintended drag behavior
- Files: `ui/main_window.py` (lines 421-442)
- Impact: Users may accidentally drag window when interacting with content
- Fix approach: Check if mouse position is within title bar bounds before starting drag

**Context Menu:**
- Issue: Uses `menu.popup()` which is non-blocking and causes the menu to close immediately instead of `menu.exec()` which blocks until user selects an option
- Files: `ui/main_window.py` (line 455)
- Impact: Right-click context menu is unusable
- Fix approach: Replace `popup()` with `exec()`

**Activity Selection Validation:**
- Issue: When activity name is empty and user clicks start, the combobox style changes to red border but timer does not start - no feedback given to user about why
- Files: `ui/main_window.py` (lines 312-321)
- Impact: Poor UX - user must figure out what's wrong
- Fix approach: Add a label or tooltip explaining the validation requirement

**Duplicate Activity Creation:**
- Issue: Adding new activity creates duplicate entries in dropdown even when activity already exists in storage (line 356 adds to combo, then line 357-360 adds to storage again if new)
- Files: `ui/main_window.py` (lines 354-360)
- Impact: Potential duplicate activities in data storage
- Fix approach: Check storage existence before adding new activity

## Known Bugs

**Context Menu Not Functional:**
- Symptoms: Right-click anywhere shows nothing or immediate menu disappearance
- Files: `ui/main_window.py` (lines 444-455)
- Trigger: Right-click anywhere on window
- Workaround: Use the menu button (...) in title bar for settings

**Window Position Not Restored on First Run:**
- Symptoms: On initial launch, window may not center properly if no saved position exists
- Files: `ui/main_window.py` (lines 270-279), `data/storage.py` (lines 74-79)
- Trigger: First application launch with no saved settings
- Workaround: Application centers on screen by default

**Timer State Lost on Crash:**
- Symptoms: If app crashes while timer is running, elapsed time is lost
- Files: `ui/main_window.py`, `data/storage.py`
- Trigger: Application crash or force close while timer running
- Workaround: None - time is not persisted during active session

**Color Not Saved for Existing Activities:**
- Symptoms: Changing color for an existing activity does not persist the new color
- Files: `data/storage.py` (method `add_activity` only creates, no update method)
- Trigger: Select existing activity, change color, start/stop timer
- Workaround: None - color change is not persisted

## Security Considerations

**Data File Permissions:**
- Risk: Data files stored in user's home directory (~/.timelogger/) with default file permissions
- Files: `data/storage.py` (line 8)
- Current mitigation: None - files inherit system default permissions
- Recommendations: Use file permissions that restrict access to owner only (mode 0o600)

**No Input Sanitization:**
- Risk: Activity names are stored and displayed without sanitization - potential for injection of malicious content in display
- Files: `ui/main_window.py`, `data/storage.py`
- Current mitigation: None
- Recommendations: Sanitize activity names before storage and display

**Sensitive Data in Plain Text:**
- Risk: All data (activity names, time tracking) stored in plain JSON files
- Files: `data/storage.py`
- Current mitigation: None
- Recommendations: Consider encryption for sensitive time tracking data

## Performance Bottlenecks

**File I/O on Every Operation:**
- Problem: Every timer tick saves data (line 60 in storage.py), every activity add saves, every time add saves
- Files: `data/storage.py` (lines 52, 60, 65)
- Cause: No batching or debouncing - synchronous writes on every state change
- Improvement path: Implement debounced auto-save with a background timer that saves every 30-60 seconds instead of on every change

**Linear Search for Activities:**
- Problem: Activity lookups use `next()` with list comprehension (lines 46, 58, 70 in storage.py) - O(n) complexity
- Files: `data/storage.py`
- Cause: Activities stored in a list, not a dictionary
- Improvement path: Convert activities list to dictionary keyed by activity name for O(1) lookups

**Stylesheet Recreation on Color Change:**
- Problem: ColorButton recreates entire stylesheet string every time color changes
- Files: `ui/main_window.py` (lines 35-46)
- Cause: No stylesheet caching or partial update mechanism
- Improvement path: Use Qt stylesheet property binding or update only background-color property

## Fragile Areas

**JSON Loading Without Validation:**
- Files: `data/storage.py` (lines 15-22, 24-31)
- Why fragile: If JSON file is corrupted or has unexpected structure, application returns default empty data without warning
- Safe modification: Add schema validation and logging for corrupted data
- Test coverage: No test coverage for corrupted data scenarios

**Event Filter Installation Without Cleanup:**
- Files: `ui/main_window.py` (line 424)
- Why fragile: Event filter is installed on every mouse press but only removed on mouse release - if exception occurs, filter stays installed
- Safe modification: Use try/finally or context manager pattern for event filter lifecycle
- Test coverage: No coverage for exception scenarios during drag

**Timer Memory Management:**
- Files: `ui/main_window.py` (lines 333-335)
- Why fragile: QTimer is created but not explicitly stopped or cleaned up if app crashes - potential resource leak
- Safe modification: Use parent ownership or explicit cleanup in close handler
- Test coverage: No test coverage for crash scenarios

## Scaling Limits

**Data Storage:**
- Current capacity: JSON file can handle thousands of activities
- Limit: File size grows unbounded - no pagination or archiving
- Scaling path: Implement database (SQLite) for larger datasets, add pagination for UI

**Memory:**
- Current capacity: Small - all data loaded into memory
- Limit: If user has >10,000 activities with history, memory usage becomes noticeable
- Scaling path: Implement lazy loading and data virtualization

## Dependencies at Risk

**PySide6:**
- Risk: Single dependency - if PySide6 has breaking changes or is deprecated, entire application breaks
- Impact: No alternative Qt binding fallback
- Migration plan: Could migrate to PyQt5 or PyQt6 with moderate refactoring - core UI patterns would remain similar

## Missing Critical Features

**Activity Deletion:**
- Problem: No way to delete activities once created
- Blocks: User cannot clean up old/irrelevant activities

**Activity Color Update:**
- Problem: Changing color for existing activity does not persist
- Blocks: Users cannot update activity colors after creation

**Time Entry History:**
- Problem: Only total_seconds accumulated - no individual time entries with timestamps
- Blocks: Cannot analyze time patterns, no daily/weekly breakdown

**Data Export:**
- Problem: No way to export tracked time data
- Blocks: Cannot use data in external tools or generate reports

**Test Coverage:**
- Problem: No unit tests or integration tests exist
- Blocks: Cannot refactor safely, regressions go undetected

---

*Concerns audit: 2026-04-19*