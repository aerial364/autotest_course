# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код
from math import sqrt

class Segment:
    def __init__(self, dot1: tuple, dot2: tuple):
        self.dot1 = dot1
        self.dot2 = dot2

    def length(self):
        return round((sqrt((self.dot1[0] - self.dot2[0]) ** 2 + (self.dot1[1] - self.dot2[1]) ** 2)), 2)

    def x_axis_intersection(self):
        if (self.dot1[1] <= 0 <= self.dot2[1]) or (self.dot1[1] >= 0 >= self.dot2[1]):
            return True
        else:
            return False

    def y_axis_intersection(self):
        if (self.dot1[0] <= 0 <= self.dot2[0]) or (self.dot1[0] >= 0 >= self.dot2[0]):
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection,

        Segment((-2, 2), (3, 2)).y_axis_intersection,  # Доп. кейс - отрезок параллелен X и пересекает Y
        Segment((-2, 2), (3, 2)).x_axis_intersection,  # Доп. кейс - отрезок параллелен X и пересекает Y
        Segment((2, 5), (2, -3)).y_axis_intersection,  # Доп. кейс - отрезок параллелен Y и пересекает X
        Segment((2, 5), (2, -3)).x_axis_intersection,  # Доп. кейс - отрезок параллелен Y и пересекает X

        Segment((-10, -1), (-1, -1)).y_axis_intersection,  # Доп. кейс - отрезок параллелен X и НЕ пересекает Y
        Segment((-10, -1), (-1, -1)).x_axis_intersection,  # Доп. кейс - отрезок параллелен X и НЕ пересекает Y
        Segment((-1, -1), (-1, -3)).y_axis_intersection,  # Доп. кейс - отрезок параллелен Y и НЕ пересекает X
        Segment((-1, -1), (-1, -3)).x_axis_intersection,  # Доп. кейс - отрезок параллелен Y и НЕ пересекает X

        Segment((0, 3), (0, 1)).y_axis_intersection,  # Доп. кейс - Отрезок на оси Y и НЕ пересекает X
        Segment((0, 3), (0, 1)).x_axis_intersection,  # Доп. кейс - Отрезок на оси Y и НЕ пересекает X
        Segment((-3, 0), (3, 0)).y_axis_intersection,  # Доп. кейс - Отрезок на оси X и пересекает Y
        Segment((-3, 0), (3, 0)).x_axis_intersection,  # Доп. кейс - Отрезок на оси X и пересекает Y

        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True,
             True, False, False, True,
             False, False, False, False,
             True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')