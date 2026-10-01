from PySide6.QtCore import QEasingCurve,QPropertyAnimation
def fade_in(widget,duration=180):
    anim=QPropertyAnimation(widget,b"windowOpacity",widget)
    anim.setDuration(duration); anim.setStartValue(0.0); anim.setEndValue(1.0)
    anim.setEasingCurve(QEasingCurve.OutCubic); widget.setWindowOpacity(0.0); widget.show(); anim.start(QPropertyAnimation.DeleteWhenStopped)
    return anim
