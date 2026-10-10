import os
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QSizePolicy, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, \
    QHeaderView, QHBoxLayout
from core.directors.db_director import save_to_database, delete_record_from_database
from gui.ui.ui_result_page import Ui_Form
from gui.ui_logic.message_box import CustomMessageBox


class ResultPage(QWidget):
    def __init__(self, result_info, input_info, excel_path, plot_paths, source, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.result_info = result_info
        self.input_info = input_info
        self.excel_path = excel_path
        self.plot_paths = plot_paths

        self.layout = self.ui.mainVerticalLayout

        self.set_problem_text()
        self.fill_input_data()
        self.set_label_for_results("Calculation results")
        self.fill_result_data()
        self.put_excel_path()
        self.set_label_for_results("Graphical plots")
        self.put_plots()

        self.buttonPlaceholder = QWidget()
        self.buttonLayout = QVBoxLayout(self.buttonPlaceholder)
        self.buttonLayout.setContentsMargins(0, 60, 0, 25)
        self.ui.mainVerticalLayout.addWidget(self.buttonPlaceholder)

        if source == "add":
            self.save_button = QPushButton("Save")
            self.set_save_button(self.save_button)
            self.save_button.clicked.connect(self.export_all_data)
        else:
            self.delete_button = QPushButton("Delete")
            self.set_delete_button(self.delete_button)
            self.delete_button.clicked.connect(self.delete_all_data)

    def set_problem_text(self):
        view = QWebEngineView()
        html_path = os.path.abspath("gui/design/html/problem.html")

        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        view.setHtml(html_content)

        view.setMinimumHeight(800)
        view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ui.mainVerticalLayout.addWidget(view)

    def fill_input_data(self):
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(len(self.input_info))
        table.setHorizontalHeaderLabels(["Parameter", "Value"])

        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)

        table.setStyleSheet("""
            QTableWidget {
                font-size: 15px;
                font-weight: 300;
            }
            QTableWidget::item {
                padding: 4px;
                border: 1px solid rgb(0, 0, 0);
            }
            QHeaderView::section {
                font-size: 15px;
                background-color: white;
                padding: 4px;
                font-weight: 400;
                text-align: center;
                border: 1px solid rgb(0,0,0);
            }
        """)
        table.setFrameStyle(QTableWidget.Box | QTableWidget.Plain)
        table.setLineWidth(1)

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        for row, (key, value) in enumerate(self.input_info.items()):
            key_item = QTableWidgetItem(str(key))
            value_item = QTableWidgetItem(str(value))
            key_item.setFlags(key_item.flags() ^ Qt.ItemIsEditable)
            value_item.setFlags(value_item.flags() ^ Qt.ItemIsEditable)
            table.setItem(row, 0, key_item)
            table.setItem(row, 1, value_item)

        table.resizeRowsToContents()
        table.resizeColumnsToContents()

        total_height = table.horizontalHeader().height()
        for r in range(table.rowCount()):
            total_height += table.rowHeight(r)
        table.setFixedHeight(total_height)

        self.ui.mainVerticalLayout.addWidget(table)

    def set_label_for_results(self, text):
        label = QLabel(text)
        label.setAlignment(Qt.AlignHCenter)
        label.setContentsMargins(0, 40, 0, 20)

        label.setStyleSheet("""
            QLabel {
                font-family: "Gill Sans", sans-serif;
                color: rgb(10, 26, 86);
                font-size: 20px;
                font-weight: 600;
            }
        """)

        self.ui.mainVerticalLayout.addWidget(label)

    def fill_result_data(self):
        table = QTableWidget()
        table.setColumnCount(len(self.result_info[0]))
        table.setRowCount(len(self.result_info))

        table.setHorizontalHeaderLabels(list(self.result_info[0].keys()))
        table.verticalHeader().setVisible(False)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)

        table.setStyleSheet("""
            QTableWidget {
                font-size: 15px;
                font-weight: 300;
            }
            QTableWidget::item {
                padding: 4px;
                border: 1px solid rgb(0, 0, 0);
            }
            QHeaderView::section {
                font-size: 15px;
                background-color: white;
                padding: 4px;
                font-weight: 400;
                text-align: center;
                border: 1px solid rgb(0,0,0);
            }
        """)
        table.setFrameStyle(QTableWidget.Box | QTableWidget.Plain)
        table.setLineWidth(1)

        table.setWordWrap(True)
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)

        for col in range(table.columnCount()):
            table.setColumnWidth(col, 200)

        for row, result in enumerate(self.result_info):
            for col, key in enumerate(result.keys()):
                item = QTableWidgetItem(str(result[key]))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                table.setItem(row, col, item)

        table.resizeRowsToContents()
        table.resizeColumnsToContents()

        table_height = table.horizontalHeader().height()
        for row in range(table.rowCount()):
            table_height += table.rowHeight(row)
        table.setMinimumHeight(table_height)

        container = QWidget()
        h_layout = QHBoxLayout(container)
        h_layout.addWidget(table, alignment=Qt.AlignHCenter)
        h_layout.setContentsMargins(0, 0, 0, 0)

        self.ui.mainVerticalLayout.addWidget(container)

    def put_excel_path(self):
        label = QLabel(f"More detailed data can be found at: {self.excel_path}")
        label.setContentsMargins(20, 40, 0, 50)

        label.setStyleSheet("""
                    QLabel {
                        font-family: "Gill Sans", sans-serif;
                        color: rgb(0, 0, 0);
                        font-size: 16px;
                    }
                """)

        self.ui.mainVerticalLayout.addWidget(label)

    def set_save_button(self, button):
        button.setFixedSize(QSize(161, 35))
        button.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                font-family: "Gill Sans", sans-serif;
                border-radius: 10px;
                text-align: center;
                color: rgb(255, 255, 255);
                border: 2px solid rgb(0, 0, 205);
                background-color: rgb(65, 105, 255);
            }
        
            QPushButton:hover {
                color: rgb(255, 255, 255);
                background-color: rgb(48, 91, 219);
                border: 2px solid rgb(0, 0, 205);
            }
        """)

        self.buttonLayout.addWidget(button, alignment=Qt.AlignHCenter)

    def set_delete_button(self, button):
        button.setFixedSize(QSize(161, 35))
        button.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                font-family: "Gill Sans", sans-serif;
                border-radius: 10px;
                text-align: center;
                color: rgb(178, 34, 34);
                border: 2px solid rgb(139, 0, 0);
                background-color: rgb(255, 255, 255);
            }

            QPushButton:hover {
                color: rgb(255, 255, 255);
                background-color: rgb(220, 20, 60);
                border: 2px solid rgb(139, 0, 0);
            }
        """)

        self.buttonLayout.addWidget(button, alignment=Qt.AlignHCenter)

    def put_plots(self):
        for key, path in self.plot_paths.items():
            if not os.path.exists(path):
                continue

            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(800, 400, Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)

            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)
            container_layout.setContentsMargins(0, 20, 0, 20)
            self.ui.mainVerticalLayout.addWidget(container)

    def export_all_data(self):
        is_saved = save_to_database(self.result_info, self.input_info, self.excel_path, self.plot_paths)
        if is_saved:
            msg = CustomMessageBox(title="Success", message="The task has been saved successfully", status="success")
            msg.exec()

            self.main_window.history_page.refresh()
        else:
            msg = CustomMessageBox(title="Error", message="Failed to save the data", status="error")
            msg.exec()

    def delete_all_data(self):
        is_deleted = delete_record_from_database(self.result_info, self.input_info, self.excel_path, self.plot_paths)
        if is_deleted:
            msg = CustomMessageBox(title="Success", message="The task has been deleted successfully", status="success")
            msg.exec()
            self.main_window.history_page.refresh()
        else:
            msg = CustomMessageBox(title="Error", message="Failed to delete the data", status="error")
            msg.exec()


