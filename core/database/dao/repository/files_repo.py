from core.database.entity.files import Files


def insert_or_get_files(cursor, entity: Files):
    if entity.id is not None:
        return entity.id

    cursor.execute("""
                        INSERT OR IGNORE INTO files 
                        (excel_path, phi_plot_path, control_plot_path, distribution_plot_path)
                        VALUES (?, ?, ?, ?)
                    """,
                   (entity.excel_path, entity.phi_plot_path,
                    entity.control_plot_path, entity.distribution_plot_path))
    cursor.execute("""
                        SELECT id FROM files
                        WHERE excel_path = ? AND phi_plot_path = ?
                            AND control_plot_path = ? AND distribution_plot_path = ?
                    """,
                   (entity.excel_path, entity.phi_plot_path,
                    entity.control_plot_path, entity.distribution_plot_path))

    row = cursor.fetchone()
    if row is None:
        raise RuntimeError("Critical DB error: files missing after insert.")

    return row[0]


def delete_files_by_id(cursor, files_id: int):
    cursor.execute("DELETE FROM files WHERE id = ?", (files_id,))
    return cursor.rowcount


def get_files_data_by_id(cursor, files_id: int):
    cursor.execute("SELECT * FROM files WHERE id = ?", (files_id,))
    row = cursor.fetchone()
    if not row:
        return None

    return Files(
        excel_path=row[1],
        phi_plot_path=row[2],
        control_plot_path=row[3],
        distribution_plot_path=row[4],
        id=files_id
    )


def get_files_id(cursor, files_entity: Files):
    cursor.execute("""
        SELECT id FROM files
        WHERE excel_path = ?
          AND phi_plot_path = ?
          AND control_plot_path = ?
          AND distribution_plot_path = ?
    """, (
        files_entity.excel_path,
        files_entity.phi_plot_path,
        files_entity.control_plot_path,
        files_entity.distribution_plot_path
    ))
    row = cursor.fetchone()
    return row[0] if row else None

