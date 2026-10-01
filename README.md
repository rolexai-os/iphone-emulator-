# iPhone Emulator

A Python/PySide6 desktop iPhone-style simulator for UI, system-flow and app prototyping. It is not a real iOS runtime and does not run signed iOS binaries.

## Features
- iPhone-style GUI and device frame
- Configurable model, resolution, scale and refresh rate
- Lock screen and Home screen
- Status bar, Control Center and Notification Center
- Calculator, Settings, Messages, Phone, Photos and Browser demos
- Modular app registry
- Tests and changelog

## Setup

### Windows PowerShell
```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

## Test
```bash
python -m pytest
```

## Update an existing installation
```bash
git pull
python -m pip install -r requirements.txt --upgrade
python run.py
```

Device profiles are in `config/device.json`. Add simulated apps under `app/apps/` and register them in `app/apps/registry.py`.
