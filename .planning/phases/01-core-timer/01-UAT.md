---
status: resolved
phase: 01-core-timer
source: 01-SUMMARY.md, 01-02-SUMMARY.md
started: 2026-04-18T23:45:00Z
updated: 2026-04-19T00:25:00Z
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

All 5 issues have been fixed in plan 01-02:

1. **No visible frame/border** (cosmetic, test 1) — Fixed with WA_TranslucentBackground + transparent styles
2. **Color picker focus** (major, test 4) — Fixed with Qt.Dialog | Qt.WindowStaysOnTopHint
3. **Window drag** (major, test 10) — Fixed drag calculation using self.pos()
4. **Context menu** (blocker, test 11) — Fixed with contextMenuEvent override
5. **Auto-save feedback** (minor, test 15) — Fixed with "SAVED ✓" visual feedback
  status: resolved
  reason: "It still has a black frame around the window - is that intended?"
  severity: cosmetic
  test: 1
  root_cause: "ui/main_window.py:65 - FramelessWindowHint set but missing WA_TranslucentBackground attribute and shadow removal"
  artifacts:
    - path: "ui/main_window.py"
      line: 65
      issue: "setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)"
    - path: "ui/main_window.py"
      line: "169-173"
      issue: "QWidget background-color style"
  missing:
    - "Add self.setAttribute(Qt.WA_TranslucentBackground)"
    - "Remove window shadow via QPalette or window shadow override"

- truth: "Color picker should have solid background and maintain focus when clicking outside"
  status: resolved
  reason: "The window that appears for color selection has transparent background. That is very inconvenient. Also clicking on it somewhere else other than the colors or buttons - causes the window to go out of focus (the app window disappears)."
  severity: major
  test: 4
  root_cause: "ui/main_window.py:291-294 - QColorDialog created with self as parent but lacks proper dialog flags (Qt.Dialog) and doesn't set Qt.WindowStaysOnTopHint"
  artifacts:
    - path: "ui/main_window.py"
      line: 291
      issue: "dialog = QColorDialog(self)"  
    - path: "ui/main_window.py"
      line: 294
      issue: "dialog.setOption(QColorDialog.DontUseNativeDialog)"
  missing:
    - "Add dialog window flags: dialog.setWindowFlags(Qt.Dialog | Qt.WindowStaysOnTopHint)"
    - "Or implement custom in-app color picker"

- truth: "Window should be draggable via title bar or content area"
  status: resolved
  reason: "Window doesn't drag at all - not on the title nor on the content area"
  severity: major
  test: 10
  root_cause: "ui/main_window.py:397-410 - Mouse event handlers exist but dragging calculation is flawed. Line 399: frameGeometry().topLeft() returns local widget position"
  artifacts:
    - path: "ui/main_window.py"
      line: "397-400"
      issue: "mousePressEvent handler"
    - path: "ui/main_window.py"
      line: "404-407"
      issue: "mouseMoveEvent handler"
  missing:
    - "Fix drag calculation: Use self.pos() instead of frameGeometry().topLeft()"
    - "Ensure entire widget area captures mouse events for dragging"

- truth: "Right-click should show context menu without errors"
  status: resolved
  reason: "Context menu doesn't show up, error in terminal. Suggests using a menu button (three dots) instead of right-click."
  severity: blocker
  test: 11
  root_cause: "ui/main_window.py:412-423 - _show_context_menu uses menu.exec() with deprecated signature, missing contextMenuEvent override"
  artifacts:
    - path: "ui/main_window.py"
      line: "401-402"
      issue: "mousePressEvent calls _show_context_menu"
    - path: "ui/main_window.py"
      line: "412-423"
      issue: "_show_context_menu method"
  missing:
    - "Override contextMenuEvent(self, event) method"
    - "Use menu.exec(event.globalPos()) or menu.popup(position)"

- truth: "Time should auto-save on close with user feedback (visual confirmation)"
  status: resolved
  reason: "It closed fine, but I do not know if it autosaved the time"
  severity: minor
  test: 15
  root_cause: "ui/main_window.py:388-395 - _close_app correctly saves time but provides no visual feedback"
  artifacts:
    - path: "ui/main_window.py"
      line: "388-395"
      issue: "_close_app method"
  missing:
    - "Add user feedback: show brief notification/status change indicating save occurred"

- truth: "Window position should persist between sessions"
  status: skipped
  reason: "Test 12 - Window position persists (test 10 failed)"
  severity: skipped
  test: 12
  root_cause: "Code exists at ui/main_window.py:266-275 (restore) but skipped due to drag issue in test 10"

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