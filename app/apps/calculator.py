from PySide6.QtWidgets import QWidget,QGridLayout,QLineEdit,QPushButton,QVBoxLayout
from PySide6.QtCore import Qt
class CalculatorApp(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent); self.expr=""
        root=QVBoxLayout(self); self.display=QLineEdit(); self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight); self.display.setStyleSheet("font-size:28px;padding:10px;")
        root.addWidget(self.display)
        grid=QGridLayout(); keys=["7","8","9","÷","4","5","6","×","1","2","3","-","0",".","C","+","="]
        for i,k in enumerate(keys):
            b=QPushButton(k); b.setMinimumHeight(46); b.clicked.connect(lambda _,x=k:self.press(x)); grid.addWidget(b,i//4,i%4)
        root.addLayout(grid)
    def press(self,k):
        if k=="C": self.expr=""
        elif k=="=":
            try: self.expr=str(eval(self.expr.replace("×","*").replace("÷","/"),{"__builtins__":{}},{}))
            except Exception: self.expr="Error"
        else: self.expr+=k
        self.display.setText(self.expr)
