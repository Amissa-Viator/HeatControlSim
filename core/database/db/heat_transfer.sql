PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS input_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    k_expression TEXT NOT NULL,
    phi_expression TEXT NOT NULL,
    f_expression TEXT NOT NULL,
    u0 REAL NOT NULL,
    ul REAL NOT NULL,
    eps REAL NOT NULL,
    alpha REAL NOT NULL,
    v_initial REAL NOT NULL,
    n_max INTEGER NOT NULL,
    n_min INTEGER,
    v_max REAL
);

CREATE TABLE IF NOT EXISTS task_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS method_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS calculation_setup (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_input_data INTEGER NOT NULL,
    id_task INTEGER NOT NULL,
    id_method INTEGER NOT NULL,

    FOREIGN KEY(id_input_data) REFERENCES input_data(id) ON DELETE CASCADE,
    FOREIGN KEY(id_task) REFERENCES task_type(id) ON DELETE CASCADE,
    FOREIGN KEY(id_method) REFERENCES method_type(id) ON DELETE CASCADE,

    CONSTRAINT unique_setup UNIQUE(id_input_data, id_task, id_method)
);

CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_setup INTEGER NOT NULL,
    iterations INTEGER NOT NULL,
    time_ms REAL NOT NULL,
    v_norm REAL NOT NULL,
    functional REAL NOT NULL,
    gradient_norm REAL NOT NULL,
    functional_plot_path TEXT NOT NULL,
    rod_plot_path TEXT NOT NULL,

    FOREIGN KEY(id_setup) REFERENCES calculation_setup(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    excel_path TEXT NOT NULL,
    phi_plot_path TEXT NOT NULL,
    control_plot_path TEXT NOT NULL,
    distribution_plot_path TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS files_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_result INTEGER NOT NULL,
    id_files INTEGER NOT NULL,

    FOREIGN KEY(id_result) REFERENCES results(id) ON DELETE CASCADE,
    FOREIGN KEY(id_files) REFERENCES files(id) ON DELETE CASCADE
);