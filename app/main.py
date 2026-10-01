import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QStackedWidget,QPushButton,QHBoxLayout,QLabel
from .core.device import default_device, load_devices
from .core.system import SimulatedSystem
from .core.state import load_state, save_state
from .core.lifecycle import AppLifecycle, AppState
from .core.gestures import GestureController
from .ui.home import HomeScreen
from .ui.lockscreen import LockScreen
from .ui.statusbar import StatusBar
from .ui.overlays import OverlayPanel
from .ui.device_selector import DeviceSelector
from .apps.registry import app_definitions

class SimulatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.devices=load_devices(); self.state=load_state()
        if self.state.model not in self.devices: self.state.model=default_device().name
        self.device=self.devices[self.state.model]
        self.system=SimulatedSystem(self); self.system.battery=self.state.battery
        self.setWindowTitle(f"iPhone Emulator — {self.device.name} — {self.device.refresh_rate_hz} Hz")
        self.resize(640,1040); self.setMinimumSize(520,820)
        outer=QVBoxLayout(); outer.setAlignment(Qt.AlignCenter)
        self.central=QWidget(); self.setCentralWidget(self.central); self.central.setLayout(outer)
        self.selector=DeviceSelector(self.devices,self.device.name)
        self.selector.device_changed.connect(self.change_device)
        self.selector.scale_changed.connect(self.change_scale)
        self.selector.refresh_changed.connect(self.change_refresh)
        outer.addWidget(self.selector)
        self.frame=QWidget(); self.frame.setObjectName("frame"); outer.addWidget(self.frame)
        layout=QVBoxLayout(self.frame); layout.setContentsMargins(10,10,10,10)
        bar=QWidget(); bl=QHBoxLayout(bar); self.status=StatusBar(self.system); bl.addWidget(self.status); layout.addWidget(bar)
        self.stack=QStackedWidget(); layout.addWidget(self.stack)
        self.home=HomeScreen(app_definitions()); self.lock=LockScreen()
        self.stack.addWidget(self.home); self.stack.addWidget(self.lock)
        self.lock.unlock_requested.connect(self.unlock)
        self.home.app_requested.connect(self.launch_app)
        self.home.control_center_requested.connect(lambda:self.show_overlay("Control Center","Wi-Fi: On\nBluetooth: On\nAirplane Mode: Off\nBrightness: 80%"))
        self.home.notification_center_requested.connect(lambda:self.show_overlay("Notification Center","No new notifications."))
        home=QPushButton("●  Home"); home.clicked.connect(self.go_home); layout.addWidget(home)
        self.frame.setStyleSheet("#frame{background:#050507;border:9px solid #171717;border-radius:48px;} QPushButton{color:white;background:#242424;border:0;padding:8px;border-radius:14px;} QLabel{color:white;}")
        self.gestures=GestureController(self)
        self.gestures.swipe_up.connect(self.go_home)
        self.gestures.swipe_down.connect(lambda:self.show_overlay("Control Center","Wi-Fi: On\nBrightness: 80%\nVolume: 50%"))
        self.lifecycle={}
        self.apply_device_geometry()
        self.stack.setCurrentWidget(self.lock if self.state.locked else self.home)

    def apply_device_geometry(self):
        w=int(self.device.width*self.selector.scale.value()); h=int(self.device.height*self.selector.scale.value())
        self.stack.setMinimumSize(w,h); self.stack.setMaximumSize(w,h)
        self.setWindowTitle(f"iPhone Emulator — {self.device.name} — {self.selector.refresh.value()} Hz")

    def change_device(self,name):
        self.device=self.devices[name]; self.state.model=name; save_state(self.state)
        self.selector.scale.blockSignals(True); self.selector.scale.setValue(self.device.scale); self.selector.scale.blockSignals(False)
        self.selector.refresh.blockSignals(True); self.selector.refresh.setValue(self.device.refresh_rate_hz); self.selector.refresh.blockSignals(False)
        self.apply_device_geometry()

    def change_scale(self,value):
        self.apply_device_geometry(); self.state.model=self.device.name; save_state(self.state)

    def change_refresh(self,value):
        self.apply_device_geometry(); save_state(self.state)

    def unlock(self):
        self.state.locked=False; save_state(self.state); self.stack.setCurrentWidget(self.home)

    def go_home(self):
        self.stack.setCurrentWidget(self.home)

    def launch_app(self,name):
        if name in self.lifecycle: self.lifecycle[name].transition(AppState.ACTIVE)
        else:
            self.lifecycle[name]=AppLifecycle(name,self); self.lifecycle[name].transition(AppState.ACTIVE)
        if name in self.state.recent_apps: self.state.recent_apps.remove(name)
        self.state.recent_apps.insert(0,name); self.state.recent_apps=self.state.recent_apps[:8]; save_state(self.state)
        definition=next(x for x in app_definitions() if x["name"]==name)
        container=QWidget(); layout=QVBoxLayout(container)
        back=QPushButton("‹ Home"); back.clicked.connect(lambda:self.close_app(name,container)); layout.addWidget(back)
        title=QLabel(name); title.setStyleSheet("font-size:22px;font-weight:700;padding:6px;"); layout.addWidget(title)
        layout.addWidget(definition["widget"]()); self.stack.addWidget(container); self.stack.setCurrentWidget(container)

    def close_app(self,name,container):
        if name in self.lifecycle: self.lifecycle[name].transition(AppState.BACKGROUND)
        self.stack.removeWidget(container); container.deleteLater(); self.go_home()

    def show_overlay(self,title,body):
        overlay=OverlayPanel(title,body,self.central); overlay.setGeometry(self.central.rect().adjusted(25,100,-25,-70)); overlay.show()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_L and event.modifiers() & Qt.ControlModifier:
            self.state.locked=not self.state.locked; save_state(self.state)
            self.stack.setCurrentWidget(self.lock if self.state.locked else self.home)
        super().keyPressEvent(event)

    def closeEvent(self,event):
        self.state.battery=self.system.battery; save_state(self.state); event.accept()

def main():
    app=QApplication(sys.argv); app.setApplicationName("iPhone Emulator"); app.setStyle("Fusion")
    window=SimulatorWindow(); window.show(); return app.exec()

if __name__=="__main__": main()
