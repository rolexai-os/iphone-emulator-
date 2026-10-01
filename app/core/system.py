from datetime import datetime
from PySide6.QtCore import QObject, QTimer, Signal

class SimulatedSystem(QObject):
    clock_changed = Signal(str)
    battery_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.battery = 87
        self.wifi = True
        self.signal = 4
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.tick()

    def tick(self):
        self.clock_changed.emit(datetime.now().strftime("%H:%M"))
        self.battery_changed.emit(self.battery)
