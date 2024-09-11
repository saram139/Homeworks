import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        if len(sides) != self.sides_count:
            self.__sides = [1 * self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self):
        for i in self.__sides:
            return isinstance(i, int) and i > 0 and len(self.__sides) == self.sides_count

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides():
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)
        self.__radius = self.__len__() / (2 * math.pi)

    def get_square(self):
        return (self.__radius ** 2) * math.pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)

    def get_square(self):
        p = len(self) / 2
        return math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1 * self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
triangle1 = Triangle((35, 100, 170), 10, 9, 8)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
triangle1.set_color(85, 120, 255)  # Изменится
print(triangle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
triangle1.set_sides(3, 4, 5)
print(triangle1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка площади треугольника:
print(triangle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())
