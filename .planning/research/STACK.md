# Stack Research — Time Logger App

## Recommended Stack

**Primary:** PySide6 (Qt for Python) — Official Qt bindings for Python
**Version:** Qt 6.x with PySide6 6.x
**Python:** 3.9+

## Why PySide6

- Official Qt bindings (LGPL license, commercial-friendly)
- Native Windows look and feel
- Rich widget library for desktop apps
- Cross-platform potential (Windows, macOS, Linux)
- Mature, well-documented
- Used by: Dropbox, VirtualBox, Autodesk Maya

## Libraries

### UI/Desktop
- `PySide6` — Main framework
- `PySide6-Addons` — Additional widgets (Qt Designer, etc.)
- `PySide6-Extras` — Extra utilities

### Data Storage
- `json` — Built-in (user preference for simplicity)
- Or: `sqlite3` (built-in) for larger datasets

### Distribution (future)
- `PyInstaller` — Create Windows .exe
- Or: `cx_Freeze` — Alternative packager

## What NOT to Use

- **PyQt6** — GPL license, commercial restrictions
- **Tkinter** — Limited desktop capabilities
- **Electron** — Overkill for this use case
- **CustomTkinter** — More limited than full Qt

## Version Guidance

- Qt 6.x (current stable)
- PySide6 6.x (matching Qt version)
- Avoid Qt 5/PySide2 (older)

## Confidence: HIGH

PySide6 is the right choice for a Windows desktop time tracking app based on user requirements.

---

*Stack researched: 2026-04-18*
*Source: pythonguis.com, pythoncentral.io, learnpyqt.com*