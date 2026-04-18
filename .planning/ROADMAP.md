# Roadmap: Time Logger

**Granularity:** Coarse (3 phases)
**Mode:** YOLO (auto-approve)
**Requirements:** 19 v1 requirements

## Phase Overview

| # | Phase | Goal | Requirements | Success Criteria |
|---|-------|------|--------------|------------------|
| 1 | Core Timer | Working timer with activity input and fixed window | TIMER-01, TIMER-02, TIMER-03, TIMER-04, TIMER-05, TIMER-06, TIMER-07, WIND-01, WIND-02 | 9 |
| 2 | Data & Display | Persistence, cumulative tracking, visual bars | CUMUL-01, CUMUL-02, CUMUL-03, CUMUL-04, DATA-01, DATA-02, DATA-03, DATA-04 | 8 |
| 3 | Reports | Weekly summary view | REPORT-01, REPORT-02 | 2 |

**Total:** 3 phases | 19 requirements | All covered ✓

---

## Phase 1: Core Timer ✓ Complete

**Goal:** Working start/stop timer with activity selection and fixed desktop position

**Requirements:**
- TIMER-01: Activity name input ✓
- TIMER-02: Activity dropdown (previous) ✓
- TIMER-03: Color picker ✓
- TIMER-04: Start button ✓
- TIMER-05: Stop button (toggle) ✓
- TIMER-06: HH:MM display ✓
- TIMER-07: Second-by-second update ✓
- WIND-01: Fixed position ✓
- WIND-02: Desktop icon behavior ✓

**Success Criteria:** ✓ All 9 criteria met

**Summary:** PySide6 timer with frameless window, activity input, color picker, HH:MM:SS timer, play/stop toggle

**Plans:**
- [x] 01-01-PLAN.md — Initial implementation (complete)
- [x] 01-02-PLAN.md — UAT gap fixes (complete)

---

## Phase 2: Data & Display

**Goal:** Cumulative tracking with visual bars and JSON persistence

**Requirements:**
- CUMUL-01: Cumulative time per activity
- CUMUL-02: Visual bars displayed
- CUMUL-03: Proportional bar widths
- CUMUL-04: Sorted by time (top shown)
- DATA-01: Clear all button
- DATA-02: Clear last button
- DATA-03: Data persists across restarts
- DATA-04: JSON file storage

**Success Criteria:**
1. Each activity shows total time logged
2. Visual bars represent time amounts
3. Longer times show longer bars
4. Activities sorted by cumulative time
5. Clear All removes all recordings
6. Clear Last removes most recent
7. Data loads on app start
8. Data saves on each change

---

## Phase 3: Weekly Reports

**Goal:** Weekly time summary view

**Requirements:**
- REPORT-01: Weekly summary
- REPORT-02: Compact weekly totals

**Success Criteria:**
1. User can view time grouped by week
2. Weekly totals shown in compact form

---

## Execution

**Parallelization:** Independent plans can run in parallel
**Phase transition:** `/gsd-transition` after each phase
**Verification:** `/gsd-verify` after phase execution

---

*Roadmap created: 2026-04-18*
*Last updated: 2026-04-18 after roadmap creation*