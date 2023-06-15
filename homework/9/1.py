# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

# Подсчитаем количество строк в файле
with open(r'test_file/task1_data.txt', encoding='utf-8') as f:
    count_lines = sum(1 for _ in f)

source = open(r'test_file/task1_data.txt', encoding='utf-8')
output = open(r'test_file/task1_answer.txt', mode='a', encoding='utf-8')
line = None  # Сюда будем записывать строку из оригинала, для работы с ней
format_line = str()  # Сюда будем записывать отформатированную строку без цифр

while count_lines != 0:
    line = (source.readline())  # Берём строку из файла
    for symbol in line:  # Перебираем каждый символ
        if symbol.isdigit() is False:  # Если символ НЕ число
            format_line += symbol  # Добавим его к новой строке
    output.writelines(format_line)  # Запишем отформатированную в новый файл
    format_line = str()  # Сбросим значение строки до пустого
    count_lines -= 1  # Уменьшим счётчик строк, которые осталось пройти

source.close()  # Закроем файлы
output.close()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')