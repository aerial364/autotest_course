# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:
    def __init__(self, symbols: str):
        self.symbols = symbols

    def from_roman(self):
        """
        Запишем в dictionary арабское значение каждого символа
        Создадим две переменные, определяющие накапливаемое арабское число и прошлое число
        Проходя данную римскую строку с конца, будем делать:
            Если текущий символ больше или равен прошлому - прибавляем значение к value
            Если текущий символ меньше прошлого - вычтем его из накопленного значения
        :return:
        value: int (Арабское число)
        """
        dict_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0
        last_digit_value = 0

        for roman in self.symbols[::-1]:
            digit_value = dict_values[roman]

            if digit_value >= last_digit_value:
                value += digit_value
                last_digit_value = digit_value
            else:
                value -= digit_value

        return value

    def is_palindrome(self):
        """
        Зовём метод from_roman для числа и переводим его в string
        Затем сверяем что строка равне себе, если читается задом-наперёд
        :return:
        True, если строка = палиндром
        False, если строка = не палиндром
        """
        a = str(self.from_roman())
        if a == a[::-1]:
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]

test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
