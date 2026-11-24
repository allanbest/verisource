#!/usr/bin/env bash
# Build upload-ready zips for the web chat apps.
#   dist/verisource-claude.zip  -> claude.ai (Customize > Skills); also try for ChatGPT skills
#   dist/verisource-gemini.zip  -> gemini.google.com (Customize > Skills)
set -euo pipefail
cd "$(dirname "$0")/.."
SKILL=skills/fact-check
rm -rf dist && mkdir -p dist/tmp
rsync -a --exclude '.DS_Store' --exclude '__pycache__' --exclude '*.pyc' "$SKILL/" dist/tmp/fact-check/
# Claude.ai wants the skill folder inside the zip: fact-check/SKILL.md
(cd dist/tmp && zip -qr ../verisource-claude.zip fact-check)
# Gemini app wants SKILL.md at the zip root
(cd dist/tmp/fact-check && zip -qr ../../verisource-gemini.zip .)
rm -rf dist/tmp
echo "Built:"; ls -1 dist/*.zip
