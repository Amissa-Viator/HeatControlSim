from core.database.dao.repository.files_repo import get_files_data_by_id
from core.database.dao.repository.files_results_repo import get_files_by_result_id
from core.database.dao.repository.input_data_repo import get_input_data_by_id
from core.database.dao.repository.results_repo import get_results_data_by_setup_id
from core.database.dao.repository.setup_repo import get_related_setups, get_unique_setups
from core.database.dao.repository.task_type_repo import get_task_name_by_id


def load_group_overview(cursor, input_id: int, task_id: int):
    setups = get_related_setups(cursor, input_id, task_id)

    setup_ids = [row[0] for row in setups]
    method_names = [row[1] for row in setups]

    input_data = get_input_data_by_id(cursor, input_id)

    problem_name = get_task_name_by_id(cursor, task_id)

    return {
        "input_data": input_data,
        "problem_name": problem_name,
        "setup_ids": setup_ids,
        "method_names": method_names
    }


def load_all_tasks_overviews(connection):
    cursor = connection.cursor()

    groups = get_unique_setups(cursor)

    all_overviews = []

    for input_id, task_id in groups:
        overview = load_group_overview(cursor, input_id, task_id)
        all_overviews.append(overview)

    return all_overviews


def load_all_results_info(connection, setup_ids):
    results_info = []

    cursor = connection.cursor()

    for setup_id in setup_ids:
        result_values = get_results_data_by_setup_id(cursor, setup_id)
        results_info.append(result_values)

    files_id = get_files_by_result_id(cursor, results_info[0].id)
    files = get_files_data_by_id(cursor, files_id)

    return results_info, files
