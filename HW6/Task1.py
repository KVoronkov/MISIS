class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


test = Person('Ivan', 'Ivanov', 43)
print(test.first_name, test.last_name, test.age)
