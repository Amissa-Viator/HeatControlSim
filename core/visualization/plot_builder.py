import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from core.visualization.paths import (
    create_filepath_for_functional,
    create_filepath_for_vectors,
    get_unique_plot_path,
    create_directory_if_not_exists
)


def plot_functional_over_iterations(result_obj):
    filepath = create_filepath_for_functional(result_obj.method)

    iteration_x = np.array(range(1, len(result_obj.functional_values) + 1))
    functional_y = np.array(result_obj.functional_values)

    x_smooth = np.linspace(iteration_x.min(), iteration_x.max(), 300)
    spline = make_interp_spline(iteration_x, functional_y, k=3)
    y_smooth = spline(x_smooth)

    plt.figure(figsize=(12, 6))
    plt.plot(x_smooth, y_smooth, linewidth=1.5, linestyle='-')
    plt.scatter(iteration_x, functional_y, color="#00008B", s=10)
    plt.xlabel("Iterations", fontsize=14)
    plt.ylabel("J(v)", fontsize=14)
    plt.title(f"Objective Function Behavior ({result_obj.method})", fontsize=16)
    plt.grid(True)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.close()

    return filepath


def plot_control_vectors(result_objects):
    filepath = create_filepath_for_vectors("v_functions.png")

    plt.figure(figsize=(10, 6))

    x_values = [out.x_value for out in result_objects[0].result]

    for res in result_objects:
        v_values = [out.v_value for out in res.result]
        plt.plot(x_values, v_values, label=res.method, linewidth=1.5)

    plt.xlabel("x", fontsize=14)
    plt.ylabel("v(x)", fontsize=14)
    plt.title("Control Functions v(x)", fontsize=16)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.close()

    return filepath


def plot_distribution_vectors(result_objects, phi_values):
    filepath = create_filepath_for_vectors("u_functions.png")

    plt.figure(figsize=(10, 6))

    x_values = [out.x_value for out in result_objects[0].result]

    for res in result_objects:
        u_values = [out.u_value for out in res.result]
        plt.plot(x_values, u_values, label=res.method, linewidth=1.5)

    plt.plot(x_values, phi_values, label="φ(x)", linewidth=2, color="red", linestyle="--")

    plt.xlabel("x", fontsize=14)
    plt.ylabel("u(x)", fontsize=14)
    plt.title("Temperature Distributions u(x) and φ(x)", fontsize=16)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.close()

    return filepath


def plot_2d_distribution(x_values, y_values, function_name, filename):
    folder = create_directory_if_not_exists()

    filepath = get_unique_plot_path(filename, folder)
    data = np.tile(y_values, (10, 1))

    plt.figure(figsize=(8, 2))
    plt.imshow(data, extent=[x_values[0], x_values[-1], 0, 1], aspect='auto', cmap='inferno')
    plt.colorbar(label="Function Value")
    plt.xlabel("x")
    plt.yticks([])
    plt.title(f"Distribution of {function_name} Along the Rod")
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.close()

    return filepath
