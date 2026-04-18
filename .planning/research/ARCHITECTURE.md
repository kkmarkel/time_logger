# Architecture Research — Time Logger App

## Application Structure

Single-window desktop application with Qt Widgets.

## Components

### Main Window (QWDialog/QWidget)
- Fixed position on desktop
- Always on top option
- Compact layout

### Timer Display
- QLabel for HH:MM:SS format
- QTimer updating every second

### Activity Section
- QLineEdit for new activity name
- QComboBox for previous activities
- QPushButton for start/stop
- QColorDialog for color selection

### Time Display
- QLabel for current session time
- QListWidget for cumulative times with bars

### Actions
- QPushButton "Clear All"
- QPushButton "Clear Last"

### Data Storage
- JSON file in AppData or app directory

## Data Flow

1. User enters/selects activity
2. User selects color (optional)
3. User clicks Start → Timer begins, timer displayed
4. User clicks Stop → Session saved, cumulative updated
5. Data persisted to JSON on each change
6. On load: Data restored from JSON

## Build Order

1. **Phase 1**: Basic window + timer start/stop
2. **Phase 2**: Activity management + persistence
3. **Phase 3**: Visual bars + cumulative display
4. **Phase 4**: Weekly reports (optional)

## Component Boundaries

- **UI Layer**: PySide6 widgets
- **Logic Layer**: Time calculation, data aggregation
- **Storage Layer**: JSON read/write

---

*Architecture researched: 2026-04-18*
*Source: pythonguis.com, learnpyqt.com*