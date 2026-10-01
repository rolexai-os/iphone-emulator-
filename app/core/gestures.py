from PySide6.QtCore import QObject, Signal
class GestureController(QObject):
    tap=Signal(object); swipe_left=Signal(); swipe_right=Signal(); swipe_up=Signal(); swipe_down=Signal()
    def __init__(self,parent=None): super().__init__(parent); self.start=None
    def press(self,pos): self.start=pos
    def release(self,pos):
        if self.start is None: return
        dx,dy=pos.x()-self.start.x(),pos.y()-self.start.y()
        if max(abs(dx),abs(dy))<45: self.tap.emit(pos)
        elif abs(dx)>abs(dy): (self.swipe_right if dx>0 else self.swipe_left).emit()
        else: (self.swipe_down if dy>0 else self.swipe_up).emit()
        self.start=None
