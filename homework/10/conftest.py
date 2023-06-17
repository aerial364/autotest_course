import pytest
import datetime


@pytest.fixture(scope="class")  # Будем использовать фикстуру на весь класс
def time_class():
    start_class = datetime.datetime.now().strftime('%H:%M:%S')  # Запомним время начала
    yield  # Подождём, пока все тесты класса пробегут
    end_class = datetime.datetime.now().strftime('%H:%M:%S')  # Получим время конца
    print(f'\nВремя начала выполнения класса с тестами: {start_class}')  # И выведем это время
    print(f'Время окончания выполнения класса с тестами: {end_class}')


@pytest.fixture()
def time_test(request):  # Укажем request в аргументе, чтобы получить информацию о функции
    test_function_name = request.function.__name__  # Получим имя функции, которая использует фикстуру
    start_test = datetime.datetime.now()  # Запомним время начала теста
    yield  # Подождём, пока тест закончит выполнение
    end_test = datetime.datetime.now()  # Запомним время конца теста
    time_length = end_test - start_test  # Вычислим разницу
    formated_time = time_length.total_seconds()  # Приведём к секундам
    print(f'\nВремя выполнения теста {test_function_name}: {formated_time} секунд\n')  # Выведем имя и время теста
