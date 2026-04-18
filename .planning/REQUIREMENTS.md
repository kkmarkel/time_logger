# Requirements: Time Logger

**Defined:** 2026-04-18
**Updated:** 2026-04-19 (pivot to Tauri)
**Stack:** Tauri (Rust + WebView)

**Core Value:** Enable personal productivity by helping users understand where their time goes through simple, visual time tracking.

## v1 Requirements

### Tauri Setup

- [ ] **TAURI-01**: Initialize Tauri project with npm create tauri-app
- [ ] **TAURI-02**: Dev server runs without errors
- [ ] **TAURI-03**: Production .exe builds successfully

### Timer Core

- [ ] **TIMER-01**: User can enter activity name in text field
- [ ] **TIMER-02**: User can select activity from previously logged activities
- [ ] **TIMER-03**: User can assign color to activity
- [ ] **TIMER-04**: User can start/stop timer with toggle button
- [ ] **TIMER-05**: Timer displays elapsed time in HH:MM:SS format
- [ ] **TIMER-06**: UI has transition animations
- [ ] **TIMER-07**: Timer updates every second while running

### Display & Storage

- [ ] **CUMUL-01**: User can view cumulative time per activity
- [ ] **CUMUL-02**: Cumulative time displayed with visual bars
- [ ] **CUMUL-03**: Bars proportionally represent time amounts
- [ ] **DATA-01**: All data persists between app restarts (JSON)
- [ ] **DATA-02**: User can clear all recordings

## Out of Scope

| Feature | Reason |
|---------|--------|
| Weekly reports | Deferred to future version |
| Auto-start with Windows | Not in v1 |
| Export to CSV | Not in v1 |
| Edit/delete recordings | Not in v1 |

## Traceability

| Requirement | Phase | Status |
|--------------|-------|--------|
| TAURI-01 | Phase 1 | Pending |
| TAURI-02 | Phase 1 | Pending |
| TAURI-03 | Phase 1 | Pending |
| TIMER-01 | Phase 2 | Pending |
| TIMER-02 | Phase 2 | Pending |
| TIMER-03 | Phase 2 | Pending |
| TIMER-04 | Phase 2 | Pending |
| TIMER-05 | Phase 2 | Pending |
| TIMER-06 | Phase 2 | Pending |
| TIMER-07 | Phase 2 | Pending |
| CUMUL-01 | Phase 3 | Pending |
| CUMUL-02 | Phase 3 | Pending |
| DATA-01 | Phase 3 | Pending |
| DATA-02 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 13 total
- Mapped to phases: 13
- Unmapped: 0 ✓

---

*Requirements defined: 2026-04-18*
*Last updated: 2026-04-19 after pivot to Tauri*