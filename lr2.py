class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

quard = Quadrilateral(3, 1, 3, 1)
print(f'Стороны: a={quard.a}, b={quard.b}, c={quard.c}, d={quard.d}, периметр={quard.perimeter()}')

class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
rectang = Rectangle(4, 2)  # Correct: Provide values for a and b
print(f'Стороны: a={rectang.a}, b={rectang.b}, периметр={rectang.perimeter()}')

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
square = Square(5)  # Only one side length is needed
print(f'Сторона: a={square.a}, периметр={square.perimeter()}')