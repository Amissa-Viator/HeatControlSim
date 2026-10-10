from PySide6.QtWidgets import QWidget
from core.directors.history_director import get_result_for_problem
from gui.ui.ui_history_block import Ui_Form
from gui.ui_logic.problem_card import ProblemCard


class HistoryBlocks(QWidget):
    def __init__(self, problems, overviews, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.problems = problems
        self.overviews = overviews
        self.main_window = main_window

        for i, problem in enumerate(problems):
            card = ProblemCard(problem)
            card.index = i
            card.clicked.connect(self.card_clicked)
            self.ui.verticalLayout.addWidget(card)

        self.ui.verticalLayout.addStretch()

    def card_clicked(self):
        card = self.sender()
        index = card.index

        problem = self.problems[index]
        overview = self.overviews[index]

        results, input_info, excel_path, plot_paths = get_result_for_problem(problem, overview)
        self.main_window.open_results_page(results, input_info, excel_path, plot_paths, source="history")
