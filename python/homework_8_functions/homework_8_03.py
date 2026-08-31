from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(movie_title:str, days_overdue:Any, fine_rate:float) -> tuple[float, float] | None:
    """Calculates the overdue fine and return index for a rented movie.

        The function handles common input errors such as
        division by zero, invalid numeric strings, and unsupported data types.

        Args:
            movie_title (str): The title of the movie.
            days_overdue (Any): The number of days the movie is overdue. Can be any type convertible to float; otherwise an
                error is handled.
            fine_rate (float): fine amount per day.

        Returns:
            tuple[float, float] | None: return index and the total fine if the calculation succeeds,
                None if an error occurs.
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
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': float() argument must be a string or a real number, not '{type(days_overdue)}'")
    finally:
        print("--- Проверка транзакции возврата завершена ---")

# 1. «Matrix»: 5 дней, 1.5$ за день (Успешный расчет)
result = calculate_overdue_fine('Matrix', '5', 1.5)

# 2. «Inception»: "пять" дней, 2.0$ за день (Ошибка значения / ValueError)
result = calculate_overdue_fine('Inception', 'пять', 2.0)

# 3. «Avatar»: 0 дней, 2.5$ за день (Деление на ноль / ZeroDivisionError)
result = calculate_overdue_fine('Avatar','0', 2.5)

# 4. «Interstellar»: [3,] (список), 3.0$ за день (Ошибка типа / TypeError)
result = calculate_overdue_fine('Interstellar', [3,], 3.0)
