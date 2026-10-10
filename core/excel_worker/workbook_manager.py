import os
from openpyxl import Workbook

from core.database.utils.settings import RESULTS_DIR


class WorkbookManager:
    _workbook = None
    _file_path = None

    @staticmethod
    def create_directory_if_not_exists():
        if not os.path.exists(RESULTS_DIR):
            os.makedirs(RESULTS_DIR)
            print(f"Directory created: {RESULTS_DIR}")

    @classmethod
    def get_workbook(cls):
        if cls._workbook is None:
            cls.create_directory_if_not_exists()
            cls._workbook = Workbook()

            if "Sheet" in cls._workbook.sheetnames:
                std = cls._workbook["Sheet"]
                cls._workbook.remove(std)

            cls._file_path = cls.get_unique_file_path()
        return cls._workbook

    @classmethod
    def get_unique_file_path(cls, base_name="outputData.xlsx"):
        path = os.path.join(RESULTS_DIR, base_name)
        counter = 1
        while os.path.exists(path):
            path = os.path.join(RESULTS_DIR, f"{base_name[:-5]}_{counter}.xlsx")
            counter += 1
        return path

    @classmethod
    def save_workbook(cls):
        if cls._workbook is None or cls._file_path is None:
            print("Workbook not initialized")
            return

        cls._workbook.save(cls._file_path)
        print(f"Workbook successfully saved to {cls._file_path}")

    @classmethod
    def close_workbook(cls):
        cls._workbook = None
        cls._file_path = None
        print("Workbook closed")
