# Research Summary — Time Logger App

## Key Findings

### Stack
**PySide6** (Qt for Python) — Modern, well-documented, native Windows look
- Qt 6.x with PySide6 6.x
- Python 3.9+
- PyInstaller for .exe creation

### Table Stakes
- Start/Stop timer
- Activity naming
- Live time display
- Data persistence (JSON)
- Cumulative tracking

### Differentiators (User Requested)
- Color-coded activities
- Visual time bars
- Weekly reports
- Fixed desktop position

### Watch Out For
1. **Timer drift** — Use system time delta, not accumulated ticks
2. **Data loss** — Save on every stop, not just exit
3. **Window covering** — Use Qt.Tool flag or always-on-top
4. **Activity duplicates** — Normalize names before lookup

## Files

- `.planning/research/STACK.md` — Tech stack
- `.planning/research/FEATURES.md` — Feature categories
- `.planning/research/ARCHITECTURE.md` — App structure
- `.planning/research/PITFALLS.md` — Common mistakes

---

*Summary created: 2026-04-18*
*Sources: pythonguis.com, learnpyqt.com, timedoctor.com, toggl.com*