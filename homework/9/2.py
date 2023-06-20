# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime

# Здесь пишем код


def func_log(file_log='log.txt'):
    def wrapper(func):
        def inner():
            res = func()  # Вызов функции
            now = datetime.datetime.now().strftime('%d.%m %H:%M:%S')  # Получим текущее время
            inner.__name__ = func.__name__  # Запишем в inner имя вызываемой функции
            inner.__doc__ = func.__doc__  # Запишем в inner документацию вызываемой функции
            with open(file_log, mode='a', encoding='utf-8') as f:  # Откроем файл
                f.writelines(f'{func.__name__} вызвана {now}\n')  # Запишем вызов функции
                f.close()  # Закроем файл
            return res
        return inner
    return wrapper


@func_log(file_log='log.txt')
def func1():
    """Описание функции №1 с декоратором"""
    print("Первая функция")


@func_log(file_log='func2.txt')
def func2():
    print('Вторая функция')


func1()  # Вызов первой функции с декоратором с записью в log.txt
time.sleep(1)
func2()  # Вызов первой функции с декоратором с записью в func2.txt
time.sleep(1)
func1()  # Вызов первой функции с декоратором с записью в log.txt

help(func1)  # Возвращаем информацию о функции 1 с декоратором (Будет работать даже без декоратора)
