from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton
class NotificationCenter(QWidget):
    closed=Signal()
    def __init__(self,parent=None):
        super().__init__(parent); l=QVBoxLayout(self)
        h=QLabel("Notifications"); h.setStyleSheet("font-size:24px;font-weight:700;"); l.addWidget(h)
        l.addWidget(QLabel("No new notifications\n\nYour simulated system is up to date."))
        l.addStretch(); b=QPushButton("Done"); b.clicked.connect(self.closed.emit); l.addWidget(b)
        self.setStyleSheet("background:rgba(20,24,35,.97);color:white;border-radius:28px;padding:18px;")
