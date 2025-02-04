import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.filled = False
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]

        if len(sides) != self.sides_count or not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, *([sides[0]] * 12))
        else:
            super().__init__(color, *([1] * 12))

    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка изменения цвета
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)
print(cube1.get_color())  # [222, 35, 130] (не изменился)

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Ошибка (не изменится)
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Периметр (длина окружности)
print(len(circle1))  # 15

# Объём куба
print(cube1.get_volume())  # 216
