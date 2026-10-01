from dataclasses import dataclass
from pathlib import Path
import json

@dataclass(frozen=True)
class DeviceProfile:
    name: str
    width: int
    height: int
    scale: float
    refresh_rate_hz: int
    corner_radius: int
    color: str

    @property
    def logical_size(self):
        return self.width, self.height

def load_devices(path="config/device.json"):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {name: DeviceProfile(name=name, **cfg) for name, cfg in data["models"].items()}

def default_device(path="config/device.json"):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return load_devices(path)[data["default_model"]]
