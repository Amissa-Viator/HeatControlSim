from core.database.dao.repository.input_data_repo import get_input_id
from core.database.dao.repository.method_type_repo import get_method_id_by_name
from core.database.dao.repository.setup_repo import get_setup_id_by_data
from core.database.dao.repository.task_type_repo import get_task_id_by_name


def uniqueness_of_task_run(connection, input_entity, task_entity, method_entities) -> bool:
    try:
        cursor = connection.cursor()

        task_id = get_task_id_by_name(cursor, task_entity.name)
        input_id = get_input_id(cursor, input_entity)

        if not task_id or not input_id:
            return True

        setup_ids = []
        for method_entity in method_entities:
            method_id = get_method_id_by_name(cursor, method_entity.name)
            if method_id:
                setup_id = get_setup_id_by_data(cursor, input_id, task_id, method_id)
                if setup_id:
                    setup_ids.append(setup_id)

        return len(setup_ids) == 0

    except Exception as e:
        print("Error:", e)
        return False
