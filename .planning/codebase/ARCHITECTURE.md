# Architecture

**Analysis Date:** 2026-04-19

## Pattern Overview

**Overall:** Simple MVC-like Desktop Application (PySide6)

**Key Characteristics:**
- Single-window application with three-layer separation: UI, Data Storage, Entry Point
- Tight coupling between Storage and UI via direct object reference injection
- Event-driven UI using Qt signals and slots
- Manual window state persistence to local JSON files

## Layers

**Entry Point:**
- Purpose: Application bootstrap and initialization
- Location: `main.py`
- Contains: Main function that creates QApplication, Storage instance, and MainWindow
- Depends on: PySide6.QtWidgets, ui.main_window, data.storage
- Used by: Python interpreter (when running `python main.py`)

**UI Layer:**
- Purpose: GUI rendering, user interaction, timer logic
- Location: `ui/main_window.py`
- Contains: MainWindow class (QWidget), ColorButton custom widget
- Depends on: PySide6.QtWidgets, PySide6.QtCore, PySide6.QtGui
- Depends on: Storage instance (injected via constructor)
- Used by: main.py

**Data Layer:**
- Purpose: Persistent data storage and retrieval
- Location: `data/storage.py`
- Contains: Storage class managing activities and settings
- Depends on: Python standard library (json, os, pathlib)
- Used by: ui/main_window.py

## Data Flow

**Application Startup:**

1. `main.py` creates QApplication with "Time Logger" app name
2. `main.py` instantiates Storage (loads data.json and settings.json)
3. `main.py` creates MainWindow with Storage reference
4. MainWindow calls `_init_ui()` to build UI
5. MainWindow calls `_load_previous_activities()` from storage
6. MainWindow calls `_restore_window_state()` from storage
7. Window displays centered or at saved position

**Timer Operation:**

1. User selects/inputs activity name in QComboBox
2. User selects color in ColorButton via QColorDialog
3. User clicks ▶ (toggle button)
4. If activity name is empty, validation error (red border)
5. If valid, QTimer starts with 1000ms interval
6. Timer label updates every second via `_update_timer()`
7. Toggle button changes to ■ (stop icon, red style)
8. User clicks ■ to stop timer
9. Elapsed seconds added to storage via `storage.add_time()`
10. Timer resets to 00:00:00

**Application Close:**

1. User clicks ✕ (close button)
2. If timer running and elapsed > 0, time is saved
3. Window position saved via `storage.set_window_position()`
4. Window closes

**Data Persistence:**

1. Activities stored in `~/.timelogger/data.json`
2. Settings stored in `~/.timelogger/settings.json`
3. Both JSON files created on first run via `Path.home() / ".timelogger"`

## Key Abstractions

**Storage Class:**
- Purpose: Abstract data persistence layer
- Location: `data/storage.py`
- Methods:
  - `get_activities()` - Returns list of activity dicts
  - `add_activity(name, color)` - Creates new activity or returns existing
  - `add_time(name, seconds)` - Accumulates time for activity
  - `get_activity_color(name)` - Retrieves color for activity
  - `get_window_position()` / `set_window_position(x, y)` - Window state
  - `get_always_on_top()` / `set_always_on_top(value)` - Always-on-top flag
- Pattern: Singleton-like (one instance shared across UI)

**MainWindow Class:**
- Purpose: Main application window and timer control
- Location: `ui/main_window.py`
- Components:
  - Custom title bar with gradient background
  - Activity selector (QComboBox)
  - Color picker (ColorButton)
  - Timer display (QLabel with monospace font)
  - Toggle button (▶ / ■)
  - Menu with always-on-top option

**ColorButton Class:**
- Purpose: Custom styled color selection button
- Location: `ui/main_window.py`
- Extends: QPushButton
- Methods: `get_color()`, `set_color(color)`

## Entry Points

**Primary Entry:**
- Location: `main.py`
- Triggers: Running `python main.py` or `python3 main.py`
- Responsibilities: QApplication creation, Storage initialization, MainWindow instantiation, app.exec() loop

## Error Handling

**Strategy:** Silent fallback to defaults

**Patterns:**
- JSON parse errors: Return default empty data structures
- File not found: Create default empty structures
- Invalid activity name: UI validation (red border on ComboBox)
- No exception propagation: All errors caught locally in Storage methods

## Cross-Cutting Concerns

**Logging:** None (no logging framework)

**Validation:**
- Activity name required before starting timer
- Color required (defaults to #888888)

**Authentication:** Not applicable (local desktop app)

**Window Management:**
- Frameless window with custom title bar
- Drag-to-move via mousePressEvent/mouseMoveEvent
- Minimum size: 280x180
- Always-on-top toggle via Qt.WindowStaysOnTopHint flag
- Window position persistence in settings.json

---

*Architecture analysis: 2026-04-19*