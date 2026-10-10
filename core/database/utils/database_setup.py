import sqlite3
from core.database.utils.settings import SQL_FILE, DB_PATH, RESULTS_DIR, PLOTS_DIR
from contextlib import closing
import shutil


def init_db():
    if not SQL_FILE.exists():
        raise FileNotFoundError(f"SQL script not found: {SQL_FILE}")

    sql_text = SQL_FILE.read_text(encoding="utf-8")

    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.executescript(sql_text)
        conn.commit()

    print("Database initialized.")


def reset_db():
    if DB_PATH.is_file():
        DB_PATH.unlink()

    for directory in (RESULTS_DIR, PLOTS_DIR):
        if directory.is_dir():
            for item in directory.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)

    init_db()
    print("Database and generated files have been reset.")


def ensure_db_exists():
    if not DB_PATH.is_file():
        init_db()

    print("Database is ready.")


