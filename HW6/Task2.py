class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        person_info = f"Информация о человеке: \nИмя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}"
        return person_info


print(Person('Ivan', 'Ivanov', 43))
