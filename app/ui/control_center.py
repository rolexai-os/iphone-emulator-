from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget,QGridLayout,QPushButton,QSlider,QLabel,QVBoxLayout

class ControlCenter(QWidget):
    closed=Signal()
    changed=Signal(str,bool)
    def __init__(self,state,parent=None):
        super().__init__(parent); self.state=state
        root=QVBoxLayout(self)
        title=QLabel("Control Center"); title.setStyleSheet("font-size:24px;font-weight:700;"); root.addWidget(title)
        grid=QGridLayout()
        self.buttons={}
        for i,(key,label) in enumerate([("wifi","Wi-Fi"),("airplane_mode","Airplane"),("dark_mode","Dark Mode")]):
            b=QPushButton(); b.setCheckable(True); b.setText(label); b.setChecked(getattr(state,key))
            b.clicked.connect(lambda checked,k=key:self.toggle(k,checked)); grid.addWidget(b,i//2,i%2); self.buttons[key]=b
        root.addLayout(grid)
        root.addWidget(QLabel("Brightness"))
        bright=QSlider(); bright.setOrientation(1); bright.setRange(10,100); bright.setValue(state.brightness); root.addWidget(bright)
        root.addWidget(QLabel("Volume"))
        vol=QSlider(); vol.setOrientation(1); vol.setRange(0,100); vol.setValue(state.volume); root.addWidget(vol)
        close=QPushButton("Done"); close.clicked.connect(self.closed.emit); root.addWidget(close)
        self.setStyleSheet("background:rgba(20,24,35,.97);color:white;border-radius:28px;padding:12px;QPushButton{background:#2c3240;color:white;border-radius:16px;padding:12px;}")

    def toggle(self,key,value):
        setattr(self.state,key,value); self.changed.emit(key,value)
