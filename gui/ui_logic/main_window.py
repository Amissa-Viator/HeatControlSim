from PySide6.QtWidgets import QMainWindow
from gui.ui.ui_mainwindow import Ui_MainWindow
from gui.ui_logic.add_problem_page import AddProblemPage
from gui.ui_logic.history_page import HistoryPage
from gui.ui_logic.home_page import HomePage
from gui.ui_logic.result_page import ResultPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Heat Simulator")

        self.setFixedSize(self.width(), self.height())

        self.home_page = HomePage()
        self.ui.page_stackedWidget.addWidget(self.home_page)

        self.history_page = HistoryPage(self)
        self.ui.page_stackedWidget.addWidget(self.history_page)

        self.add_page = AddProblemPage(self)
        self.ui.page_stackedWidget.addWidget(self.add_page)
        self.result_page = None

        self.ui.home_button.clicked.connect(self.switch_to_home_page)
        self.ui.add_problem_button.clicked.connect(self.switch_to_add_page)
        self.ui.history_button.clicked.connect(self.switch_to_history_page)

    def switch_to_home_page(self):
        self.ui.page_stackedWidget.setCurrentWidget(self.home_page)

    def switch_to_add_page(self):
        self.add_page.clear_all_fields()
        self.ui.page_stackedWidget.setCurrentWidget(self.add_page)

    def switch_to_history_page(self):
        self.ui.page_stackedWidget.setCurrentWidget(self.history_page)

    def open_results_page(self, results, input_info, excel_path, plot_paths, source):
        self.result_page = ResultPage(results, input_info, excel_path, plot_paths, source, self)
        self.ui.page_stackedWidget.addWidget(self.result_page)
        self.ui.page_stackedWidget.setCurrentWidget(self.result_page)


