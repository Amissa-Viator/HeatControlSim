from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Signal, Qt


class ProblemCard(QFrame):
    clicked = Signal(int)

    def __init__(self, problem_data):
        super().__init__()
        self.problem_data = problem_data
        self.index = None

        self.setObjectName("ProblemCard")
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(250)

        self.setStyleSheet("""
            QFrame#ProblemCard {
                border: 1px solid rgb(192,192,192);
                border-radius: 10px;
                background: #fafafa;
                padding: 8px;
            }
            QFrame#ProblemCard:hover {
                border: 2px solid rgb(123,104,238);
                background: white;
                margin-top: -4px;
                margin-bottom: 4px;
            }
            QLabel {
                font-weight: 500;
                font-size: 16px;
                color: rgb(2, 7, 28);
            }
        """)

        main = QVBoxLayout(self)
        main.setContentsMargins(8, 8, 8, 8)
        main.setSpacing(6)

        problem_name = self.problem_data.get("Problem", "").lower()
        method = self.problem_data.get("Method", "").lower()

        self.task_label = QLabel(f"Problem: {problem_name}")
        self.task_label.setStyleSheet("font-weight:600; font-size:15px;")
        main.addWidget(self.task_label)

        self.method_label = QLabel(f"Approach: {method}")
        self.method_label.setStyleSheet("font-weight:600; font-size:15px;")
        main.addWidget(self.method_label)

        line_container = QVBoxLayout()
        line_container.setContentsMargins(10, 2, 10, 2)
        line_container.setSpacing(0)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)

        line_container.addWidget(line)
        main.addLayout(line_container)

        cols = QHBoxLayout()
        cols.setSpacing(20)
        main.addLayout(cols)

        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
        self.col3 = QVBoxLayout()

        cols.addLayout(self.col1)
        cols.addLayout(self.col2)
        cols.addLayout(self.col3)

        self.fill_columns()

    def fill_columns(self):
        col1_keys = ["f(x)", "k(x)", "φ(x)", "v⁽⁰⁾"]
        col2_keys = ["ε", "α", "u(0)", "u(l)"]

        col3_keys = [
            k for k in self.problem_data.keys()
            if k not in ["Problem", "Approach"] + col1_keys + col2_keys
        ]

        self.put_into(self.col1, col1_keys)
        self.put_into(self.col2, col2_keys)
        self.put_into(self.col3, col3_keys)

    def put_into(self, layout, keys):
        for k in keys:
            if k in self.problem_data:
                lbl = QLabel(f"{k}: {self.problem_data[k]}")
                lbl.setWordWrap(True)
                layout.addWidget(lbl)
        layout.addStretch()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.index)

