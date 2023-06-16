# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time  # Нужно только для искусственных пауз в тестах

import pytest


def multiply(a, b):  # Функция, которую тестируем
    """Возвращает произведение чисел a и b"""
    result = a * b
    return result


@pytest.mark.usefixtures("time_class")  # Маркируем для использования фикстуры для всего класса
class TestMultiply:

    def test_positive(self):
        assert multiply(2, 2) == 4

    def test_negative(self, time_test):  # Вызываем фикстуру для конкретного теста
        assert multiply(5, -2) == -10
        time.sleep(3)  # Подождём, чтобы накопить разницу во времени
        assert multiply(-11, 3) == -33

    def test_negative_into_positive(self):
        time.sleep(2)  # Подождём, чтобы накопить разницу во времени
        assert multiply(-7, -5) == 35

    def test_multiply_by_zero(self):
        assert multiply(1, 0) == 0
        assert multiply(0, 2) == 0
        assert multiply(0, 0) == 0
