from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class StatusBar(QLabel):
    def __init__(self, system, parent=None):
        super().__init__(parent)
        self.clock = "--:--"
        self.battery = 0
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color:white;font-weight:600;background:transparent;")
        system.clock_changed.connect(self.set_clock)
        system.battery_changed.connect(self.set_battery)

    def set_clock(self, value):
        self.clock = value
        self.refresh()

    def set_battery(self, value):
        self.battery = value
        self.refresh()

    def refresh(self):
        self.setText(f"{self.clock}    Wi-Fi  •  4G    {self.battery}%")
