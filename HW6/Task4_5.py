from Task1 import Person
import random
from statistics import mean


class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, grades: list[int]):
        super().__init__(first_name, last_name, age)
        self.grades = grades

    def __str__(self) -> str:
        return f'Имя: {self.first_name}, Фамилия: {self.last_name}, Возраст: {self.age}, Средний балл: {self.get_mean_grade()}'

    # Задание 5 (средний бал)
    def get_average_grade(self) -> float:
        return mean(self.grades)


# Задание 4
STUDENTS_N = 5
GRADES_N = 10
grades = list(range(2, 6))
grades_list = [[random.choice(grades) for _ in range(GRADES_N)]
               for _ in range(STUDENTS_N)]
students = [Student(
    f'First_Name_{i}', f'Last_Name_{i}', 10+i, student_grades) for i, student_grades in enumerate(grades_list)]

# Задание 5
sorted_students = sorted(
    students, key=lambda person: person.get_average_grade(), reverse=True)

for student in sorted_students:
    print(student.first_name, student.last_name, student.get_average_grade())
