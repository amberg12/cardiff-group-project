# Basic Flask + Bootstrap + TypeScript App

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm

## Build

### Linux / macOS

```bash
./build.sh
```

This script will:
- create `.venv`
- install Python dependencies from `requirements.txt`
- install Node dependencies
- compile TypeScript to `app/static/dist`

### Windows (PowerShell)

```powershell
.\build.ps2
```

This script will do the same setup/build steps for Windows.

## Run

After building, run:

```bash
flask --app app.py run
```

Open the app at:
- Home page: `http://127.0.0.1:5000/`
- Send test data page: `http://127.0.0.1:5000/send-test-data`

## What the app does

- `/send-test-data` sends random `temperature`, `humidity`, and `light` values to `POST /api/readings`.
- The backend stores readings in a global in-memory list of dataclass entries.
- `/` displays all stored readings.

## Notes

- Data is in-memory only and resets when the Flask server restarts.
