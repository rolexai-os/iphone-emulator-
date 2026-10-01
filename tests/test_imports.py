def test_imports():
    from app.main import SimulatorWindow
    from app.apps.registry import app_definitions
    assert SimulatorWindow
    assert len(app_definitions()) >= 6
