from core.database.dao.repository.input_data_repo import get_input_data_by_id
from core.database.dao.repository.method_type_repo import get_method_entity_by_id
from core.database.dao.repository.task_type_repo import get_task_entity_by_id
from core.database.entity.calculation_setup import CalculationSetup
from core.database.entity.input_data import InputData
from core.database.entity.method_type import MethodType
from core.database.entity.task_type import TaskType


def insert_or_get_setup(cursor, input_entity: InputData, task_entity: TaskType,
                        method_entity: MethodType, setup_entity: CalculationSetup):
    if setup_entity.id is not None:
        return setup_entity.id

    cursor.execute("""
                    INSERT OR IGNORE INTO calculation_setup (id_input_data, id_task, id_method)
                    VALUES (?, ?, ?)
                """,
                   (input_entity.id, task_entity.id, method_entity.id))
    cursor.execute("""
                    SELECT id FROM calculation_setup 
                    WHERE id_input_data = ? AND id_task = ? AND id_method = ?
                """,
                   (input_entity.id, task_entity.id, method_entity.id))

    row = cursor.fetchone()
    if row is None:
        raise RuntimeError("Critical DB error: calculation_setup missing after insert.")

    return row[0]


def delete_setup(cursor, setup_id: int):
    cursor.execute("DELETE FROM calculation_setup WHERE id = ?", (setup_id,))
    return cursor.rowcount


def get_setup_id_by_data(cursor, input_id: int, task_id: int, method_id: int):
    cursor.execute("SELECT id FROM calculation_setup WHERE id_input_data = ? AND id_task = ? AND id_method = ?",
                   (input_id, task_id, method_id))
    row = cursor.fetchone()
    return row[0] if row else None


def delete_setup_by_data(cursor, input_id: int, task_id: int, method_id: int):
    cursor.execute("""
        DELETE FROM calculation_setup
        WHERE id_input_data = ? AND id_task = ? AND id_method = ?
    """, (input_id, task_id, method_id))
    return cursor.rowcount


def get_setup_info(cursor, setup_id: int):
    cursor.execute("SELECT id_input_data, id_task FROM calculation_setup WHERE id = ?", (setup_id,))
    return cursor.fetchone()


def get_setup_ids(cursor):
    cursor.execute("SELECT id FROM calculation_setup ORDER BY id")
    setup_ids = [row[0] for row in cursor.fetchall()]

    return setup_ids


def get_related_setups(cursor, input_id: int, task_id: int):
    cursor.execute("""
            SELECT s.id, m.name
            FROM calculation_setup s
            JOIN method_type m ON s.id_method = m.id
            WHERE s.id_input_data = ? AND s.id_task = ?
        """, (input_id, task_id))
    return cursor.fetchall()


def get_unique_setups(cursor):
    cursor.execute("""
        SELECT DISTINCT id_input_data, id_task
        FROM calculation_setup
        ORDER BY id_input_data, id_task
    """)
    return cursor.fetchall()


def get_setup_entity_by_id(cursor, setup_id: int):
    cursor.execute("SELECT id_input_data, id_task, id_method FROM calculation_setup WHERE id = ?", (setup_id,))
    row = cursor.fetchone()

    if not row:
        return None

    id_input, id_task, id_method = row

    input_data = get_input_data_by_id(cursor, id_input)
    task = get_task_entity_by_id(cursor, id_task)
    method = get_method_entity_by_id(cursor, id_method)

    return CalculationSetup(
        input_data=input_data,
        task=task,
        method=method,
        id=setup_id
    )
