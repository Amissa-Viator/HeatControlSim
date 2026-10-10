import os
from core.calculation.load_calculation import start_calculation
from core.data_worker.problems_solutions import ProblemType, SolutionMethod
from core.data_worker.data import Data
from core.excel_worker.excel_writer import ExcelWriter
from core.excel_worker.workbook_manager import WorkbookManager
from core.visualization.plot_builder import plot_functional_over_iterations, plot_control_vectors, \
    plot_distribution_vectors, plot_2d_distribution


class ResultData:
    def __init__(self, method, result, functional_values, gradient_norm, v_norm, iterations,
                 time_ms, functional):
        self.method = method
        self.result = result
        self.functional_values = functional_values
        self.gradient_norm = gradient_norm
        self.v_norm = v_norm
        self.iterations = iterations
        self.time_ms = time_ms
        self.functional = functional


def run_calculation(data: Data, problem: ProblemType, method: SolutionMethod, v_initial: float):
    results_data = start_calculation(data, problem, method, v_initial)

    result_objects = []
    plot_paths = {}

    for entry in results_data:
        save_entry_to_excel(entry)

        res_obj = ResultData(
            method=entry["method"],
            result=entry["result"],
            functional_values=entry["functional_values"],
            gradient_norm=entry["gradient_norm"],
            v_norm=entry["v_norm"],
            iterations=entry["iterations"],
            time_ms=entry["time_ms"],
            functional=entry["functional"]
        )

        result_objects.append(res_obj)

        path = plot_functional_over_iterations(res_obj)
        plot_paths[f"J(v) {res_obj.method}"] = path

    excel_path = os.path.abspath(WorkbookManager._file_path)
    close_excel_workbook()

    input_info = make_input_info_dict(data, problem, method, v_initial)
    result_info = make_result_info(result_objects)

    plot_path_v = plot_control_vectors(result_objects)
    plot_paths["v(x)"] = plot_path_v

    phi_values = calculate_phi_values(result_objects, data)

    plot_path_u = plot_distribution_vectors(result_objects, phi_values)
    plot_paths["u(x) and φ(x)"] = plot_path_u

    plot_path_2d_phi = create_2d_phi_distribution_plot(phi_values, result_objects)
    plot_paths["2D φ(x)"] = plot_path_2d_phi

    u_2d_plot_paths = create_2d_plot_u(result_objects)
    for i, path in enumerate(u_2d_plot_paths):
        plot_paths[f"2D u(x) {result_objects[i].method}"] = path

    return result_info, input_info, excel_path, plot_paths


def calculate_phi_values(result_objects, data):
    phi_values = []
    x_values = [out.x_value for out in result_objects[0].result]

    for x in x_values:
        phi_values.append(data.phi(x))

    return phi_values


def create_2d_phi_distribution_plot(phi_values, result_objects):
    x_values = [out.x_value for out in result_objects[0].result]
    phi_path = plot_2d_distribution(x_values, phi_values, "φ(x)", filename="phi_distribution.png")

    return phi_path


def create_2d_plot_u(result_objects):
    u_paths = []
    x_values = [out.x_value for out in result_objects[0].result]

    for i, res in enumerate(result_objects):
        u_values = [out.u_value for out in res.result]
        name = res.method + " u(x)"
        path = plot_2d_distribution(x_values, u_values, name, filename=f"u_distribution_{i}.png")
        u_paths.append(path)
    return u_paths


def get_problem_and_method(problem: ProblemType, method: SolutionMethod) -> tuple[str, str]:
    if problem == ProblemType.WITHOUT_CONSTRAINT:
        problem_name = "Without Control Constraints"
        if method == SolutionMethod.GRADIENT_METHOD:
            method_name = "Gradient Method"
        elif method == SolutionMethod.MODIFIED_METHOD:
            method_name = "Modified Gradient Method"
        else:
            method_name = "Comparison of Gradient Method and Modified Gradient Method"
    else:
        problem_name = "With Control Constraints"
        if method == SolutionMethod.CONDITIONAL_GRADIENT_METHOD:
            method_name = "Conditional Gradient Method"
        elif method == SolutionMethod.MODIFIED_METHOD:
            method_name = "Modified Conditional Gradient Method"
        else:
            method_name = "Comparison of Conditional Gradient Method and Modified Conditional Gradient Method"

    return problem_name, method_name


def make_input_info_dict(data: Data, problem: ProblemType, method: SolutionMethod, v_initial: float) -> dict:
    input_info = {}
    problem_name, method_name = get_problem_and_method(problem, method)
    input_info["Problem"] = problem_name
    input_info["Method"] = method_name

    input_info["ε"] = data.epsilon
    input_info["α"] = data.alpha
    input_info["v⁽⁰⁾"] = v_initial

    if method in (SolutionMethod.GRADIENT_METHOD, SolutionMethod.CONDITIONAL_GRADIENT_METHOD):
        input_info["n"] = data.n_max
    else:
        input_info["n₁"] = data.n_min
        input_info["nₘₐₓ"] = data.n_max

    if problem == ProblemType.WITH_CONSTRAINT:
        input_info["vₘₐₓ"] = data.v_max

    input_info["u(0)"] = data.u_boundary.A
    input_info["u(l)"] = data.u_boundary.B

    input_info["f(x)"] = str(data.f_expr)
    input_info["k(x)"] = str(data.k_expr)
    input_info["φ(x)"] = str(data.phi_expr)

    return input_info


def make_result_info(result_list) -> list:
    results = []

    for res in result_list:
        result = {
            "Method": res.method,
            "Iterations": res.iterations,
            "Execution Time (ms)": f"{res.time_ms:.2f}",
            "J(v)": f"{res.functional:.4g}",
            "||J'(v)||": f"{res.gradient_norm:.4g}",
            "||v(x)||": f"{res.v_norm:.4g}",
        }
        results.append(result)

    return results


def save_entry_to_excel(entry: dict):
    method = entry["method"]

    if method in ("Gradient Method", "Conditional Gradient Method"):
        result_list = entry["result"]
        ExcelWriter.export_values(result_list, method)
        ExcelWriter.export_functional(entry["functional_values"], f"J(v) {method}")
        ExcelWriter.export_gradient(entry.get("gradient_values"), f"J'(v) {method}")
    else:
        result_list_per_level = entry["results_per_level"]
        for i, level_list in enumerate(result_list_per_level):
            ExcelWriter.export_values(level_list, f"{method} {i+1}")
            ExcelWriter.export_functional(entry["functionals_per_level"][i], f"J(v) Modified Method {i}")
            ExcelWriter.export_gradient(entry["gradients_per_level"][i], f"J'(v) Modified Method {i}")


def close_excel_workbook():
    WorkbookManager.save_workbook()
    WorkbookManager.close_workbook()
