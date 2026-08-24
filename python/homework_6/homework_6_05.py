import random

random_number = random.randint(1, 20)
print("Я загадала число от 1 до 20. У тебя 5 попыток!")
number_of_times = 1
has_won = False
while number_of_times <= 5 :

    try:
        number = int(input(f"Попытка {number_of_times}. Введите число: "))
    except ValueError:
        print("Ошибка: вы ввели не число!")
        continue

    if number == random_number :
        has_won = True
        break
    elif number > random_number :
        print(f"Слишком много! Осталось попыток: {5 - number_of_times} ")
    elif number < random_number :
        print(f"Слишком мало! Осталось попыток: {5 - number_of_times} ")
    number_of_times += 1

if has_won :
    print(f"Ты угадал! Отличная работа.")
else:
    print(f"Вы проиграли! Я загадывала число: {random_number}.")