from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout

class HomeScreen(QWidget):
    app_requested = Signal(str)
    control_center_requested = Signal()
    notification_center_requested = Signal()

    def __init__(self, apps, parent=None):
        super().__init__(parent)
        root = QVBoxLayout(self)
        root.setContentsMargins(14, 38, 14, 16)
        top = QPushButton("◀ Notifications          Control Center ▶")
        top.clicked.connect(self.control_center_requested.emit)
        root.addWidget(top)
        root.addStretch()
        grid = QGridLayout()
        grid.setSpacing(10)
        for i, app in enumerate(apps):
            button = QPushButton(f"{app['icon']}\n{app['name']}")
            button.setMinimumSize(74, 74)
            button.clicked.connect(lambda checked=False, n=app["name"]: self.app_requested.emit(n))
            grid.addWidget(button, i // 4, i % 4)
        root.addLayout(grid)
        root.addStretch()
        dock = QLabel("  ☎ Phone     🌐 Browser     💬 Messages     🎵 Music  ")
        dock.setAlignment(Qt.AlignCenter)
        dock.setStyleSheet("background:rgba(255,255,255,.18);border-radius:20px;padding:10px;color:white;")
        root.addWidget(dock)
        self.setStyleSheet("""
        QWidget {color:white;}
        QPushButton {color:white;background:rgba(255,255,255,.17);border:0;border-radius:18px;padding:7px;}
        QPushButton:hover {background:rgba(255,255,255,.28);}
        """)
        self.setStyleSheet(self.styleSheet()+" QWidget#HomeScreen{background:#1a263d;}")

    def paintEvent(self, event):
        from PySide6.QtGui import QPainter, QLinearGradient
        p=QPainter(self); g=QLinearGradient(0,0,self.width(),self.height())
        g.setColorAt(0,"#18243a"); g.setColorAt(.5,"#6c3f74"); g.setColorAt(1,"#d06b4e")
        p.fillRect(self.rect(),g)
