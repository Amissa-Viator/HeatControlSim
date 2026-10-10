from core.database.entity.files import Files
from core.database.entity.results import Results


def insert_files_result(cursor, res: Results, files_entity: Files):
    cursor.execute("""
                    INSERT INTO files_results (id_result, id_files)
                    VALUES (?, ?)
                """,
                   (res.id, files_entity.id))


def delete_files_result_by_result_id(cursor, result_id: int):
    cursor.execute("DELETE FROM files_results WHERE id_result = ?", (result_id,))

    return cursor.rowcount


def get_files_by_result_id(cursor, result_id: int):
    cursor.execute(
        "SELECT id_files FROM files_results WHERE id_result = ?",
        (result_id,)
    )
    row = cursor.fetchone()

    return row[0] if row else None
