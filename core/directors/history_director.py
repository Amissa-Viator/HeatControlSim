from core.database.dao.service.loader_service import load_all_tasks_overviews, load_all_results_info
from core.database.entity.files import Files
from core.database.entity.input_data import InputData
from core.database.entity.results import Results
from core.database.utils.connection_manager import ConnectionManager


def create_input_info_dict(input_data: InputData, problem_name, methods) -> dict:
    input_info = {}
    method_name = get_method(problem_name, methods)

    input_info["Problem"] = problem_name
    input_info["Method"] = method_name
    input_info["ε"] = input_data.eps
    input_info["α"] = input_data.alpha
    input_info["v⁽⁰⁾"] = input_data.v_initial

    classic_methods = {
        "Gradient Method",
        "Conditional Gradient Method",
    }

    modified_methods = {
        "Modified Gradient Method",
        "Comparison of Gradient Method and Modified Gradient Method",
        "Modified Conditional Gradient Method",
        "Comparison of Conditional Gradient Method and Modified Conditional Gradient Method",
    }

    if method_name in classic_methods:
        input_info["n"] = input_data.n_max
    elif method_name in modified_methods:
        input_info["n₁"] = input_data.n_min
        input_info["nₘₐₓ"] = input_data.n_max

    if problem_name == "With Control Constraints":
        input_info["vₘₐₓ"] = input_data.v_max

    input_info["u(0)"] = input_data.u0
    input_info["u(l)"] = input_data.ul

    input_info["f(x)"] = input_data.f_expression
    input_info["k(x)"] = input_data.k_expression
    input_info["φ(x)"] = input_data.phi_expression

    return input_info


def get_method(problem, methods) -> str:
    constrained = problem != "Without Control Constraints"

    base = "Conditional Gradient Method" if constrained else "Gradient Method"
    modified = f"Modified {base}"

    if len(methods) == 2:
        return f"Comparison of {base} and {modified}"

    return modified if methods[0] == modified else base


def search_all_solved_problems():
    with ConnectionManager() as cm:
        connection = cm.get_connection()
        overviews = load_all_tasks_overviews(connection)

    problems = []

    for ov in overviews:
        problem = create_input_info_dict(ov.get("input_data"), ov.get("problem_name"), ov.get("method_names"))
        problems.append(problem)

    return problems, overviews


def get_result_for_problem(problem, overview):
    setup_ids = overview["setup_ids"]
    with ConnectionManager() as cm:
        connection = cm.get_connection()
        results_list, files = load_all_results_info(connection, setup_ids)

    results = get_results_list(results_list, overview.get("method_names"))
    excel_path = get_excel_path(files)
    plot_paths = collect_all_plots(results_list, files, overview.get("method_names"))

    return results, problem, excel_path, plot_paths


def get_results_list(results_entities: list[Results], method_names):
    results = []

    for i, entity in enumerate(results_entities):
        result = {
            "Method": method_names[i],
            "Iterations": entity.iterations,
            "Executed time (ms)": entity.time_ms,
            "J(v)": entity.functional,
            "||J'(v)||": entity.gradient_norm,
            "||v(x)||": entity.v_norm,
        }
        results.append(result)

    return results


def collect_all_plots(results_entities: list[Results], files: Files, methods):
    plot_paths = {}
    for i, res in enumerate(results_entities):
        plot_paths[f"J(v) {methods[i]}"] = res.functional_plot_path

    plot_paths["v(x)"] = files.control_plot_path
    plot_paths["u(x) and φ(x)"] = files.distribution_plot_path
    plot_paths["2D φ(x)"] = files.phi_plot_path

    for i, res in enumerate(results_entities):
        plot_paths[f"2D u(x) {methods[i]}"] = res.rod_plot_path

    return plot_paths


def get_excel_path(files: Files) -> str:
    path = files.excel_path
    return path

