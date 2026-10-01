from PySide6.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton,QTextBrowser
class BrowserApp(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent); root=QVBoxLayout(self)
        self.url=QLineEdit("https://example.com"); root.addWidget(self.url)
        b=QPushButton("Go"); root.addWidget(b)
        view=QTextBrowser(); view.setHtml("<h2>Mini Browser</h2><p>Simulated browser screen. Internet navigation is disabled in this demo.</p>"); root.addWidget(view)
