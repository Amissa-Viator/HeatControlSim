import unicodedata

from core.database.entity.task_type import TaskType


def insert_or_get_task_type(cursor, entity: TaskType):
    if entity.id is not None:
        return entity.id

    cursor.execute("INSERT OR IGNORE INTO task_type (name) VALUES (?)", (entity.name,))

    cursor.execute("SELECT id FROM task_type WHERE name = ?", (entity.name,))

    row = cursor.fetchone()
    if row is None:
        raise RuntimeError("Critical DB error: task_type missing after insert.")

    return row[0]


def delete_task_type_if_unused(cursor, task_id: int):
    cursor.execute("SELECT COUNT(*) FROM calculation_setup WHERE id_task = ?", (task_id,))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("DELETE FROM task_type WHERE id = ?", (task_id,))
        return cursor.rowcount
    return 0


def get_task_name_by_id(cursor, task_id):
    cursor.execute("SELECT name FROM task_type WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    return row[0] if row else None


def get_task_id_by_name(cursor, task_name: str):
    task_name_norm = unicodedata.normalize("NFC", task_name).strip().lower()

    cursor.execute("SELECT id, name FROM task_type")
    for row in cursor.fetchall():
        db_name_norm = unicodedata.normalize("NFC", row[1]).strip().lower()
        if db_name_norm == task_name_norm:
            return row[0]
    return None


def get_task_entity_by_id(cursor, task_id):
    cursor.execute("SELECT name FROM task_type WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    if not row:
        return None

    return TaskType(
        name=row[0],
        id=task_id
    )
