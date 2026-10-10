from core.database.dao.service.calculation_service import save_calculation_run, delete_calculation_run
from core.database.entity.calculation_setup import CalculationSetup
from core.database.entity.files import Files
from core.database.entity.input_data import InputData
from core.database.entity.method_type import MethodType
from core.database.entity.results import Results
from core.database.entity.task_type import TaskType
from core.database.utils.connection_manager import ConnectionManager


def create_input_data_entity(input_info: dict) -> InputData:
    return InputData(
        k_expression=input_info["k(x)"],
        phi_expression=input_info["φ(x)"],
        f_expression=input_info["f(x)"],
        u0=input_info["u(0)"],
        ul=input_info["u(l)"],
        eps=input_info["ε"],
        alpha=input_info["α"],
        v_initial=input_info["v⁽⁰⁾"],
        n_max=input_info.get("nₘₐₓ") or input_info.get("n"),
        n_min=input_info.get("n₁") or None,
        v_max=input_info.get("vₘₐₓ") or None
    )


def create_task_type_entity(input_info: dict) -> TaskType:
    return TaskType(name=input_info["Problem"])


def create_method_type_entity(results: list) -> list[MethodType]:
    method_entities = []

    for res in results:
        method_entity = MethodType(name=res["Method"])
        method_entities.append(method_entity)

    return method_entities


def create_setup_entity(input_entity, task_entity, method_entities) -> list[CalculationSetup]:
    calculation_setups = []

    for method in method_entities:
        setup_entity = CalculationSetup(input_data=input_entity, task=task_entity, method=method)
        calculation_setups.append(setup_entity)

    return calculation_setups


def create_result_entities(results: list, setup_entities, plot_paths: dict) -> list[Results]:
    results_entities = []

    for i, res in enumerate(results):
        result_entity = Results(
            setup=setup_entities[i],
            iterations=res.get("Iterations"),
            time_ms=res.get("Execution Time (ms)"),
            v_norm=res.get("||v(x)||"),
            functional=res.get("J(v)"),
            gradient_norm=res.get("||J'(v)||"),
            functional_plot_path=plot_paths.get(f"J(v) {res.get('Method')}"),
            rod_plot_path=plot_paths.get(f"2D u(x) {res.get('Method')}")
        )
        results_entities.append(result_entity)

    return results_entities


def create_files_entity(plot_paths: dict, excel_path: str) -> Files:
    return Files(
        excel_path=excel_path,
        distribution_plot_path=plot_paths.get("u(x) and φ(x)"),
        control_plot_path=plot_paths.get("v(x)"),
        phi_plot_path=plot_paths.get("2D φ(x)")
    )


def save_to_database(result_info, input_info, excel_path, plot_paths) -> bool:
    input_entity = create_input_data_entity(input_info)
    task_entity = create_task_type_entity(input_info)
    method_entities = create_method_type_entity(result_info)

    setup_entities = create_setup_entity(input_entity, task_entity, method_entities)

    results_entities = create_result_entities(result_info, setup_entities, plot_paths)
    files_entity = create_files_entity(plot_paths, excel_path)

    with ConnectionManager() as cm:
        connection = cm.get_connection()
        is_saved = save_calculation_run(connection, input_entity, task_entity,
                                        method_entities, setup_entities, results_entities, files_entity)

    return is_saved


def delete_record_from_database(result_info, input_info, excel_path, plot_paths) -> bool:
    input_entity = create_input_data_entity(input_info)
    task_entity = create_task_type_entity(input_info)
    method_entities = create_method_type_entity(result_info)

    setup_entities = create_setup_entity(input_entity, task_entity, method_entities)

    results_entities = create_result_entities(result_info, setup_entities, plot_paths)
    files_entity = create_files_entity(plot_paths, excel_path)

    with ConnectionManager() as cm:
        connection = cm.get_connection()
        is_deleted = delete_calculation_run(connection, input_entity, task_entity, method_entities, results_entities,
                                            files_entity)

    return is_deleted

