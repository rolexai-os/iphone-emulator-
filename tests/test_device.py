from app.core.device import load_devices, default_device

def test_profiles():
    devices=load_devices()
    assert len(devices) >= 4
    assert default_device().width > 0
    assert default_device().height > 0
    assert default_device().refresh_rate_hz in (60,90,120,144,165)
