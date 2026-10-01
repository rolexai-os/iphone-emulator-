from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton
class PhoneApp(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent); root=QVBoxLayout(self); root.addWidget(QLabel("Phone"))
        self.number=QLineEdit(); self.number.setPlaceholderText("Phone number"); root.addWidget(self.number)
        b=QPushButton("Call"); b.clicked.connect(lambda:self.status.setText("Demo call — no real call placed")); root.addWidget(b)
        self.status=QLabel("Ready"); root.addWidget(self.status); root.addStretch()
