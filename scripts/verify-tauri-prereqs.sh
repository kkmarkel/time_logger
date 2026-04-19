#!/usr/bin/env bash
set -euo pipefail

INSTALL_GUIDANCE="sudo apt update && sudo apt install -y build-essential libwebkit2gtk-4.1-dev librsvg2-dev patchelf"

echo "[tauri:prereqs] Checking host prerequisites for Tauri dev/build..."

if ! command -v cc >/dev/null 2>&1; then
  echo "[tauri:prereqs] ERROR: Missing C linker/compiler ('cc') in PATH."
  echo "[tauri:prereqs] Install required dependencies:"
  echo "  ${INSTALL_GUIDANCE}"
  exit 1
fi

set +e
TAURI_INFO_OUTPUT="$(npm run tauri -- info 2>&1)"
TAURI_INFO_STATUS=$?
set -e

printf '%s\n' "${TAURI_INFO_OUTPUT}"

if [[ ${TAURI_INFO_STATUS} -ne 0 ]]; then
  echo "[tauri:prereqs] ERROR: 'npm run tauri -- info' failed (exit ${TAURI_INFO_STATUS})."
fi

if [[ "${TAURI_INFO_OUTPUT}" == *"webkit2gtk-4.1"* ]] || [[ "${TAURI_INFO_OUTPUT}" == *"rsvg2"* ]] || [[ "${TAURI_INFO_OUTPUT}" == *"linker \\`cc\\` not found"* ]] || [[ "${TAURI_INFO_OUTPUT}" == *"linker 'cc' not found"* ]]; then
  echo "[tauri:prereqs] ERROR: Missing Linux prerequisites detected (webkit2gtk-4.1, rsvg2, or linker)."
  echo "[tauri:prereqs] Install required dependencies:"
  echo "  ${INSTALL_GUIDANCE}"
  exit 1
fi

if [[ ${TAURI_INFO_STATUS} -ne 0 ]]; then
  exit ${TAURI_INFO_STATUS}
fi

echo "[tauri:prereqs] OK: Host prerequisite checks passed."
