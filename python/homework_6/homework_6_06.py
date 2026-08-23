number_input = input("Введите первое число: ")

try:
    number_1 = float(number_input)
except ValueError:
    print("Ошибка: вы ввели не число!")
    exit()


number_input = input("Введите второе число: ")
try:
    number_2 = float(number_input)
except ValueError:
    print("Ошибка: вы ввели не число!")
    exit()

operator = input("Введите оператор (+, -, *, /): ")

if operator == "+":
    print(f"{number_1} {operator} {number_2} =", number_1 + number_2)
elif operator == "-":
    print(f"{number_1} {operator} {number_2} =", number_1 - number_2)
elif operator == "*":
    print(f"{number_1} {operator} {number_2} =", number_1 * number_2)
elif operator == "/":
    if number_2 == 0:
        print("Деление на 0 запрещено. Попробуй еще раз.")
        exit()
    print(f"{number_1} {operator} {number_2} =", number_1 / number_2)
else:
    print("Введите корректное значение оператора")
