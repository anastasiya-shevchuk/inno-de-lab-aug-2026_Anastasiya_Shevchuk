import functools
import time
from typing import Callable, Any

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

# Набор 1 (Стандартный)
first_set = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]
# Набор 2 (С одинаковой выручкой)
second_set = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]
# Набор 3 (Единичный элемент)
third_set = [
    {"category": "Drama", "total_sales": 500.00}
]

# Prints an already sorted set in a correct expected format.
def pretty_print(sorted_set: list[dict[str, str | float]]):
    print("Топ категорий по выручке:")
    for index, item in enumerate(sorted_set):
        print(f"{index+1}. {item["category"]}: {item["total_sales"]}")


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that logs the execution time of the decorated function.

    Wrapper to measure the execution time of the decorated function and prints it.

    Args:
        func (Callable[..., Any]): The function to be wrapped and measured.

    Returns:
        Callable[..., Any]: The wrapper function.
    """
    @functools.wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        # 1. Code to run BEFORE the original function
        start_time = time.perf_counter()

        # 2. Execute the original function
        result = func(*args, **kwargs)

        # 3. Code to run AFTER the original function
        end_time = time.perf_counter()

        result_time = end_time - start_time

        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {result_time:.{TIME_DECIMALS}f} сек")

        # 4. Return the result
        return result
    return wrapper


@performance_logger
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """Sorts a list of sales reports by total sales in descending order.

    Args:
        data (list[dict[str, str | float]]): A list of dictionaries, each contains a
            'category' (str) and a 'total_sales' (float) keys.

    Returns:
        list[dict[str, str | float]]: The sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x["total_sales"], reverse=True)


# TESTS for sets
print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
print("--- ТЕСТ 1 ---")
pretty_print(get_sorted_report(first_set))
print("--- ТЕСТ 2 ---")
pretty_print(get_sorted_report(second_set))
print("--- ТЕСТ 3 ---")
pretty_print(get_sorted_report(third_set))