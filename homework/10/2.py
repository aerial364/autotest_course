# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_divide_positive_by_positive():
    assert all_division(10, 5) == 2


@pytest.mark.acceptance
def test_divide_positive_by_negative():
    assert all_division(6, -2) == -3


@pytest.mark.acceptance
def test_divide_with_float_result():
    assert all_division(7, 2) == 3.5


@pytest.mark.acceptance
def test_divide_by_float_number():
    assert all_division(7, 2.5) == 2.8


@pytest.mark.acceptance
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(10, 0)
