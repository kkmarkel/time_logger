---
status: complete
phase: 01-core-timer
source: 01-SUMMARY.md
started: 2026-04-18T23:45:00Z
updated: 2026-04-19T00:15:00Z
---

## Current Test

[testing complete]
awaiting: user response

## Tests

### 1. Launch application
expected: App launches as a compact frameless window with custom title bar (minimize, close buttons). Title bar shows "Time Logger".
result: issue
reported: "It still has a black frame around the window - is that intended?"
severity: cosmetic

## Gaps

- truth: "Frameless window with no visible frame/border"
  status: failed
  reason: "User reported: It still has a black frame around the window"
  severity: cosmetic
  test: 1

- truth: "Color picker dialog with solid background that stays in focus"
  status: failed
  reason: "User reported: The window that appears for color selection has transparent background. That is very inconvenient. Also clicking on it somewhere else other than the colors or buttons - causes the window to go out of focus (the app window disappears)."
  severity: major
  test: 4

- truth: "Window can be dragged by clicking and dragging on title bar or content area"
  status: failed
  reason: "User reported: Window doesn't drag at all - not on the title nor on the content area"
  severity: major
  test: 10

- truth: "Menu to toggle always-on-top via button (three dots) instead of right-click"
  status: failed
  reason: "User reported: Context menu doesn't show up, error in terminal. Suggests using a menu button (three dots) instead of right-click."
  severity: blocker
  test: 11

- truth: "Auto-save on close is visible/verified"
  status: failed
  reason: "User reported: It closed fine, but I do not know if it autosaved the time"
  severity: minor
  test: 15

### 2. Enter activity name
expected: Type activity name in the input field. Name displays and can be changed.
result: pass

### 3. Select previous activity
expected: Click the dropdown arrow to see list of previous activities. Select one to load it.
result: pass

### 4. Pick color
expected: Click the color button to open preset colors (8 colors). Click a color to select it. Color button updates to show selected color.
result: issue
reported: "The window that appears for color selection has transparent background. That is very inconvenient. Also clicking on it somewhere else other than the colors or buttons - causes the window to go out of focus (the app window disappears). Other than that actual color selection and color presets work."
severity: major

### 5. Custom color
expected: Click color button, select a custom color from the Qt color dialog. Custom color is saved with the activity.
result: issue
reported: "Same issue as test 4 - transparent background and focus issues"
severity: major

### 6. Start timer
expected: Click the play button (▶). Timer starts counting up, button changes to stop icon (■). Display shows elapsed time in HH:MM:SS format.
result: pass

### 7. Timer updates
expected: While running, timer display updates every second showing elapsed time.
result: pass

### 8. Stop timer
expected: Click stop button (■). Timer stops, elapsed time is saved to the activity. Button returns to play (▶). Display resets to 00:00:00.
result: pass

### 9. Empty activity blocked
expected: Attempt to start timer without entering activity name. Button does nothing, input shows red border warning.
result: pass

### 10. Drag window
expected: Click and drag anywhere on the title bar or content area to move the window.
result: issue
reported: "Window doesn't drag at all - not on the title nor on the content area"
severity: major

### 11. Always-on-top toggle
expected: Right-click anywhere to show context menu. Select "Enable Always on Top" or "Disable Always on Top". Window stays above other windows when enabled.
result: issue
reported: "Context menu doesn't show up, and it also prints out an error in the terminal. User suggests using a menu button (three dots) instead of right-click."
severity: blocker

### 12. Window position persists
expected: Move the window to a specific position. Close the app. Reopen app. Window appears in the same position.
result: skipped
reason: Cannot test - drag doesn't work (test 10 failed)

### 13. Activity history persists
expected: Start timer with an activity. Stop it. Close and reopen app. Activity appears in the dropdown list.
result: pass

### 14. Minimize window
expected: Click the minimize button (─) in title bar. Window minimizes to taskbar.
result: pass

### 15. Close window
expected: Click the close button (✕) in title bar. If timer is running, auto-saves elapsed time. Window closes.
result: issue
reported: "It closed fine, but I do not know if it autosaved the time"
severity: minor

## Summary

total: 15
passed: 8
issues: 6
pending: 0
skipped: 1
skipped: 0
blocked: 0

## Gaps

[none yet]