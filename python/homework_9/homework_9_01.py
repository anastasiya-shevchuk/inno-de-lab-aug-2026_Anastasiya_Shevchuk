class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if type(new_score) != int:
            raise TypeError (f"Expected value of type int, got {type(new_score)}")
        if new_score < 0:
            raise ValueError ("The score shouldn't be less than 0!")
        self.__score = new_score


    def do_homework(self):
        """Increases score by 1"""
        self.score += 1

    def miss_homework(self):
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self):
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self):
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        return self.score >= self.passing_grade

if __name__ == "__main__":
    print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")
    # 1. Создание стажера с начальным баллом 9 и проходным баллом 10
    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)
    # 2. Выполнение домашнего задания и проверка статуса
    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
    # 3. Пропуск лекции и проверка статуса
    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")
    # 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")