from core.data_worker.data import Data
from core.data_worker.output_data import OutputData


def collect_all_results(data: Data, size: int, x_values, u_values, v_values):
    result = [OutputData(x_values[i], u_values[i], v_values[i])
              for i in range(size)]

    step = (Data.RIGHT_BORDER - Data.LEFT_BORDER) / (size - 1)
    functional_value = data.method_simpson(x_values, u_values, step)

    return result, functional_value
