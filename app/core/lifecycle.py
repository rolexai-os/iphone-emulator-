from enum import Enum
from PySide6.QtCore import QObject, Signal

class AppState(str, Enum):
    INACTIVE="inactive"; ACTIVE="active"; BACKGROUND="background"; TERMINATED="terminated"

class AppLifecycle(QObject):
    state_changed=Signal(str,str)
    def __init__(self,name,parent=None):
        super().__init__(parent); self.name=name; self.state=AppState.TERMINATED
    def transition(self,state):
        old=self.state; self.state=state; self.state_changed.emit(old.value,state.value)
