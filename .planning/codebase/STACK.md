# Technology Stack

**Analysis Date:** 2026-04-19

## Languages

**Primary:**
- Python 3.x - Core application logic, UI, and data storage

**Secondary:**
- None detected

## Runtime

**Environment:**
- Python interpreter (system-installed)
- No virtual environment configuration detected

**Package Manager:**
- pip (standard)
- Dependencies defined in: `requirements.txt`

## Frameworks

**Core:**
- PySide6 >= 6.5.0 - Qt for Python GUI framework
  - Provides: Widgets, dialogs, styling, window management
  - Used in: `ui/main_window.py`, `main.py`

**Build/Dev:**
- None detected (simple pip-based setup)

## Key Dependencies

**Critical:**
- PySide6 >= 6.5.0 - All UI components (QApplication, QWidget, QLabel, QPushButton, QComboBox, QColorDialog, etc.)

**No additional third-party dependencies detected.**

## Configuration

**Environment:**
- No environment variable configuration required
- Application stores data locally in user home directory

**Data Storage:**
- Location: `~/.timelogger/` (user home directory)
- Files:
  - `data.json` - Activity time logs (activities, names, colors, total_seconds)
  - `settings.json` - Window position (x, y) and always-on-top flag
- Format: JSON

**No build configuration files detected** (no tsconfig.json, no package.json for this project).

## Platform Requirements

**Development:**
- Python 3.x
- pip package manager
- PySide6 >= 6.5.0

**Production:**
- Desktop runtime with display (X11/Wayland on Linux, equivalent on macOS/Windows)
- No server-side deployment

---

*Stack analysis: 2026-04-19*