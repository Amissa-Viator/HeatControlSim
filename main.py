import sys
import argparse
from PySide6.QtWidgets import QApplication
from core.database.utils.database_setup import ensure_db_exists, reset_db
from gui.ui_logic.main_window import MainWindow


def start():
    ensure_db_exists()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


def main():
    parser = argparse.ArgumentParser(
        description="Information System for Optimal Control of Thermostatic Processes on the Rod"
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--init-db",
        action="store_true",
        help="Initialize the database if it does not exist."
    )

    group.add_argument(
        "--reset-db",
        action="store_true",
        help="Reset the database and remove generated files."
    )

    args = parser.parse_args()

    if args.reset_db:
        reset_db()
        return

    if args.init_db:
        ensure_db_exists()
        return

    start()


if __name__ == "__main__":
    main()