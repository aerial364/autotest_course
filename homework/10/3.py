# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result',
                         [pytest.param(10, 5, 2, marks=pytest.mark.smoke),
                          pytest.param(6, -2, -3, marks=pytest.mark.acceptance),
                          pytest.param(7, 2, 3.5, marks=pytest.mark.acceptance),
                          pytest.param(7, 2.5, 2.8, marks=pytest.mark.skip(reason='Скип до 23.7100 по ошибке')),
                          pytest.param(10, 0, None, marks=pytest.mark.acceptance)])
def test_division(a, b, result):
    try:  # Используем try, т.к. ожидаем тест на ошибку при делении на 0
        assert all_division(a, b) == result
    except ZeroDivisionError:
        assert result is None  # Тест будет пройден, если упадёт ZeroDivisionError с результатом = None
