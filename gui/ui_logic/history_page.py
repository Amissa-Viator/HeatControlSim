from PySide6.QtWidgets import QWidget
from core.directors.history_director import search_all_solved_problems
from gui.ui.ui_history_page import Ui_Form
from gui.ui_logic.empty_history import EmptyHistory
from gui.ui_logic.history_blocks import HistoryBlocks


class HistoryPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.content_layout = self.ui.verticalLayout

        self.main_window = main_window
        self.problems = None

        self.refresh()

    def refresh(self):
        self.problems, overviews = search_all_solved_problems()
        self.update_view(overviews)

    def update_view(self, overviews):
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not self.problems:
            self.content_layout.addWidget(EmptyHistory())
        else:
            self.content_layout.addWidget(HistoryBlocks(self.problems, overviews, self.main_window))


