from core.database.entity.input_data import InputData


def insert_input_data(cursor, entity: InputData):
    if entity.id is not None:
        return entity.id

    cursor.execute("""
        INSERT INTO input_data (k_expression, phi_expression, f_expression, u0, ul, eps, alpha, v_initial, n_min, n_max, v_max)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entity.k_expression,
        entity.phi_expression,
        entity.f_expression,
        entity.u0,
        entity.ul,
        entity.eps,
        entity.alpha,
        entity.v_initial,
        entity.n_min,
        entity.n_max,
        entity.v_max
    ))
    return cursor.lastrowid


def delete_input_data_if_unused(cursor, input_id: int):
    cursor.execute("SELECT COUNT(*) FROM calculation_setup WHERE id_input_data = ?", (input_id,))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("DELETE FROM input_data WHERE id = ?", (input_id,))
        return cursor.rowcount
    return 0


def get_input_data_by_id(cursor, input_id: int):
    cursor.execute("SELECT * FROM input_data WHERE id = ?", (input_id,))
    row = cursor.fetchone()
    if not row:
        return None

    return InputData(
        k_expression=row[1],
        phi_expression=row[2],
        f_expression=row[3],
        u0=row[4],
        ul=row[5],
        eps=row[6],
        alpha=row[7],
        v_initial=row[8],
        n_max=row[9],
        n_min=row[10],
        v_max=row[11],
        id=row[0]
    )


def get_input_id(cursor, input_entity: InputData):
    cursor.execute("""
        SELECT id FROM input_data
        WHERE k_expression = ? AND phi_expression = ? AND f_expression = ?
            AND u0 = ? AND ul = ? AND eps = ? AND alpha = ? AND v_initial = ? AND n_max = ?
            AND (n_min = ? OR (n_min IS NULL AND ? IS NULL))
            AND (v_max = ? OR (v_max IS NULL AND ? IS NULL))
    """, (
        input_entity.k_expression, input_entity.phi_expression, input_entity.f_expression,
        input_entity.u0, input_entity.ul, input_entity.eps, input_entity.alpha,
        input_entity.v_initial, input_entity.n_max,
        input_entity.n_min, input_entity.n_min,
        input_entity.v_max, input_entity.v_max
    ))
    row = cursor.fetchone()
    return row[0] if row else None
