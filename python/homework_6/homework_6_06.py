def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Ошибка: вы ввели не число!")

number_1 = get_number("Введите первое число: ")
number_2 = get_number("Введите второе число: ")


def get_operator(msg):
    allowed_operators = {"+", "-", "*", "/"}
    while True:
        operator = input(msg)
        if operator in allowed_operators:
            return operator
        else:
            print("Ошибка. Введите один из разрешенных операторов: +, -, *, /")

operator = get_operator("Введите оператор (+, -, *, /): ")

if operator == "+":
    print(f"{number_1} {operator} {number_2} =", number_1 + number_2)
elif operator == "-":
    print(f"{number_1} {operator} {number_2} =", number_1 - number_2)
elif operator == "*":
    print(f"{number_1} {operator} {number_2} =", number_1 * number_2)
elif operator == "/":
    while True:
        try:
            print(f"{number_1} {operator} {number_2} =", number_1 / number_2)
            break
        except ZeroDivisionError:
            print("Деление на 0 запрещено.")
            number_2 = get_number("Введите второе число еще раз: ")





