from core.database.entity.method_type import MethodType


def insert_or_get_method_type(cursor, entity: MethodType):
    if entity.id is not None:
        return entity.id

    cursor.execute("INSERT OR IGNORE INTO method_type (name) VALUES (?)", (entity.name,))

    cursor.execute("SELECT id FROM method_type WHERE name = ?", (entity.name,))

    row = cursor.fetchone()
    if row is None:
        raise RuntimeError("Critical DB error: method_type missing after insert.")

    return row[0]


def delete_method_type_if_unused(cursor, method_id: int):
    cursor.execute("SELECT COUNT(*) FROM calculation_setup WHERE id_method = ?", (method_id,))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("DELETE FROM method_type WHERE id = ?", (method_id,))
        return cursor.rowcount
    return 0


def get_method_entity_by_id(cursor, id_method: int):
    cursor.execute("SELECT name FROM method_type WHERE id = ?", (id_method,))
    row = cursor.fetchone()

    if not row:
        return None

    return MethodType(
        name=row[0],
        id=id_method
    )


def get_method_id_by_name(cursor, method_name: str):
    cursor.execute("SELECT id FROM method_type WHERE name = ?", (method_name,))
    row = cursor.fetchone()
    return row[0] if row else None

