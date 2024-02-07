
class NegativeValueError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'NegativeValueError has been raised'

class Rectangle:
    '''
            >>> r1 = Rectangle(5)
            >>> r1.width
            5
            >>> r1.height
            5
            >>> r2 = Rectangle(3, 4)
            >>> r2.width
            3
            >>> r2.height
            4
            >>> r3 = Rectangle(-2)
            Traceback (most recent call last):
            ...
            NegativeValueError: Ширина должна быть положительной, а не -2
            >>> r4 = Rectangle(5, -3)
            Traceback (most recent call last):
            ...
            NegativeValueError: Высота должна быть положительной, а не -3
            '''

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self.width = width
        if height is None:
            self.height = width
        elif height <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        else:
            self.height = height

    def perimeter(self):
        '''
                >>> r1 = Rectangle(5)
                >>> r1.perimeter()
                20
                >>> r2 = Rectangle(3, 4)
                >>> r2.perimeter()
                14
                '''
        return 2 * (self.width + self.height)

    def area(self):
        '''
                >>> r1 = Rectangle(5)
                >>> r1.area()
                25
                >>> r2 = Rectangle(3, 4)
                >>> r2.area()
                12
                '''
        return self.width * self.height

    def __add__(self, other):
        '''
                >>> r1 = Rectangle(5)
                >>> r2 = Rectangle(3, 4)
                >>> r3 = r1 + r2
                >>> r3.width
                8
                >>> r3.height
                6.0
                '''
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        '''
                >>> r1 = Rectangle(5)
                >>> r2 = Rectangle(3, 4)
                >>> r3 = r1 - r2
                >>> r3.width
                2
                >>> r3.height
                2.0
                '''
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"



if __name__ == '__main__':
    import  doctest
    doctest.testmod(verbose=True)

