from PySide6.QtWidgets import QWidget,QHBoxLayout,QLabel,QComboBox,QSpinBox,QDoubleSpinBox
from PySide6.QtCore import Signal
class DeviceSelector(QWidget):
    device_changed=Signal(str); scale_changed=Signal(float); refresh_changed=Signal(int)
    def __init__(self,devices,current,parent=None):
        super().__init__(parent); l=QHBoxLayout(self); l.addWidget(QLabel("Device"))
        self.model=QComboBox(); self.model.addItems(devices.keys()); self.model.setCurrentText(current); l.addWidget(self.model)
        self.scale=QDoubleSpinBox(); self.scale.setRange(.35,1.5); self.scale.setSingleStep(.05); self.scale.setValue(devices[current].scale); l.addWidget(self.scale)
        self.refresh=QSpinBox(); self.refresh.setRange(30,240); self.refresh.setValue(devices[current].refresh_rate_hz); self.refresh.setSuffix(" Hz"); l.addWidget(self.refresh)
        self.model.currentTextChanged.connect(self.device_changed); self.scale.valueChanged.connect(self.scale_changed); self.refresh.valueChanged.connect(self.refresh_changed)
