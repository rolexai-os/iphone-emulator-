from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget
class MessagesApp(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent); root=QVBoxLayout(self); root.addWidget(QLabel("Messages"))
        self.list=QListWidget(); self.list.addItem("Demo conversation"); root.addWidget(self.list)
        self.input=QLineEdit(); self.input.setPlaceholderText("Message"); root.addWidget(self.input)
        b=QPushButton("Send"); b.clicked.connect(self.send); root.addWidget(b)
    def send(self):
        text=self.input.text().strip()
        if text: self.list.addItem("You: "+text); self.input.clear()
