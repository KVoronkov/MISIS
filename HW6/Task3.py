from Task1 import Person


class GreetPerson(Person):
    def greet(self) -> None:
        print(
            f"Привет! Меня зовут {self.last_name} {self.first_name}, мне {self.age} лет")


test = GreetPerson('Ivan', 'Ivanov', 13)
test.greet()
