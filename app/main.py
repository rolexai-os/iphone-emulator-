import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QStackedWidget,QPushButton,QHBoxLayout
from .core.device import default_device, load_devices
from .core.system import SimulatedSystem
from .ui.home import HomeScreen
from .ui.lockscreen import LockScreen
from .ui.statusbar import StatusBar
from .ui.overlays import OverlayPanel
from .apps.registry import app_definitions

class SimulatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.devices=load_devices(); self.device=default_device(); self.system=SimulatedSystem(self)
        self.setWindowTitle(f"iPhone Emulator — {self.device.name} — {self.device.refresh_rate_hz} Hz")
        self.resize(600,960); self.setMinimumSize(500,780)
        outer=QVBoxLayout(); outer.setAlignment(Qt.AlignCenter)
        self.central=QWidget(); self.setCentralWidget(self.central); self.central.setLayout(outer)
        self.frame=QWidget(); self.frame.setObjectName("frame"); outer.addWidget(self.frame)
        layout=QVBoxLayout(self.frame); layout.setContentsMargins(10,10,10,10)
        bar=QWidget(); bl=QHBoxLayout(bar); bl.setContentsMargins(8,2,8,2)
        self.status=StatusBar(self.system); bl.addWidget(self.status); layout.addWidget(bar)
        self.stack=QStackedWidget(); layout.addWidget(self.stack)
        self.home=HomeScreen(app_definitions()); self.lock=LockScreen()
        self.stack.addWidget(self.home); self.stack.addWidget(self.lock)
        self.lock.unlock_requested.connect(lambda:self.stack.setCurrentWidget(self.home))
        self.home.app_requested.connect(self.launch_app)
        self.home.control_center_requested.connect(lambda:self.show_overlay("Control Center","Wi-Fi: On\nBluetooth: On\nAirplane Mode: Off\nBrightness: 80%"))
        self.home.notification_center_requested.connect(lambda:self.show_overlay("Notification Center","No new notifications."))
        home=QPushButton("●  Home"); home.clicked.connect(lambda:self.stack.setCurrentWidget(self.home)); layout.addWidget(home)
        self.frame.setStyleSheet("#frame{background:#050507;border:9px solid #171717;border-radius:48px;} QPushButton{color:white;background:#242424;border:0;padding:8px;border-radius:14px;} QLabel{color:white;}")
        self.apply_device_geometry()

    def apply_device_geometry(self):
        w=int(self.device.width*self.device.scale); h=int(self.device.height*self.device.scale)
        self.stack.setMinimumSize(w,h); self.stack.setMaximumSize(w,h)

    def launch_app(self,name):
        definition=next(x for x in app_definitions() if x["name"]==name)
        container=QWidget(); layout=QVBoxLayout(container)
        back=QPushButton("‹ Home"); back.clicked.connect(lambda:self.stack.setCurrentWidget(self.home)); layout.addWidget(back)
        layout.addWidget(definition["widget"]()); self.stack.addWidget(container); self.stack.setCurrentWidget(container)

    def show_overlay(self,title,body):
        overlay=OverlayPanel(title,body,self.central); overlay.setGeometry(self.central.rect().adjusted(25,80,-25,-70)); overlay.show()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_L and event.modifiers() & Qt.ControlModifier:
            self.stack.setCurrentWidget(self.lock if self.stack.currentWidget() is self.home else self.home)
        super().keyPressEvent(event)

def main():
    app=QApplication(sys.argv); app.setApplicationName("iPhone Emulator"); app.setStyle("Fusion")
    window=SimulatorWindow(); window.show(); return app.exec()

if __name__=="__main__":
    main()
