import os
import sympy as sp
import math
from PySide6.QtWidgets import QWidget
from core.data_worker.data import BoundaryConditions, Data
from core.data_worker.problems_solutions import ProblemType, SolutionMethod
from core.directors.calculation_director import run_calculation
from core.directors.checker_director import compare_task_with_db_records
from gui.ui.ui_add_problem_page import Ui_Form
from gui.ui_logic.message_box import CustomMessageBox


def get_method_to_calculate(method_text: str, problem_choice: ProblemType) -> SolutionMethod:
    if problem_choice == ProblemType.WITHOUT_CONSTRAINT:
        if method_text == "Gradient Method":
            return SolutionMethod.GRADIENT_METHOD
        elif method_text == "Modified Gradient Method":
            return SolutionMethod.MODIFIED_METHOD
        else:
            return SolutionMethod.COMPARE_MODIFIED_TO_GRADIENT

    else:
        if method_text == "Conditional Gradient Method":
            return SolutionMethod.CONDITIONAL_GRADIENT_METHOD
        elif method_text == "Modified Conditional Gradient Method":
            return SolutionMethod.MODIFIED_METHOD
        else:
            return SolutionMethod.COMPARE_MODIFIED_TO_GRADIENT


def get_function(line_edit, with_derivative=False):
    expr_str = line_edit.text().strip()
    x = sp.Symbol('x')

    allowed = {
        "x": x,
        **{k: getattr(math, k) for k in dir(math) if not k.startswith("__")},
        **{k: getattr(sp, k) for k in dir(sp) if isinstance(getattr(sp, k), sp.FunctionClass)}
    }

    try:
        expr = sp.sympify(expr_str, locals=allowed)

        free_symbols = expr.free_symbols
        if free_symbols - {x}:
            raise ValueError("Unknown values in the expression")

        f = sp.lambdify(x, expr, modules=["math", "sympy"])
        fprime = None

        if with_derivative:
            fprime = sp.lambdify(x, sp.diff(expr, x), modules=["math", "sympy"])

        line_edit.setStyleSheet("")
        return f, fprime, expr

    except Exception as e:
        line_edit.setStyleSheet("border: 2px solid red;")
        return None, None, None


def read_numeric_value(line_edit, allow_zero=True, positive_only=True, num_type=float):
    text = line_edit.text().strip()

    try:
        value = num_type(text)
        if positive_only and value < 0:
            raise ValueError("Value must be positive")
        if not allow_zero and value == 0:
            raise ValueError("Value can't be equal zero")
        line_edit.setStyleSheet("")
        return value

    except Exception as e:
        line_edit.setStyleSheet("border: 2px solid red;")
        return None


def read_even_int(line_edit):
    value = read_numeric_value(line_edit, allow_zero=False, positive_only=True)
    if value is None:
        return None

    value = int(value)
    if value % 2 != 0:
        line_edit.setStyleSheet("border: 2px solid red;")
        return None
    return value


def validate_fields(fields: dict) -> bool:
    valid = True
    for line_edit, name in fields.items():
        if line_edit is None or line_edit.text().strip() == "" or line_edit.text() == "None":
            line_edit.setStyleSheet("border: 2px solid red;")
            valid = False
        else:
            line_edit.setStyleSheet("")
    if not valid:
        msg = CustomMessageBox(title="Error",
                               message="Please fill in all required fields",
                               status="error")
        msg.exec()
    return valid


def check_values(*checks):
    for value, message in checks:
        if value is None:
            msg = CustomMessageBox(title="Error", message=message, status="error")
            msg.exec()
            return False
    return True


def check_nmin_and_nmax(n_min, n_max, min_lineEdit, max_lineEdit):
    if n_min is None or n_max is None:
        return False

    if n_min >= n_max:
        msg = CustomMessageBox(title="Error",
                               message="The value of N₁ must be less than Nₘₐₓ",
                               status="error")
        msg.exec()
        min_lineEdit.setStyleSheet("border: 2px solid red;")
        max_lineEdit.setStyleSheet("border: 2px solid red;")
        return False

    return True


class AddProblemPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.methods_for_tasks = {
            "without": [
                "Gradient Method",
                "Modified Gradient Method",
                "Comparison of Gradient Method\nand Modified Gradient Method"
            ],
            "with": [
                "Conditional Gradient Method",
                "Modified Conditional Gradient Method",
                "Comparison of Conditional Gradient Method\nand Modified Conditional Gradient Method"
            ]
        }

        html_path = os.path.abspath("gui/design/html/problem.html")
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        self.ui.info_content.setHtml(html_content)

        self.ui.without_constraints_RB.toggled.connect(self.on_problem_type_changed)
        self.ui.with_constraints_RB.toggled.connect(self.on_problem_type_changed)
        self.ui.method_comboBox.currentTextChanged.connect(self.update_additional_fields)
        self.ui.solve_button.clicked.connect(self.collect_all_data)

        self.on_problem_type_changed()

    def on_problem_type_changed(self):
        self.ui.method_comboBox.clear()

        if self.ui.without_constraints_RB.isChecked():
            methods = self.methods_for_tasks["without"]
        else:
            methods = self.methods_for_tasks["with"]

        self.ui.method_comboBox.addItems(methods)
        self.update_additional_fields()

    def update_additional_fields(self):
        method = self.ui.method_comboBox.currentText().replace("\n", " ")

        if method == "":
            self.ui.additional_stackedWidget.setCurrentWidget(self.ui.empty_page)
            return

        if self.ui.without_constraints_RB.isChecked():
            if method == "Gradient Method":
                self.ui.additional_stackedWidget.setCurrentWidget(self.ui.page_1)
            elif method in ["Modified Gradient Method",
                            "Comparison of Gradient Method and Modified Gradient Method"]:
                self.ui.additional_stackedWidget.setCurrentWidget(self.ui.page_3)
        elif self.ui.with_constraints_RB.isChecked():
            if method == "Conditional Gradient Method":
                self.ui.additional_stackedWidget.setCurrentWidget(self.ui.page_2)
            elif method in ["Modified Conditional Gradient Method",
                            "Comparison of Conditional Gradient Method and Modified Conditional Gradient Method"]:
                self.ui.additional_stackedWidget.setCurrentWidget(self.ui.page_4)

    def collect_all_data(self):
        method_text = self.ui.method_comboBox.currentText().replace("\n", " ")

        problem_choice = ProblemType.WITHOUT_CONSTRAINT if self.ui.without_constraints_RB.isChecked() else ProblemType.WITH_CONSTRAINT

        if method_text == "":
            msg = CustomMessageBox(title="Error",
                                   message="Please select a method",
                                   status="error")
            msg.exec()
            return
        method_choice = get_method_to_calculate(method_text, problem_choice)

        required_fields = self.get_required_fields()
        if not validate_fields(required_fields):
            return

        epsilon = read_numeric_value(self.ui.eps_lineEdit, allow_zero=False, positive_only=True)
        alpha = read_numeric_value(self.ui.alpha_lineEdit, allow_zero=False, positive_only=True)
        v_initial = read_numeric_value(self.ui.v_lineEdit, allow_zero=True, positive_only=True)
        u0 = read_numeric_value(self.ui.u0_lineEdit)
        ul = read_numeric_value(self.ui.ul_lineEdit)

        u_bc = BoundaryConditions(
            ALPHA_0=1, ALPHA_1=0,
            BETA_0=1, BETA_1=0,
            A=u0, B=ul
        )

        if None in (epsilon, alpha, v_initial, u0, ul):
            msg = CustomMessageBox(title="Error",
                                   message="Invalid numeric values entered",
                                   status="error")
            msg.exec()
            return

        f, _, f_expr = get_function(self.ui.f_lineEdit)
        k, k_der, k_expr = get_function(self.ui.k_lineEdit, with_derivative=True)
        phi, _, phi_expr = get_function(self.ui.phi_lineEdit)

        if None in (f, k, phi):
            msg = CustomMessageBox(title="Error",
                                   message="Errors in the entered functions",
                                   status="error")
            msg.exec()
            return

        n_min = n_max = v_max = None
        current_widget = self.ui.additional_stackedWidget.currentWidget()

        checks = []

        if current_widget == self.ui.page_1:
            n_max = read_even_int(self.ui.n_lineEdit)
            checks.append((n_max, "Invalid numeric value entered!\nThe value must be even"))

        elif current_widget == self.ui.page_2:
            v_max = read_numeric_value(self.ui.vmax_lineEdit_2, allow_zero=False, positive_only=True)
            n_max = read_even_int(self.ui.n_lineEdit_2)

            checks.append((v_max, "Invalid numeric value entered!"))
            checks.append((n_max, "Invalid numeric value entered!\nThe value must be even"))

        elif current_widget == self.ui.page_3:
            n_min = read_even_int(self.ui.n_1_lineEdit)
            n_max = read_even_int(self.ui.n_max_lineEdit)

            checks.append((n_min, "Invalid numeric value entered!\nThe value must be even"))
            checks.append((n_max, "Invalid numeric value entered!\nThe value must be even"))

        elif current_widget == self.ui.page_4:
            n_min = read_even_int(self.ui.n1_lineEdit)
            n_max = read_even_int(self.ui.nmax_lineEdit)
            v_max = read_numeric_value(self.ui.vmax_lineEdit, allow_zero=False, positive_only=True)

            checks.append((n_min, "Invalid numeric value entered!\nThe value must be even"))
            checks.append((n_max, "Invalid numeric value entered!\nThe value must be even"))
            checks.append((v_max, "Invalid numeric value entered!"))

        if not check_values(*checks):
            return

        if current_widget in (self.ui.page_3, self.ui.page_4):
            if not check_nmin_and_nmax(n_min, n_max,
                                     self.ui.n_1_lineEdit if current_widget == self.ui.page_3 else self.ui.n1_lineEdit,
                                     self.ui.n_max_lineEdit if current_widget == self.ui.page_3 else self.ui.nmax_lineEdit):
                return

        data = Data(
            n_max=n_max,
            n_min=n_min,
            epsilon=epsilon,
            alpha=alpha,
            v_max=v_max,
            u_boundary=u_bc,
            f=f,
            k=k,
            k_derivative=k_der,
            phi=phi,
            f_expr=f_expr,
            k_expr=k_expr,
            phi_expr=phi_expr
        )

        is_unique = compare_task_with_db_records(data, problem_choice, method_choice, v_initial)
        if is_unique:
            results, input_info, excel_path, plot_paths = run_calculation(data, problem_choice, method_choice,
                                                                          v_initial)
            self.main_window.open_results_page(results, input_info, excel_path, plot_paths, source="add")
        else:
            msg = CustomMessageBox(title="Note",
                                   message="This task has already been solved. \nPlease check the 'History' tab")
            msg.exec()
            return

    def get_required_fields(self) -> dict:
        fields = {
            self.ui.f_lineEdit: "f(x)",
            self.ui.k_lineEdit: "k(x)",
            self.ui.phi_lineEdit: "phi(x)",
            self.ui.eps_lineEdit: "epsilon",
            self.ui.alpha_lineEdit: "alpha",
            self.ui.v_lineEdit: "v_initial",
            self.ui.u0_lineEdit: "u0",
            self.ui.ul_lineEdit: "ul"
        }

        current = self.ui.additional_stackedWidget.currentWidget()

        if current == self.ui.page_1:
            fields[self.ui.n_lineEdit] = "n_max"

        elif current == self.ui.page_2:
            fields[self.ui.vmax_lineEdit_2] = "v_max"
            fields[self.ui.n_lineEdit_2] = "n_max"

        elif current == self.ui.page_3:
            fields[self.ui.n_1_lineEdit] = "n_min"
            fields[self.ui.n_max_lineEdit] = "n_max"

        elif current == self.ui.page_4:
            fields[self.ui.n1_lineEdit] = "n_min"
            fields[self.ui.nmax_lineEdit] = "n_max"
            fields[self.ui.vmax_lineEdit] = "v_max"

        return fields

    def clear_all_fields(self):
        for line_edit in [
            self.ui.f_lineEdit, self.ui.k_lineEdit, self.ui.phi_lineEdit,
            self.ui.eps_lineEdit, self.ui.alpha_lineEdit, self.ui.v_lineEdit,
            self.ui.u0_lineEdit, self.ui.ul_lineEdit,
            self.ui.n_lineEdit, self.ui.n_1_lineEdit, self.ui.n_max_lineEdit,
            self.ui.n_lineEdit_2, self.ui.n1_lineEdit, self.ui.nmax_lineEdit,
            self.ui.vmax_lineEdit, self.ui.vmax_lineEdit_2
        ]:
            line_edit.clear()
            line_edit.setStyleSheet("")

        for rb in [self.ui.without_constraints_RB, self.ui.with_constraints_RB]:
            rb.setAutoExclusive(False)
            rb.setChecked(False)
            rb.setAutoExclusive(True)

        self.ui.method_comboBox.clear()
