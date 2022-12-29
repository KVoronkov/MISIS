class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, left_low: Point, right_top: Point):
        self.left_low = left_low
        self.right_top = right_top

        self.side_len = self.right_top.y - self.left_low.y
        self.top_len = self.right_top.x - self.left_low.x

    def contains(self, point: Point):

        if point.x > self.left_low.x and point.x < self.right_top.x and point.y > self.left_low.y and point.y < self.right_top.y:
            print('Точка лежит внутри прямоугольника')
            return True
        elif point.x == self.left_low.x or point.x == self.right_top.x or point.y == self.left_low.y or point.y == self.right_top.y:
            print('Точка лежит на грани прямоугольника')
            return True
        else:
            print('Точка не лежит внутри прямоугольника')
            return False


left_low = Point(0, 0)
right_top = Point(7, 3)
rectangle = Rectangle(left_low, right_top)
rectangle.contains(Point(2, 3))
