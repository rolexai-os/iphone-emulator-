from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QComboBox,QSlider
from PySide6.QtCore import Qt
class SettingsApp(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent); root=QVBoxLayout(self)
        h=QLabel("Settings"); h.setStyleSheet("font-size:28px;font-weight:700;"); root.addWidget(h)
        root.addWidget(QLabel("Appearance")); c=QComboBox(); c.addItems(["Light","Dark","System"]); root.addWidget(c)
        root.addWidget(QLabel("Refresh Rate")); r=QComboBox(); r.addItems(["60 Hz","90 Hz","120 Hz"]); root.addWidget(r)
        root.addWidget(QLabel("Brightness")); s=QSlider(Qt.Horizontal); s.setRange(10,100); s.setValue(80); root.addWidget(s)
        root.addWidget(QLabel("Device simulation settings are applied from config/device.json.")); root.addStretch()
