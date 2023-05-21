# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:
    def __init__(self, name: str, age: int, *department: list):
        self.name = name
        self.age = age
        self. department = department

    def short_name(self):
        """
        Разбиваем строку на 2 элемента по пробелу
        Выводим укороченное ФИ через форматированную строку
        :return:
        """
        splitted = list(self.name.split(' '))
        shortened = f'{splitted[1]} {splitted[0][0]}.'
        return shortened

    def path_deps(self):
        """
        Если путь состоит из одного элемента - вернём его
        Если путь состоит из 2+ элементов - будем записывать в строку название отдела
        Если мы записали НЕ последний элемент - добавим в строку стрелку ' --> '
        :return:
        path: string
        """
        path = ''
        if len(self.department) == 1:
            path = self.department[0]
        else:
            for dep in self.department:
                path += dep
                if len(self.department) - 1 > self.department.index(dep):
                    path += f' --> '
                else:
                    break
        return path

    def new_salary(self):
        """
        Создадим словарь и посчитаем букву и общее количество её повторений в каждом из отделов
        Отсортируем справочник по значению в порядке возрастания
        Найдём три наиболее встречающиеся буквы через popitem()
        Вычислим salary по формуле
        :return:
        salary: int
        """
        dict1 = {}
        for dep in self.department:
            for char in dep:
                if char not in dict1.keys():
                    dict1.update({char: 1})
                else:
                    a = dict1.get(char)
                    dict1.update({char: a + 1})

        dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}

        top1 = dict1.popitem()[1]
        top2 = dict1.popitem()[1]
        top3 = dict1.popitem()[1]

        salary = 1337 * self.age * (top1 + top2 + top3)

        return salary

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')