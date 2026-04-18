# Features Research — Time Logger App

## Table Stakes (Must Have)

Features expected in any time tracking app — users leave if missing:

- **Start/Stop Timer** — Single button to toggle tracking on/off
- **Activity/Project Name** — Enter or select what you're tracking
- **Live Time Display** — Real-time timer showing elapsed time (HH:MM)
- **Data Persistence** — Saved between app restarts
- **Cumulative Time** — Total time per activity

## Differentiators (Competitive)

Features that make the app stand out:

- **Color Coding** — Assign colors to activities (user request)
- **Visual Bars** — Graphical representation of time amounts (user request)
- **Weekly Reports** — Summary view by week (user request)
- **Quick Activity Select** — Dropdown of previously used activities
- **Desktop Fixed Position** — Stays where placed on desktop

## Anti-Features (Don't Build)

Things to deliberately NOT include in v1:

- **Automatic tracking** — Requires always-on, privacy concerns
- **Employee monitoring** — Not a team/productivity tool
- **Cloud sync** — Local storage only (privacy)
- **Screenshots** — Privacy-invasive
- **Invoicing** — Not in scope for personal productivity

## Feature Complexity Notes

| Feature | Complexity | Notes |
|---------|-----------|-------|
| Timer UI | Low | QTimer in PySide6 |
| Activity list | Low | Simple QListWidget |
| Color picker | Low | QColorDialog |
| Visual bars | Medium | QProgressBar or custom painting |
| JSON persistence | Low | Built-in json module |
| Weekly reports | Medium | Date grouping, aggregation |
| Fixed position | Low | QWidget.setFixedPos / window flags |

---

*Features researched: 2026-04-18*
*Sources: memtime.com, timedoctor.com, toggl.com, rize.io*