# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    letters_str = 'qwertyuiopasdfghjklzxcvbnm'  # Список букв, из которых будем их брать
    while True:  # Нужно для того, чтобы генерировалась новая пара при каждом обращении к функции
        length1 = random.randint(1, 15)  # Сгенерируем длину каждого слова
        length2 = random.randint(1, 15)
        line1 = ''  # Переменные, куда будем записывать слова
        line2 = ''
        while length1 > 0:
            line1 += random.choice(letters_str)  # Прибавляем к слову рандомные буквы
            length1 -= 1  # И уменьшаем счётчик длины на единицу, чтобы закончить цикл на 0
        while length2 > 0:
            line2 += random.choice(letters_str)
            length2 -= 1
        lines = f'{line1} {line2}'  # Собираем предложение из 2 слов
        yield lines


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
