---
status: partial
phase: 01-core-timer
source: 01-SUMMARY.md, 01-02-SUMMARY.md
started: 2026-04-18T23:45:00Z
updated: 2026-04-19T16:25:00Z
---

## Current Test

number: 10
name: Drag window
expected: |
  Click and drag anywhere on the title bar or content area. Window moves smoothly with the mouse. No focus loss.
awaiting: user response

## Tests

### 1. Launch application
expected: App launches as a compact frameless window with stylized retrowave gradient title bar (purple/pink/cyan gradient effect), not transparent. Title bar shows "Time Logger".
result: pass

## Gaps

- truth: "Stylized retrowave title bar instead of transparent"
  status: pending
  reason: "window is fully transparent - wants retrowave style title bar"
  severity: minor
  test: 1
  root_cause: "title_bar uses transparent background-color"
  missing: "Add retrowave gradient/gradient-style to title bar"

- truth: "Color picker has solid background and maintains focus"
  status: pending
  reason: "Color picker still has transparent background and loses focus when clicking transparent areas"
  severity: major
  test: 4
  root_cause: "QColorDialog still has transparent parent widget causing focus loss"
  missing: "Set dialog parent to None or use different approach for solid background"

- truth: "Window draggable via title bar or content area"
  status: pending_re_test
  reason: "User reported: no, it does not drag"
  severity: major
  test: 10
  root_cause: "Mouse events intercepted by child widgets; grabMouse() needed"
  missing: []

- truth: "Always-on-top toggle works after enabling"
  status: pending_re_test
  reason: "User reported: It does not stay on top with enabled"
  severity: major
  test: 11
  root_cause: "close() destroys window; use hide()/show() instead"
  missing: []
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
expected: Click color button. Color picker opens with solid background (not transparent). Click outside the color buttons/area - picker maintains focus, window doesn't lose focus.
result: pass

### 5. Custom color
expected: Click color button, select a custom color from the Qt color dialog. Custom color is saved with the activity.
result: issue
reported: "Same issue as test 4 - transparent background and loses focus"
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
expected: Click and drag anywhere on the title bar or content area. Window moves smoothly with the mouse. No focus loss.
result: issue
reported: "no, it does not drag"
severity: major

### 11. Always-on-top toggle
expected: Right-click anywhere to show context menu. Select "Enable Always on Top" or "Disable Always on Top". Window stays above other windows when enabled.
result: issue
reported: "It does not stay on top with enabled"
severity: major

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
result: pass

## Summary

total: 15
passed: 9
issues: 1
pending: 0
skipped: 1
skipped: 0
blocked: 0

## Gaps

- truth: "Window draggable via title bar or content area"
  status: failed
  reason: "User reported: no, it does not drag"
  severity: major
  test: 10
  root_cause: "Mouse events intercepted by child widgets; multiple fixes attempted (grabMouse, event override, eventFilter) - all failed"
  artifacts:
    - path: "ui/main_window.py"
      issue: "mousePressEvent, mouseMoveEvent, event(), eventFilter all fail to capture mouse events from child widgets"
  missing: []
  debug_session: ""