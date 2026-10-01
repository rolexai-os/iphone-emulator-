from PySide6.QtCore import QObject, QPoint, Signal

class GestureTracker(QObject):
    tapped = Signal(QPoint)
    swipe_up = Signal()
    swipe_down = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.start = None

    def press(self, pos):
        self.start = pos

    def release(self, pos):
        if self.start is None:
            return
        dy = pos.y() - self.start.y()
        if abs(dy) > 60:
            (self.swipe_down if dy > 0 else self.swipe_up).emit()
        else:
            self.tapped.emit(pos)
        self.start = None
