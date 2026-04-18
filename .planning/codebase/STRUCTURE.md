# Codebase Structure

**Analysis Date:** 2026-04-19

## Directory Layout

```
time_logger/
├── main.py                # Application entry point
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── data/                 # Data persistence layer
│   └── storage.py        # Storage class
├── ui/                   # UI layer
│   └── main_window.py   # MainWindow and ColorButton classes
└── __pycache__/         # Generated Python bytecode (not committed)
```

## Directory Purposes

**Root (`/`):**
- Purpose: Entry points and project metadata
- Contains: main.py, requirements.txt, README.md
- Key files: `main.py` (bootstrap), `requirements.txt` (dependencies)

**`data/`:**
- Purpose: Data storage and persistence
- Contains: Storage class for managing activities and settings
- Key files: `data/storage.py`

**`ui/`:**
- Purpose: User interface components
- Contains: MainWindow, ColorButton
- Key files: `ui/main_window.py`

**Hidden directories (not committed):**
- `.timelogger/` - Created at runtime in user's home directory
  - Contains: `data.json`, `settings.json`
- `__pycache__/` - Python bytecode cache

## Key File Locations

**Entry Points:**
- `main.py`: Application bootstrap (invoke via `python main.py`)

**Configuration:**
- `requirements.txt`: Single dependency (PySide6)
- No other config files present

**Core Logic:**
- `ui/main_window.py`: MainWindow class (470 lines)
- `data/storage.py`: Storage class (86 lines)

**Testing:**
- Not present (no test files found)

## Naming Conventions

**Files:**
- `snake_case.py`: All Python files use snake_case
- Example: `main_window.py`, `storage.py`

**Directories:**
- `snake_case/`: All directories use snake_case
- Example: `ui/`, `data/`

**Classes:**
- `PascalCase`: All classes use PascalCase
- Example: `MainWindow`, `ColorButton`, `Storage`

**Methods/Functions:**
- `snake_case`: All methods use snake_case (with leading underscore for private)
- Example: `_init_ui()`, `_load_previous_activities()`, `get_activities()`

**Variables:**
- `snake_case`: All variables use snake_case
- Example: `current_activity_name`, `elapsed_seconds`

## Where to Add New Code

**New Feature:**
- Primary code: Add to `ui/main_window.py` (for UI features) or `data/storage.py` (for data features)
- No separate test directory exists

**New Component/Module:**
- If new UI component: Add class to `ui/main_window.py` or create new file in `ui/`
- If new data module: Add to `data/storage.py` or create new file in `data/`

**Utilities:**
- Shared helpers: Not presently organized (would go alongside existing modules)

## Special Directories

**`.timelogger/` (runtime-created):**
- Purpose: Persistent data storage
- Created by: `Storage.__init__()` on first run
- Contents: `data.json`, `settings.json`
- Committed: No (gitignored via .gitignore)

**`__pycache__/`:**
- Purpose: Python bytecode cache
- Generated: Yes (by Python interpreter)
- Committed: No (gitignored)

---

*Structure analysis: 2026-04-19*