MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
        Calculates the rental batch parameters for management.

        Args:
            quantity (int): how many discs were rented this batch.
            rental_rate (float): how much one disc cost this batch.
            discount (float, optional): discount rate. Defaults to 0.0 (no discount).

        Returns:
            tuple[float, bool]: tuple for calculated batch parameters:
                - final_sum (float): total sum for the batch (including discount).
                - is_limit_exceeded (bool): True if final_sum exceeded the limit set in MAX_RENTAL_BATCH_LIMIT (False otherwise).
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

if __name__ == "__main__":
    # batches test data
    batches = [
        ("Academy Dinosaur", 30, 2.99, 0.0),
        ("Affair Prejudice", 40, 4.99, 0.1),
        ("Agent Truman", 10, 1.99, 0.0),
        ("African Egg", 50, 3.50, 0.2),
    ]

    print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

    name, qty, rate, disc = batches[0]

    # positional args example
    total, exceeded = calculate_rental_batch(qty, rate, disc)

    print(f"Партия 1 ({name}): Сумма {total}$. Превышение лимита: {exceeded}")

    # named args examples
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

