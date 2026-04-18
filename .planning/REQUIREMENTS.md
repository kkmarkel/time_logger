# Requirements: Time Logger

**Defined:** 2026-04-18
**Core Value:** Enable personal productivity by helping users understand where their time goes through simple, visual time tracking.

## v1 Requirements

### Core Timer

- [ ] **TIMER-01**: User can enter activity name in text field
- [ ] **TIMER-02**: User can select activity from previously logged activities dropdown
- [ ] **TIMER-03**: User can assign color to activity via color picker
- [ ] **TIMER-04**: User can start timer with single button click
- [ ] **TIMER-05**: User can stop timer with same button (toggle)
- [ ] **TIMER-06**: Timer displays elapsed time in HH:MM format
- [ ] **TIMER-07**: Timer updates every second while running

### Cumulative Display

- [ ] **CUMUL-01**: User can view cumulative time per activity
- [ ] **CUMUL-02**: Cumulative time displayed with visual bars
- [ ] **CUMUL-03**: Bars proportionally represent time amounts
- [ ] **CUMUL-04**: Top activities shown (sorted by time)

### Data Management

- [ ] **DATA-01**: User can clear all recordings with "Clear" button
- [ ] **DATA-02**: User can clear last recording with "Clear Last" button
- [ ] **DATA-03**: All data persists between app restarts
- [ ] **DATA-04**: Data saved to JSON file in app directory

### Window Behavior

- [ ] **WIND-01**: App window stays at fixed position on desktop
- [ ] **WIND-02**: App acts as desktop icon (compact, always visible)

### Weekly Reports

- [ ] **REPORT-01**: User can view time summary by week
- [ ] **REPORT-02**: Weekly totals displayed in compact view

## v2 Requirements

### Extensions (Not in v1)

- **AUTO-01**: App auto-starts with Windows (optional)
- **EXPORT-01**: Export data to CSV
- **EDIT-01**: Edit/delete past recordings
- **DAILY-01**: Daily totals view

## Out of Scope

| Feature | Reason |
|---------|--------|
| Automatic tracking | Not requested, privacy concerns |
| Cloud sync | Local storage only |
| Employee monitoring | Not team productivity tool |
| Invoicing | Not personal productivity focus |
| Mobile app | Windows desktop only |

## Traceability

| Requirement | Phase | Status |
|--------------|-------|--------|
| TIMER-01 | Phase 1 | Pending |
| TIMER-02 | Phase 1 | Pending |
| TIMER-03 | Phase 1 | Pending |
| TIMER-04 | Phase 1 | Pending |
| TIMER-05 | Phase 1 | Pending |
| TIMER-06 | Phase 1 | Pending |
| TIMER-07 | Phase 1 | Pending |
| CUMUL-01 | Phase 2 | Pending |
| CUMUL-02 | Phase 2 | Pending |
| CUMUL-03 | Phase 2 | Pending |
| CUMUL-04 | Phase 2 | Pending |
| DATA-01 | Phase 2 | Pending |
| DATA-02 | Phase 2 | Pending |
| DATA-03 | Phase 2 | Pending |
| DATA-04 | Phase 2 | Pending |
| WIND-01 | Phase 1 | Pending |
| WIND-02 | Phase 1 | Pending |
| REPORT-01 | Phase 3 | Pending |
| REPORT-02 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 19 total
- Mapped to phases: 19
- Unmapped: 0 ✓

---

*Requirements defined: 2026-04-18*
*Last updated: 2026-04-18 after initial definition*