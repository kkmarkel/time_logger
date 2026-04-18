# Phase 1 Plan 02 Summary: Gap Closure Fixes

**Phase:** 01-core-timer
**Plan:** 02
**Type:** gap_closure
**Wave:** 1

## Key Files Modified

| File | Description |
|------|-------------|
| ui/main_window.py | Main window with all 5 bug fixes |

## Implementation Summary

Fixed 5 issues identified during UAT testing:

### Fix 1: Frameless window translucent background (cosmetic)
- Added `setAttribute(Qt.WA_TranslucentBackground)` in `_init_ui()`
- Changed QWidget background from `#2c3e50` to `transparent`
- Changed title_bar background to `transparent`
- **Result:** No black frame visible around frameless window

### Fix 2: Color picker dialog flags (major)
- Added `dialog.setWindowFlags(Qt.Dialog | Qt.WindowStaysOnTopHint)` in `_pick_color()`
- **Result:** Color picker stays on top and maintains focus

### Fix 3: Window drag calculation (major)
- Changed `frameGeometry().topLeft()` to `self.pos()` in mouse event handlers
- Changed condition from `==` to `&` for button check
- **Result:** Window can be dragged by clicking title bar or content area

### Fix 4: Context menu implementation (blocker)
- Added `contextMenuEvent(self, event)` override
- Uses `menu.popup(event.globalPos())` instead of deprecated `exec()`
- **Result:** Right-click shows context menu without errors

### Fix 5: Auto-save visual feedback (minor)
- Added visual feedback: timer label shows "SAVED ✓" or "CLOSED" before closing
- Uses `QTimer.singleShot(400, self._execute_close)` for delayed close
- **Result:** User sees that time was saved before window closes

## Requirements Achieved

- [x] No visible frame/border around the frameless window
- [x] Color picker has solid background and maintains focus
- [x] Window is draggable via title bar or content area
- [x] Right-click shows context menu without errors
- [x] Time auto-saves on close with user feedback

## Duration

- Start: 2026-04-19T00:20:00Z
- End: 2026-04-19T00:25:00Z
- Total: ~5 min

---

*Phase: 01-core-timer*
*Plan completed: 2026-04-19*