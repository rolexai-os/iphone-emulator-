from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel
class AppSwitcher(QWidget):
    app_selected=Signal(str); closed=Signal()
    def __init__(self,recent,parent=None):
        super().__init__(parent); l=QVBoxLayout(self)
        h=QLabel("App Switcher"); h.setStyleSheet("font-size:24px;font-weight:700;"); l.addWidget(h)
        if recent:
            for name in recent:
                b=QPushButton(name); b.clicked.connect(lambda _,n=name:self.app_selected.emit(n)); l.addWidget(b)
        else: l.addWidget(QLabel("No recent apps"))
        l.addStretch(); b=QPushButton("Close"); b.clicked.connect(self.closed.emit); l.addWidget(b)
        self.setStyleSheet("background:rgba(14,17,25,.98);color:white;border-radius:28px;padding:18px;")
