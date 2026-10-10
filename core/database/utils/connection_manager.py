import sqlite3
from core.database.utils.settings import DB_PATH


class ConnectionManager:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        if self.connection is None:
            raise RuntimeError("Connection isn't opened. Use 'with ConnectionManager() as cm:'")
        return self.connection.cursor()



