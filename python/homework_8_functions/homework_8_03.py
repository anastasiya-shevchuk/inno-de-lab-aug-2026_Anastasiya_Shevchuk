from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(movie_title: str, days_overdue: Any, fine_rate: float) -> tuple[float, float] | None:
    """Рассчитывает штраф за просрочку и индекс возврата для арендованного фильма.

    Функция обрабатывает распространённые ошибки ввода, такие как
    деление на ноль, недопустимые числовые строки и неподдерживаемые типы данных.

    Аргументы:
        movie_title (str): Название фильма.
        days_overdue (Any): Количество дней просрочки. Может быть любым типом,
            преобразуемым в float; в противном случае обрабатывается ошибка.
        fine_rate (float): Размер штрафа за день.

    Возвращает:
        tuple[float, float] | None: Индекс возврата и общая сумма штрафа в случае
            успешного вычисления, None в случае возникновения ошибки.
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{movie_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")

        return return_index, total_fine
    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': float division by zero")
    except ValueError:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': could not convert string to float: '{days_overdue}'")
    except TypeError:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': float() argument must be a string or a real number, not '{type(days_overdue).__name__}'")
    finally:
        print("--- Проверка транзакции возврата завершена ---")

# 1. «Matrix»: 5 дней, 1.5$ за день (Успешный расчет)
calculate_overdue_fine('Matrix', '5', 1.5)

# 2. «Inception»: "пять" дней, 2.0$ за день (Ошибка значения / ValueError)
calculate_overdue_fine('Inception', 'пять', 2.0)

# 3. «Avatar»: 0 дней, 2.5$ за день (Деление на ноль / ZeroDivisionError)
calculate_overdue_fine('Avatar', '0', 2.5)

# 4. «Interstellar»: [3,] (список), 3.0$ за день (Ошибка типа / TypeError)
calculate_overdue_fine('Interstellar', [3,], 3.0)