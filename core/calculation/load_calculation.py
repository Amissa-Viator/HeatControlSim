import time
import numpy as np
from core.calculation.conditional_gradient_method import ConditionalGradientMethod
from core.calculation.gradient_method import GradientMethod
from core.calculation.modified_gradient_method import ModifiedGradientMethod
from core.calculation.utils import collect_all_results
from core.data_worker.data import Data
from core.data_worker.problems_solutions import ProblemType, SolutionMethod


def get_time(start: float, end: float):
    return (end - start) * 1000


def start_calculation(data: Data, problem: ProblemType, method: SolutionMethod, v_initial: float):
    methods_to_run = []

    if problem == ProblemType.WITHOUT_CONSTRAINT:
        if method == SolutionMethod.GRADIENT_METHOD:
            methods_to_run.append((lambda d: ordinary_gradient_method(d, v_initial), "Gradient Method"))
        elif method == SolutionMethod.MODIFIED_METHOD:
            methods_to_run.append(
                (lambda d: modified_gradient_method(d, v_initial, with_condition=False), "Modified Gradient Method"))
        else:
            methods_to_run.append((lambda d: ordinary_gradient_method(d, v_initial), "Gradient Method"))
            methods_to_run.append(
                (lambda d: modified_gradient_method(d, v_initial, with_condition=False), "Modified Gradient Method"))

    else:
        if method == SolutionMethod.CONDITIONAL_GRADIENT_METHOD:
            methods_to_run.append((lambda d: conditional_gradient_method(d, v_initial), "Conditional Gradient Method"))
        elif method == SolutionMethod.MODIFIED_METHOD:
            methods_to_run.append(
                (lambda d: modified_gradient_method(d, v_initial, with_condition=True), "Modified Conditional Gradient Method"))
        else:
            methods_to_run.append((lambda d: conditional_gradient_method(d, v_initial), "Conditional Gradient Method"))
            methods_to_run.append(
                (lambda d: modified_gradient_method(d, v_initial, with_condition=True), "Modified Conditional Gradient Method"))

    all_measurements = []

    for runner, name in methods_to_run:
        start = time.time()
        results = runner(data)
        end = time.time()

        time_in_ms = get_time(start, end)

        if "modified" in name.lower():
            all_measurements.extend(collect_measurements(modified_results=results,
                                                         time_ms=time_in_ms, name=name))
        else:
            all_measurements.extend(collect_measurements(gm_result=results,
                                                         time_ms=time_in_ms, name=name))
    return all_measurements


def ordinary_gradient_method(data: Data, v_initial: float):
    size = data.n_max + 1
    v_values = np.full(size, v_initial)
    gm = GradientMethod(data, data.epsilon, size, data.alpha, v_values)
    gm.start()
    return process_gradient_method_results(data, gm, size)


def conditional_gradient_method(data: Data, v_initial: float):
    size = data.n_max + 1
    v_values = np.full(size, v_initial)
    gm = ConditionalGradientMethod(data, data.epsilon, size, data.alpha, v_values)
    gm.start()
    return process_gradient_method_results(data, gm, size)


def modified_gradient_method(data: Data, v_initial: float, with_condition):
    mg = ModifiedGradientMethod(data, v_initial, with_condition)
    modified_results, iterations = mg.run()

    return process_modified_gradient_method_results(data, mg, modified_results, iterations)


def process_modified_gradient_method_results(data: Data, mg, results, iteration_list: list[int]):
    step = (Data.RIGHT_BORDER - Data.LEFT_BORDER) / data.n_max
    gradient_norm = Data.net_norm(mg.modified_gradient[-1], step)

    last_output_data_list = results[-1]

    last_v_values = [item.v_value for item in last_output_data_list]
    last_u_values = [item.u_value for item in last_output_data_list]
    last_x_values = [item.x_value for item in last_output_data_list]

    v_norm = Data.net_norm(last_v_values, step)
    functional = data.method_simpson(last_x_values, last_u_values, step)

    iterations = "+".join(str(i) for i in iteration_list) + "=" + str(sum(iteration_list))

    return {"results": results, "gradient": mg.modified_gradient, "functional_values": mg.modified_functional,
            "last_result": last_output_data_list, "iterations": iterations,
            "gradient_norm": gradient_norm, "v_norm": v_norm, "functional": functional}


def process_gradient_method_results(data: Data, gm, size: int):
    result, functional = collect_all_results(data, size, gm.x_values, gm.u_values, gm.v_values)
    gradient_values = gm.gradient.copy()
    functional_values = gm.functional_list.copy()

    iterations = gm.number_of_iterations
    gradient_norm = Data.net_norm(gm.gradient, gm.step)
    v_norm = Data.net_norm(gm.v_values, gm.step)

    return {"result": result, "gradient": gradient_values, "functional_values": functional_values,
            "iterations": iterations, "gradient_norm": gradient_norm, "v_norm": v_norm, "functional": functional}


def collect_measurements(gm_result=None, modified_results=None, time_ms=None, name=None):

    measurements = []

    if gm_result is not None:
        data = {
            "method": name,
            "result": gm_result["result"],
            "functional_values": gm_result["functional_values"],
            "gradient_values": gm_result["gradient"],
            "iterations": gm_result["iterations"],
            "gradient_norm": gm_result["gradient_norm"],
            "v_norm": gm_result["v_norm"],
            "functional": gm_result["functional"],
            "time_ms": time_ms
        }
        measurements.append(data)

    if modified_results is not None:
        data = {
            "method": name,
            "results_per_level": modified_results["results"],
            "gradients_per_level": modified_results["gradient"],
            "functionals_per_level": modified_results["functional_values"],
            "result": modified_results["last_result"],
            "functional_values": modified_results["functional_values"][-1],
            "functional": modified_results["functional"],
            "gradient_norm": modified_results["gradient_norm"],
            "v_norm": modified_results["v_norm"],
            "iterations": modified_results["iterations"],
            "time_ms": time_ms
        }
        measurements.append(data)

    return measurements


