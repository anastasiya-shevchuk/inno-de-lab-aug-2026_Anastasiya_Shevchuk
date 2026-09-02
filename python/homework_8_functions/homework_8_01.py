MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Рассчитывает параметры партии для управления.

    Args:
        quantity (int): количество дисков, арендованных в этой партии.
        rental_rate (float): стоимость аренды одного диска в этой партии.
        discount (float, optional): размер скидки. По умолчанию 0.0 (без скидки).

    Returns:
        tuple[float, bool]: кортеж с рассчитанными параметрами партии:
            - final_sum (float): итоговая сумма за партию (с учетом скидки).
            - is_limit_exceeded (bool): True, если final_sum превысила лимит,
            установленный в MAX_RENTAL_BATCH_LIMIT, иначе False.
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

if __name__ == "__main__":
    # тестовые данные для партий
    batches = [
        ("Academy Dinosaur", 30, 2.99, 0.0),
        ("Affair Prejudice", 40, 4.99, 0.1),
        ("Agent Truman", 10, 1.99, 0.0),
        ("African Egg", 50, 3.50, 0.2),
    ]

    print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

    name, qty, rate, disc = batches[0]

    # пример с позиционными аргументами
    total, exceeded = calculate_rental_batch(qty, rate, disc)

    print(f"Партия 1 ({name}): Сумма {total}$. Превышение лимита: {exceeded}")

    # примеры с именованными аргументами
    i = 2
    for batch in batches[1:]:
        name, qty, rate, disc = batch
        total, exceeded = calculate_rental_batch(
            rental_rate=rate,
            quantity=qty,
            discount=disc
        )
        print(f"Партия {i} ({name}): Сумма {total}$. Превышение лимита: {exceeded}")
        i += 1