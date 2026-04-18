# Coding Conventions

**Analysis Date:** 2026-04-19

## Naming Patterns

**Files:**
- Python files use snake_case: `main.py`, `storage.py`, `main_window.py`
- No underscore prefix for private modules

**Classes:**
- PascalCase for class names: `MainWindow`, `ColorButton`, `Storage`

**Functions/Methods:**
- snake_case: `main()`, `_init_ui()`, `_toggle_timer()`, `get_activities()`
- Private methods prefixed with single underscore: `_init_ui`, `_load_previous_activities`, `_restore_window_state`

**Variables:**
- snake_case: `running`, `start_time`, `current_activity_name`, `elapsed_seconds`
- Instance variables prefixed with single underscore for Qt private conventions: `_color` (in ColorButton)

**Constants:**
- SCREAMING_SNAKE_CASE for module-level constants: `PRESET_COLORS`
- Uppercase hex color strings in constant lists: `"#E74C3C"`, `"#3498DB"`

## Code Style

**Formatting:**
- No explicit formatter configured (no .prettierrc, black, or yapf config found)
- Python standard 4-space indentation
- Most string formatting uses f-strings with embedded newlines for stylesheets

**Linting:**
- No explicit linter configured (no .pylintrc, .flake8, or ruff config found)
- Code appears manually checked for common issues

**Imports:**
- Standard library imports first: `import sys`, `import json`, `import os`
- Third-party imports second: `from PySide6.QtWidgets import ...`
- Third-party imports grouped by module level: QtWidgets, QtCore, QtGui
- Alphabetical within groups

## Import Organization

**Order:**
1. Built-in modules: `import sys`, `import json`, `from pathlib import Path`
2. Third-party Qt modules: `from PySide6.QtWidgets import ...`, `from PySide6.QtCore import ...`, `from PySide6.QtGui import ...`

**Path Aliases:**
- No path aliases configured

## Error Handling

**Patterns:**
- Try/except blocks for file I/O: In `storage.py`, `_load_data()` and `_load_settings()` catch `json.JSONDecodeError` and `IOError`
- Fallback to empty defaults on error: Returns `{"activities": []}` or `{"window_position": None, "always_on_top": False}`
- No custom exceptions defined

**Return Values:**
- Methods return `None` for missing data: `get_activity_color()` returns `"#888888"` as default color
- Methods return early on not found: `add_time()` returns after finding match

## Logging

**Framework:** No logging framework configured

**Patterns:** No explicit logging calls in codebase

## Comments

**When to Comment:**
- Minimal comments in code
- Placeholder comments like `# Create title bar` are used

**JSDoc/TSDoc:** Not applicable (Python project)

## Function Design

**Size:** Functions range from simple (5-10 lines) to moderate (30-50 lines)

**Parameters:**
- Explicit parameters: `__init__(self, storage)`, `get_activity_color(self, name)`
- Uses type hints: Not observed in codebase (runs on Python without type checking)

**Return Values:**
- Explicit returns: Most functions have explicit return statements
- Return None implicitly at end of void methods

## Module Design

**Exports:**
- Classes as primary exports via class definition
- No `__all__` defined

**Barrel Files:** Not applicable - small codebase

**Module Organization:**
- `ui/` package for UI components: `ui/main_window.py`
- `data/` package for data layer: `data/storage.py`
- Entry point: `main.py`

## Style Patterns

**Qt Widgets:**
- Double underscores avoided (Python name mangling conflicts with Qt naming)
- Style sheets embedded as multi-line f-strings with CSS

**Data Classes:**
- Dictionary-based data structures: Activity stored as `{"name": name, "color": color, "total_seconds": 0}`
- JSON serialization for persistence: Uses `json.dump()` and `json.load()`

## Window Management

**Window Flags:**
- Uses Qt enums: `Qt.FramelessWindowHint`, `Qt.WindowStaysOnTopHint`
- Flags set via `setWindowFlags()` and combined with bitwise operators

---

*Convention analysis: 2026-04-19*