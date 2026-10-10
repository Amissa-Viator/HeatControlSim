from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QUrl
from gui.ui.ui_home_page import Ui_Form
import os


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        html_path = os.path.abspath("gui/design/html/home_info.html")
        self.ui.info_text.setUrl(QUrl.fromLocalFile(html_path))
