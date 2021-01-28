"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль."""



def calc_data (*args):
    try:
        first = int (input ('Введите первое число: '))
        second = int (input ('Введите второе число: '))
        result = first / second
    except ZeroDivisionError as zero:
        return "Делить на ноль нельзя!!!!"
    return result

print(f'Результат =  {calc_data()}')