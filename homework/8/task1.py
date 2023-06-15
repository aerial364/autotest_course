# Напишите функцию treatment_sum, использовав конструкцию try/except
# На вход поступает кортеж our_tuple

# Если в кортеже 2 элемента и их можно сложить,
# то функция возвращает получившийся результат

# Если в кортеже 2 элемента и их нельзя сложить,
# то функция обрабатывает исключение и возвращает строку 'Нельзя сложить эти данные'

# Если в кортеже меньше двух элементов,
# то функция обрабатывает исключение и возвращает строку 'Недостаточно данных'

# Если в кортеже больше двух элементов,
# то функция генерирует исключение Exception с текстом 'Много данных'


import unittest  # Не удалять


# Здесь пишем код
def treatment_sum(our_tuple):
    """
    Возвращает сумму 2 элементов кортежа
    :param our_tuple: tuple
    :return: output: int если нет ошибок, string, если были ошибки
    """
    output = None
    try:  # Пробуем сложить 2 первых элемента
        output = our_tuple[0] + our_tuple[1]
    except TypeError:  # Данные не верного типа
        output = 'Нельзя сложить эти данные'
        return output
    except IndexError:  # Получили только 1 аргумент
        output = 'Недостаточно данных'
        return output
    if len(our_tuple) > 2:  # В кортеже больше 2 элементов
        raise Exception("Много данных")
    else:
        return output


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, 5), (3, '7'), (3,), (), ('23', '32')]

        test_data = [8, 'Нельзя сложить эти данные', 'Недостаточно данных', 'Недостаточно данных', '2332']

        for i, d in enumerate(data):
            assert treatment_sum(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
            print(f'Тестовый набор {d} прошёл проверку')

        with self.assertRaises(Exception):
            treatment_sum((3, 4, 5))
        try:
            treatment_sum((3, 4, 5))
        except Exception as e:
            assert e.args[0] == 'Много данных', 'Исключение имеет неправильный текст'
        print('Всё ок')


if __name__ == '__main__':
    unittest.main()
