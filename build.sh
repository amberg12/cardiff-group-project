#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
npm install
npm run build

echo "Build complete. Run the app with: source .venv/bin/activate && flask --app app.py run"
