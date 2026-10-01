from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel
from PySide6.QtCore import Qt
class PhotosApp(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent); root=QVBoxLayout(self); h=QLabel("Photos"); h.setStyleSheet("font-size:28px;font-weight:700;"); root.addWidget(h)
        root.addWidget(QLabel("🌄\n\nSimulated photo library\nNo real device photos are accessed."),alignment=Qt.AlignCenter); root.addStretch()
