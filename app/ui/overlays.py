from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton
class OverlayPanel(QWidget):
    def __init__(self,title,body,parent=None):
        super().__init__(parent); layout=QVBoxLayout(self)
        h=QLabel(title); h.setStyleSheet("font-size:24px;font-weight:700;"); layout.addWidget(h)
        layout.addWidget(QLabel(body)); layout.addStretch()
        b=QPushButton("Close"); b.clicked.connect(self.close); layout.addWidget(b)
        self.setStyleSheet("background:#111722;color:white;border-radius:22px;padding:10px;")
