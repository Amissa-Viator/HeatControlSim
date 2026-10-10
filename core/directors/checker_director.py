from core.data_worker.data import Data
from core.data_worker.problems_solutions import ProblemType, SolutionMethod
from core.database.dao.service.checker_service import uniqueness_of_task_run
from core.database.entity.input_data import InputData
from core.database.entity.method_type import MethodType
from core.database.entity.task_type import TaskType
from core.database.utils.connection_manager import ConnectionManager


def create_input_data_entity_from_data(data: Data, v_initial) -> InputData:
    return InputData(
        k_expression=str(data.k_expr),
        phi_expression=str(data.phi_expr),
        f_expression=str(data.f_expr),
        u0=data.u_boundary.A,
        ul=data.u_boundary.B,
        eps=data.epsilon,
        alpha=data.alpha,
        v_initial=v_initial,
        n_max=data.n_max,
        n_min=data.n_min,
        v_max=data.v_max
    )


def create_task_type_entity(problem: ProblemType) -> TaskType:
    if problem == ProblemType.WITHOUT_CONSTRAINT:
        problem_name = "Without Control Constraints"
    else:
        problem_name = "With Control Constraints"
    return TaskType(name=problem_name)


def get_methods(problem: ProblemType, method: SolutionMethod) -> list[str]:
    method_names = []
    if problem == ProblemType.WITHOUT_CONSTRAINT:
        if method == SolutionMethod.GRADIENT_METHOD:
            method_names.append("Gradient Method")
        elif method == SolutionMethod.MODIFIED_METHOD:
            method_names.append("Modified Gradient Method")
        else:
            method_names.append("Gradient Method")
            method_names.append("Modified Gradient Method")
    else:
        if method == SolutionMethod.CONDITIONAL_GRADIENT_METHOD:
            method_names.append("Conditional Gradient Method")
        elif method == SolutionMethod.MODIFIED_METHOD:
            method_names.append("Modified Conditional Gradient Method")
        else:
            method_names.append("Conditional Gradient Method")
            method_names.append("Modified Conditional Gradient Method")

    return method_names


def create_method_type_entity(problem: ProblemType, method: SolutionMethod) -> list[MethodType]:
    method_names = get_methods(problem, method)
    method_entities = []

    for method in method_names:
        method_entity = MethodType(name=method)
        method_entities.append(method_entity)

    return method_entities


def compare_task_with_db_records(data, task_choice, method_choice, v_initial) -> bool:
    input_entity = create_input_data_entity_from_data(data, v_initial)
    task_entity = create_task_type_entity(task_choice)
    method_entities = create_method_type_entity(task_choice, method_choice)

    with ConnectionManager() as cm:
        connection = cm.get_connection()
        is_unique = uniqueness_of_task_run(connection, input_entity, task_entity,
                                           method_entities)

    return is_unique
