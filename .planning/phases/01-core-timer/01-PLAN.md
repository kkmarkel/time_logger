# Phase 1: Core Timer - Plan

**Created:** 2026-04-18
**Status:** Ready for execution

## Phase Goal

Working start/stop timer with activity selection and color picker in a fixed-position frameless window.

## Requirements Covered

- TIMER-01: Activity name input
- TIMER-02: Activity dropdown (previous)
- TIMER-03: Color picker
- TIMER-04: Start button
- TIMER-05: Stop button (toggle)
- TIMER-06: HH:MM display
- TIMER-07: Second-by-second update
- WIND-01: Fixed position
- WIND-02: Desktop icon behavior

## Tasks

### Foundation Setup

**T-01: Project Initialization**
- Create Python project with PySide6 dependency
- Set up main application class
- Verify window launches on Windows
- Add to `.gitignore`: `__pycache__/`, `*.pyc`, `venv/`

**T-02: Window Configuration**
- Create frameless window with custom close/min buttons
- Set minimum window size for compact form
- Implement full-window drag functionality
- Add right-click context menu for always-on-top toggle

### Activity Input

**T-03: Smart ComboBox**
- Implement editable ComboBox with activity history
- Add filtering: typing filters the dropdown list
- Store unique activity names (case-insensitive dedupe)
- Load previous activities from JSON storage

**T-04: Color Picker**
- Create preset color row (8-10 common colors)
- Add button to open full Qt color dialog for custom colors
- Store color selection with activity name
- Visual indicator of selected color

### Timer Functionality

**T-05: Timer Display**
- Create HH:MM:SS formatted display label
- Implement QTimer for 1-second updates
- Track start time and calculate elapsed

**T-06: Toggle Button**
- Implement single button with icon states
- Play triangle (▶) for stopped/running
- Update button icon based on timer state
- Block empty activity name (T-12)

**T-07: Timer Logic**
- Start: record start timestamp, begin 1-second updates
- Stop: calculate total elapsed, save to activity in memory
- Update: refresh display every second showing elapsed time

### Persistence & Behavior

**T-08: JSON Data Storage**
- Create JSON file in user's app data directory
- Load existing activities on startup
- Save activities after each timer stop

**T-09: Window Position**
- Save window position to JSON on move/close
- Restore position on app launch
- Handle case when saved position is off-screen

**T-10: App Close Behavior**
- Detect timer running on window close
- Auto-save elapsed time before exit
- Clean shutdown of timer and app

## Implementation Notes

### Dependencies
- PySide6 (Qt for Python)
- Python 3.9+

### File Structure
```
timelogger/
├── main.py          # Entry point, app initialization
├── ui/
│   ├── __init__.py
│   └── main_window.py  # Main window class
├── data/
│   ├── __init__.py
│   └── storage.py    # JSON persistence
└── requirements.txt
```

## Acceptance Criteria

1. User can enter activity name and see it displayed
2. User can select from previous activities dropdown
3. User can pick color for activity
4. Single button starts timer, shows running state
5. Same button stops timer when clicked again
6. Timer displays elapsed time in HH:MM:SS format
7. Timer updates every second while active
8. App stays at fixed position on desktop
9. App has compact desktop icon form factor
10. Window is frameless with custom controls
11. User can toggle always-on-top
12. Position persists across restarts
13. Running timer auto-saves on close
14. Cannot start timer without activity name

---

*Phase: 01-core-timer*
*Plan created: 2026-04-18*