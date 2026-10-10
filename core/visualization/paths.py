import os

from core.database.utils.settings import PLOTS_DIR


def create_directory_if_not_exists():
    result_dir = PLOTS_DIR
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    return result_dir


def get_unique_plot_path(base_name, folder):
    path = os.path.join(folder, base_name)
    name, ext = os.path.splitext(base_name)
    counter = 1
    while os.path.exists(path):
        path = os.path.join(folder, f"{name}_{counter}{ext}")
        counter += 1
    return path


def create_filepath_for_functional(method):
    folder = create_directory_if_not_exists()

    method_name = method.replace(" ", "_")
    filename = f"{method_name}_functional.png"

    filepath = get_unique_plot_path(filename, folder)
    return filepath


def create_filepath_for_vectors(filename):
    folder = create_directory_if_not_exists()
    filepath = get_unique_plot_path(filename, folder)

    return filepath
