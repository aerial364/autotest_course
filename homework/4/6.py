# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    num_tuple = [str(i) for i in num_tuple]  # Сконвертируем каждый блок в списке в STRING
    #  Разделим на отдельные блоки HEAD, BODY, TAIL
    #  И тут же объединим каждый блок в один STRING
    head = ''.join(num_tuple[0:3])  # 123
    body = ''.join(num_tuple[3:6])  # 456
    tail = ''.join(num_tuple[6:])  # 7890
    #  Создадим формироватованную строку из блоков
    str_phone = f'({head}) {body}-{tail}'
    return str_phone

# Список из списков. Каждый список из строк. Каждая строка из символа.
# phonebook = [
#     ['Andrew', 'Artyom', 'Arnold'],
#     ['Baba', 'Beba', 'Booba'],
#     ['Caleb', 'Carcass'],
#     ['Drew']]
# for letter in phonebook:
#     for name in letter:
#         for character in name:
#             print(character, end=' ')

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
