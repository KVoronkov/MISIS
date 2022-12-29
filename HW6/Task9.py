class DecimalCounter:
    def __init__(self):
        self._count = 0

    def get_counter(self):
        return self._count

    def increment(self):
        self._count += 1

    def decrement(self):
        if self._count < 1:
            self._count = 0
            print('Отрицательное значение недопустимо')
        else:
            self._count -= 1


counter = DecimalCounter()
counter.increment()
print(counter.get_counter())
counter.decrement()
print(counter.get_counter())
