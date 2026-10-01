from dataclasses import asdict, dataclass, field
from pathlib import Path
import json

STATE_FILE = Path("config/state.json")

@dataclass
class SimulatorState:
    locked: bool = False
    dark_mode: bool = True
    brightness: int = 80
    battery: int = 87
    wifi: bool = True
    airplane_mode: bool = False
    volume: int = 50
    model: str = "iPhone 17 Pro"
    orientation: str = "portrait"
    recent_apps: list[str] = field(default_factory=list)

def load_state():
    if not STATE_FILE.exists(): return SimulatorState()
    try: return SimulatorState(**json.loads(STATE_FILE.read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError): return SimulatorState()

def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(asdict(state), indent=2), encoding="utf-8")
