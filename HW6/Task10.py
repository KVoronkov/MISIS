class Clock:
    def __init__(self, hours, minutes, sec) -> None:
        if hours > 23 or hours < 0:
            raise ValueError('Некорректно заданы часы')
        if minutes > 59 or minutes < 0:
            raise ValueError('Некорректно заданы минуты')
        if sec > 59 or sec < 0:
            raise ValueError('Некорректно заданы секунды')

        self.hours = hours
        self.minutes = minutes
        self.sec = sec

    def add_hour(self):
        self.hours = (self.hours + 1) % 24

    def add_minute(self):
        self.minutes = (self.minutes + 1) % 60
        if self.minutes == 0:
            self.hours = (self.hours + 1) % 24

    def add_sec(self):
        self.sec = (self.sec + 1) % 60
        if self.sec == 0:
            self.minutes = (self.minutes + 1) % 60
            if self.minutes == 0:
                self.hours = (self.hours + 1) % 24

    def __str__(self) -> str:
        return 'Текущее время: {:02d}:{:02d}:{:02d}'.format(self.hours, self.minutes, self.sec)


clock = Clock(22, 58, 58)
print(clock)
clock.add_sec()
print(clock)
clock.add_minute()
print(clock)
clock.add_hour()
print(clock)
clock.add_sec()
print(clock)
