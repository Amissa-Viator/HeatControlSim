from core.database.dao.repository.setup_repo import get_setup_entity_by_id
from core.database.entity.calculation_setup import CalculationSetup
from core.database.entity.results import Results


def insert_result(cursor, setup_entity: CalculationSetup, res_entity: Results):
    if res_entity.id is not None:
        return res_entity.id

    cursor.execute("""
            INSERT INTO results 
            (id_setup, iterations, time_ms, v_norm, functional, gradient_norm, functional_plot_path, rod_plot_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
        setup_entity.id,
        res_entity.iterations,
        res_entity.time_ms,
        res_entity.v_norm,
        res_entity.functional,
        res_entity.gradient_norm,
        res_entity.functional_plot_path,
        res_entity.rod_plot_path
    ))

    return cursor.lastrowid


def delete_result_by_id(cursor, result_id: int):
    cursor.execute(" DELETE FROM results WHERE id = ?", (result_id,))
    return cursor.rowcount


def get_results_data_by_setup_id(cursor, setup_id: int):
    cursor.execute("SELECT * FROM results WHERE id_setup = ?", (setup_id,))
    row = cursor.fetchone()
    if not row:
        return None

    setup_entity = get_setup_entity_by_id(cursor, setup_id)

    return Results(
        setup=setup_entity,
        iterations=row[2],
        time_ms=row[3],
        v_norm=row[4],
        functional=row[5],
        gradient_norm=row[6],
        functional_plot_path=row[7],
        rod_plot_path=row[8],
        id=row[0]
    )


def get_result_id(cursor, res_entity: Results):
    cursor.execute("""
        SELECT id FROM results
        WHERE iterations = ?
          AND time_ms = ?
          AND v_norm = ?
          AND functional = ?
          AND gradient_norm = ?
          AND functional_plot_path = ?
          AND rod_plot_path = ?
    """, (
        res_entity.iterations,
        res_entity.time_ms,
        res_entity.v_norm,
        res_entity.functional,
        res_entity.gradient_norm,
        res_entity.functional_plot_path,
        res_entity.rod_plot_path
    ))
    row = cursor.fetchone()
    return row[0] if row else None
