# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    msg = 1

    def local_function():

        nonlocal msg  # Объявим нелокальную переменную из родительской функции
        msg = 2  # Изменим значение переменной

    local_function()  # Вызовем дочернюю функцию для изменения переменной

    return msg


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')