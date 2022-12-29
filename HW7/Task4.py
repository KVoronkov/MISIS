class Water:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        else:
            return None


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Earth:
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Dirt:
    answer = 'Получили грязь'


class Storm:
    answer = 'Получили шторм'


class Steam:
    answer = 'Получили пар'


class Lightning:
    answer = 'Получили молнию'


class Dust:
    answer = 'Получили пыль'


class Lava:
    answer = 'Получили лаву'


result = Water() + Air()
print(result.answer)
