from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from gui.ui.ui_empty_history import Ui_Form


class EmptyHistory(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setOffset(1, 1)

        self.ui.empty_label.setGraphicsEffect(self.shadow)
