from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QRect
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout

class DynamicIsland(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("island")
        self.label=QLabel("●  Ready")
        self.label.setStyleSheet("color:white;font-size:10px;font-weight:600;")
        l=QHBoxLayout(self); l.setContentsMargins(12,4,12,4); l.addWidget(self.label)
        self.setStyleSheet("#island{background:#000;border-radius:18px;}")
        self.setFixedHeight(34)

    def set_activity(self,text):
        self.label.setText(text)
        self.animate_expand()

    def animate_expand(self):
        start=self.width() or 150
        anim=QPropertyAnimation(self,b"minimumWidth",self)
        anim.setDuration(220); anim.setStartValue(max(120,start)); anim.setEndValue(230)
        anim.setEasingCurve(QEasingCurve.OutCubic); anim.start(QPropertyAnimation.DeleteWhenStopped)
