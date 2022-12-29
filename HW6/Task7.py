class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, left_low: Point, right_top: Point) -> None:
        self.left_low = left_low
        self.right_top = right_top

        self.side_len = self.right_top.y - self.left_low.y
        self.top_len = self.right_top.x - self.left_low.x

        print(f'Периметр прямоугольника: {2*(self.side_len + self.top_len)}')
        print(f'Площадь прямоугольника: {self.top_len * self.side_len}')


left_low = Point(0, 0)
right_top = Point(7, 3)
rectangle = Rectangle(left_low, right_top)
