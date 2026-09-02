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

# Выводит уже отсортированный набор в правильном ожидаемом формате.
def pretty_print(sorted_set: list[dict[str, str | float]]):
    print("Топ категорий по выручке:")
    for index, item in enumerate(sorted_set):
        print(f"{index+1}. {item["category"]}: {item["total_sales"]}")


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор, измеряющий и логирующий время выполнения декорируемой функции.

    Обёртка, возвращаемая декоратором, при вызове:
        1. Записывает время начала выполнения с помощью time.perf_counter().
        2. Вызывает исходную функцию с переданными аргументами.
        3. Записывает время окончания выполнения и вычисляет разницу.
        4. Выводит в консоль сообщение с префиксом PERFORMANCE_LOG_PREFIX,
           именем функции и временем выполнения с точностью TIME_DECIMALS знаков.
        5. Возвращает результат, полученный от исходной функции.

    Декоратор сохраняет метаданные исходной функции с помощью functools.wraps.

    Аргументы:
        func (Callable[..., Any]): Декорируемая функция, время выполнения которой
            необходимо измерить и залогировать.

    Возвращает:
        Callable[..., Any]: Функция-обёртка, которая добавляет поведение
            логирования времени выполнения к исходной функции.
    """
    @functools.wraps(func)  # Сохраняет метаданные исходной функции
    def wrapper(*args, **kwargs):
        # 1. Код, выполняемый ДО вызова исходной функции
        start_time = time.perf_counter()

        try:
            # 2. Выполнение исходной функции
            result = func(*args, **kwargs)
            # 3. Возврат результата
            return result

        finally:
            # 4. Код, выполняемый ПОСЛЕ вызова исходной функции
            end_time = time.perf_counter()
            result_time = end_time - start_time
            print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {result_time:.{TIME_DECIMALS}f} сек")


    return wrapper


@performance_logger
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """Сортирует список отчётов о продажах по общей выручке в порядке убывания.

    Аргументы:
        data (list[dict[str, str | float]]): Список словарей, каждый из которых содержит
            ключи 'category' (str) и 'total_sales' (float).

    Возвращает:
        list[dict[str, str | float]]: Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x["total_sales"], reverse=True)


# ТЕСТЫ для наборов
print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
print("--- ТЕСТ 1 ---")
pretty_print(get_sorted_report(first_set))
print("--- ТЕСТ 2 ---")
pretty_print(get_sorted_report(second_set))
print("--- ТЕСТ 3 ---")
pretty_print(get_sorted_report(third_set))