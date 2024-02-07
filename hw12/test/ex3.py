class Rectangle:
    def __init__(self, width, height=None) -> None:
        self.width = width
        self.height = height if height else width

    def area(self):
        return int(self.width * self.height)

    def perimeter(self):
        return int(2 * (self.width + self.height))

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other):

        return Rectangle(self.width - other.width, self.height - other.height)

    def __lt__(self, other):

        if self.perimeter() < other.perimeter():
            return True
        else:
            return False

    def __eq__(self, other):

        if self.area() == other.area():
            return True
        else:
            return False

    def __le__(self, other):

        if self.area() <= other.area():
            return True
        else:
            return False

    def __str__(self):

        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")