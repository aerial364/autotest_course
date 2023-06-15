# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
source = open(r'test_file/task_3.txt')
list_file = source.readlines()  # Запишем каждую строку как отдельный элемент в списке
list_of_sums = list()  # Создадим список, в который будем помещать суммы чеков
source.close()  # Закроем файл, т.к. больше не работаем с ним

current_line = str()  # Текущая строка в списке покупок
receipt = int()  # Сумма чека

for i in range(len(list_file)):  # Будем прогонять по всему списку покупок
    current_line = list_file[i]  # Запишем текущую строку
    if current_line != '\n':  # Если это не пустая строка, то
        receipt += int(current_line)  # Прибавим число к сумме чека
    else:  # А если наткнулись на пустую строку
        list_of_sums.append(receipt)  # Добавим сумму чека в список сумм чеков
        receipt = 0  # Обнулим переменную, чтобы считать следующий чек

list_of_sums.sort(reverse=True)  # Отсортируем список от больших сумм к меньшим
three_most_expensive_purchases = sum(list_of_sums[:3])  # Возьмем сумму первых трёх элементов
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
