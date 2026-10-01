from PySide6.QtCore import Qt, QDateTime, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class LockScreen(QWidget):
    unlock_requested = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 70, 24, 24)
        date = QLabel()
        date.setAlignment(Qt.AlignCenter)
        date.setText(QDateTime.currentDateTime().toString("dddd, MMMM d"))
        layout.addWidget(date)
        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setStyleSheet("font-size:58px;font-weight:200;")
        layout.addWidget(self.clock)
        layout.addStretch()
        button = QPushButton("Tap to Unlock")
        button.clicked.connect(self.unlock_requested.emit)
        layout.addWidget(button)
        self.setStyleSheet("background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #07131e,stop:1 #315a72);color:white;")
        self.timer = self.startTimer(1000)
        self.update_clock()

    def timerEvent(self, event):
        self.update_clock()

    def update_clock(self):
        self.clock.setText(QDateTime.currentDateTime().toString("HH:mm"))
