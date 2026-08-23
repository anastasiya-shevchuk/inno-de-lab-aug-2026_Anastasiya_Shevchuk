import random

random_number = random.randint(1, 20)
number_of_times = 0
print("Я загадала число от 1 до 20. У тебя 5 попыток!")
number_of_times += 1
hasWon = 0
while number_of_times <= 5 :
    number = int(input(f"Попытка {number_of_times}. Введите число: "))
    if number == random_number :
        hasWon = 1
        break
    elif number > random_number :
        print(f"Слишком много! Осталось попыток: {5 - number_of_times} ")
    elif number < random_number :
        print(f"Слишком мало! Осталось попыток: {5 - number_of_times} ")
    number_of_times += 1

if hasWon == 1 :
    print(f"Ты угадал! Отличная работа.")
else:
    print(f"Вы проиграли! Я загадывала число: {random_number}.")