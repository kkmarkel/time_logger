#!/usr/bin/env bash
set -euo pipefail

ARTIFACT_PATH="src-tauri/target/release/bundle/nsis/time_logger.exe"
DEV_LOG="$(mktemp)"

cleanup() {
  rm -f "${DEV_LOG}"
}
trap cleanup EXIT

echo "[phase1:verify] Step 1/3: Running prerequisite gate"
npm run tauri:prereqs

echo "[phase1:verify] Step 2/3: Proving dev startup with bounded timeout"
set +e
timeout 120s npm run tauri dev >"${DEV_LOG}" 2>&1
DEV_STATUS=$?
set -e

cat "${DEV_LOG}"

if [[ ${DEV_STATUS} -ne 0 && ${DEV_STATUS} -ne 124 ]]; then
  echo "[phase1:verify] ERROR: 'npm run tauri dev' exited with ${DEV_STATUS}."
  exit ${DEV_STATUS}
fi

if ! grep -Eq "Running (BeforeDevCommand|DevCommand)|Dev server running|Local:" "${DEV_LOG}"; then
  echo "[phase1:verify] ERROR: Could not find startup evidence in dev output."
  exit 1
fi

if grep -Eq "linker ['\"][^'\"]*cc[^'\"]*['\"] not found|webkit2gtk-4.1|rsvg2|error:" "${DEV_LOG}"; then
  echo "[phase1:verify] ERROR: Detected build/runtime errors during dev startup proof."
  exit 1
fi

echo "[phase1:verify] Step 3/3: Running production build"
npm run tauri build

if [[ ! -f "${ARTIFACT_PATH}" ]]; then
  echo "[phase1:verify] ERROR: Expected artifact not found: ${ARTIFACT_PATH}"
  exit 1
fi

echo "[phase1:verify] OK: Verified artifact exists at ${ARTIFACT_PATH}"
