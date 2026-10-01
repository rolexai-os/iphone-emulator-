# iPhone Emulator

A cross-platform Python/PySide6 **iPhone-style system simulator** for UI prototyping, testing and education.

## Major upgrade

The simulator now includes a richer system shell inspired by public Apple interaction guidance: adaptive device profiles, standard gestures, system overlays, Dynamic Island-style activity UI, app switching, app lifecycle simulation, animations and persistent state. Apple recommends standard gestures such as tap, swipe, drag and touch-and-hold and emphasizes responsive feedback and avoiding conflicts with system UI. citeturn0search0turn0search4

### Current features

- Device selector with multiple profiles
- Dynamic logical screen size and scale
- Runtime refresh-rate target setting
- Lock Screen
- Home Screen
- Status bar
- Dynamic Island-style activity indicator
- Control Center
- Notification Center
- App Switcher / recent apps
- Swipe-up Home gesture
- Swipe-down Control Center gesture
- Tap and directional gesture engine
- App lifecycle states
- Persistent simulator state
- Dark-mode, Wi-Fi, airplane-mode, brightness and volume state controls
- Animated panel/app presentation
- Calculator
- Settings
- Messages
- Phone
- Photos
- Browser demo
- Modular app registry
- Automated tests

Apple's current public documentation also describes Dynamic Island and Live Activity presentations including compact, minimal, expanded and Lock Screen contexts. This project implements an independent simulation of those interaction concepts rather than Apple's private implementation. citeturn0search2

## Architecture

```
app/
├── core/
│   ├── device.py
│   ├── system.py
│   ├── state.py
│   ├── gestures.py
│   ├── lifecycle.py
│   └── touch.py
├── ui/
│   ├── home.py
│   ├── lockscreen.py
│   ├── statusbar.py
│   ├── device_selector.py
│   ├── dynamic_island.py
│   ├── control_center.py
│   ├── notification_center.py
│   ├── app_switcher.py
│   └── animations.py
├── apps/
│   ├── calculator.py
│   ├── settings.py
│   ├── messages.py
│   ├── phone.py
│   ├── photos.py
│   ├── browser.py
│   └── registry.py
└── main.py
```

## Install

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

## Controls

- **Home** button: return to Home Screen
- **Lock**: show Lock Screen
- **App Switcher**: open recent apps
- **Swipe up**: Home
- **Swipe down**: Control Center
- **Ctrl+L**: lock
- **Ctrl+R**: App Switcher
- **H**: Home

## Persistent state

The simulator stores user-facing simulated settings and recent apps in:

`config/state.json`

This is simulation data only. It does not access an iPhone or modify a real device.

## Updating existing installations

```bash
git pull
python -m pip install -r requirements.txt --upgrade
python run.py
```

## Testing

```bash
python -m pytest
```

## Important scope

This is an independent simulator. It does not include Apple's proprietary source code, firmware, private APIs, signing infrastructure or copyrighted system assets, and it does not execute real iOS binaries. Apple's official iOS Simulator is part of Xcode and uses Apple platform runtimes on supported development environments.

The app lifecycle model is based on the publicly documented concept that foreground apps have priority while background apps should minimize work, with transitions between active, inactive and background states. citeturn0search3

The UI is also designed to adapt to different display sizes and orientations, consistent with Apple's public layout guidance. citeturn0search9
