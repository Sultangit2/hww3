class Calculator:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __add__(self, other):
        return self.x + other.y

    def __sub__(self, other):
        return self.x - other.y

    def __mul__(self, other):
        return self.x * other.y

    def __truediv__(self, other):
        return self.x / other.y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"