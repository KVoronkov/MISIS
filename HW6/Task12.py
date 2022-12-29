class Grass:
    def __init__(self, nutrition) -> None:
        self.nutrition = nutrition


class Animal:
    def __init__(self) -> None:
        self.hunger = 10

    def __str__(self) -> str:
        if self.hunger < 2:
            print('Необходимо покормить')
        else:
            print('Кормить не надо')

    def eat(self, grass):
        if self.hunger <= 2:
            self.hunger += grass.nutrition
            print(f'Животное сыто на {self.hunger}')

    def add_hunger(self):
        self.hunger -= 3


animal = Animal()
grass = Grass(2)
animal.add_hunger()
animal.add_hunger()
animal.add_hunger()
animal
animal.eat(grass)
animal
