from PySide6.QtGui import QPixmap, Qt, QIcon
from PySide6.QtWidgets import QDialog, QPushButton
from gui.ui.ui_message_box import Ui_Dialog


class CustomMessageBox(QDialog):
    def __init__(self, title="", message="", status="info"):
        super().__init__()
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._is_dragging = False
        self._drag_position = None

        close_button = QPushButton(self)
        close_button.setIcon(QIcon("gui/design/icons/close.png"))
        close_button.setGeometry(320, 0, 35, 35)
        close_button.setFlat(True)

        self.ui.title_label.setText(title)

        self.ui.message_label.setAlignment(Qt.AlignCenter)
        self.ui.message_label.setText(message)

        if status == "info":
            self.ui.bottom_frame.setStyleSheet("background-color: rgb(226, 118, 2);")
            self.set_icon("gui/design/icons/info.png")

        elif status == "success":
            self.ui.bottom_frame.setStyleSheet("background-color: rgb(32, 186, 32);")
            self.set_icon("gui/design/icons/check.png")

        elif status == "error":
            self.ui.bottom_frame.setStyleSheet("background-color: rgb(220, 20, 60);")
            self.set_icon("gui/design/icons/cross.png")

        close_button.clicked.connect(self.close)

    def set_icon(self, path):
        pix = QPixmap(path).scaled(90, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.icon_label.setPixmap(pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._is_dragging = False
