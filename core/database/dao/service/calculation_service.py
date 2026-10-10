from core.database.dao.repository.files_repo import insert_or_get_files, delete_files_by_id, get_files_id
from core.database.dao.repository.files_results_repo import insert_files_result, delete_files_result_by_result_id
from core.database.dao.repository.input_data_repo import insert_input_data, delete_input_data_if_unused, get_input_id
from core.database.dao.repository.method_type_repo import insert_or_get_method_type, delete_method_type_if_unused, \
    get_method_id_by_name
from core.database.dao.repository.results_repo import insert_result, delete_result_by_id, get_result_id
from core.database.dao.repository.setup_repo import insert_or_get_setup, delete_setup_by_data
from core.database.dao.repository.task_type_repo import insert_or_get_task_type, delete_task_type_if_unused, \
    get_task_id_by_name


def save_calculation_run(conn, input_entity, task_entity, method_entities,
                         setup_entities, results_entities, files_entity) -> bool:
    try:
        cursor = conn.cursor()

        input_entity.id = insert_input_data(cursor, input_entity)
        task_entity.id = insert_or_get_task_type(cursor, task_entity)

        for method_entity in method_entities:
            method_entity.id = insert_or_get_method_type(cursor, method_entity)

        for i, setup_entity in enumerate(setup_entities):
            setup_entity.id = insert_or_get_setup(cursor, input_entity, task_entity, method_entities[i], setup_entity)

        for i, res in enumerate(results_entities):
            res.id = insert_result(cursor, setup_entities[i], res)

        files_entity.id = insert_or_get_files(cursor, files_entity)

        for res in results_entities:
            insert_files_result(cursor, res, files_entity)

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return False


def mark_deleted(deleted_any: bool, rows: int) -> bool:
    return deleted_any or rows > 0


def delete_calculation_run(connection, input_entity, task_entity, method_entities,
                           results_entities, files_entity) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        deleted_any = False

        for res in results_entities:
            res_id = get_result_id(cursor, res)
            if res_id:
                deleted_any = mark_deleted(deleted_any, delete_files_result_by_result_id(cursor, res_id))
                deleted_any = mark_deleted(deleted_any, delete_result_by_id(cursor, res_id))

        files_id = get_files_id(cursor, files_entity)
        if files_id:
            deleted_any = mark_deleted(deleted_any, delete_files_by_id(cursor, files_id))

        task_id = get_task_id_by_name(cursor, task_entity.name)
        input_id = get_input_id(cursor, input_entity)

        method_ids = []
        for method_entity in method_entities:
            method_id = get_method_id_by_name(cursor, method_entity.name)
            if method_id:
                method_ids.append(method_id)

        for method_id in method_ids:
            if task_id and input_id:
                deleted_any = mark_deleted(deleted_any, delete_setup_by_data(cursor, input_id, task_id, method_id))

        if task_id:
            delete_task_type_if_unused(cursor, task_id)

        for method_id in method_ids:
            delete_method_type_if_unused(cursor, method_id)

        delete_input_data_if_unused(cursor, input_id)

        connection.commit()
        return deleted_any

    except Exception as e:
        connection.rollback()
        print("Error:", e)
        return False

