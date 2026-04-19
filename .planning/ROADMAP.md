# Roadmap: Time Logger

**Granularity:** Coarse (3 phases)
**Mode:** YOLO (auto-approve)
**Tech Stack:** Tauri (Rust + WebView)

## PIVOT NOTE

2026-04-19: Stack changed from PySide6 to Tauri. Old PySide6 implementation archived. Rebuilding UI.

## Phase Overview

| # | Phase | Goal | Requirements | Success Criteria |
|---|-------|------|--------------|------------------|
| 1 | Tauri Setup | Initialize Tauri project with dev environment | TAURI-01, TAURI-02, TAURI-03 | 3 |
| 2 | Timer Core | Working timer with activity tracking and animations | TIMER-01, TIMER-02, TIMER-03, TIMER-04, TIMER-05, TIMER-06 | 6 |
| 3 | Display & Storage | Cumulative display, visual bars, JSON persistence | CUMUL-01, CUMUL-02, DATA-01, DATA-02 | 4 |

**Total:** 3 phases | 13 requirements | All covered ✓

---

## Phase 1: Tauri Setup

**Goal:** Initialize Tauri project with working dev environment

**Requirements:**
- TAURI-01: Tauri project scaffolded
- TAURI-02: Dev server runs without errors
- TAURI-03: .exe builds successfully

**Success Criteria:**
1. `npm run tauri dev` starts without errors
2. Empty window displays
3. `npm run tauri build` produces .exe

**Plans:** 2 plans

**Plan list:**
- [x] 01-01-PLAN.md — Initialize Tauri project with Svelte frontend
- [x] 01-02-PLAN.md — Close TAURI-02/TAURI-03 verification gaps with prerequisite + build evidence

---

## Phase 2: Timer Core

**Goal:** Working timer with activity tracking and transition animations

**Requirements:**
- TIMER-01: Activity name input field
- TIMER-02: Activity dropdown (from history)
- TIMER-03: Color picker
- TIMER-04: Start/Stop toggle button
- TIMER-05: Timer display (HH:MM:SS)
- TIMER-06: UI transition animations

**Success Criteria:**
1. User can enter activity name
2. User can select previous activity
3. User can pick color
4. Start/stop toggle works
5. Timer updates every second
6. UI animates on state changes

---

## Phase 3: Display & Storage

**Goal:** Cumulative time display with visual bars and JSON persistence

**Requirements:**
- CUMUL-01: Cumulative time per activity
- CUMUL-02: Visual bars (proportional)
- DATA-01: Data persists to JSON
- DATA-02: Clear functionality

**Success Criteria:**
1. Shows total time per activity
2. Visual bars represent amounts
3. Data saves on changes
4. Data loads on start
5. Clear all/clear last work

---

## Execution

**Parallelization:** Independent plans can run in parallel
**Phase transition:** `/gsd-transition` after each phase
**Verification:** `/gsd-verify` after phase execution

---

*Roadmap created: 2026-04-18*
*Last updated: 2026-04-19 after pivot to Tauri*
