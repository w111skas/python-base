"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов."""



def my_func (*args):
    one = int (input ('Введите первое значение: '))
    two = int (input ('Введите второе значение: '))
    three = int (input ('Введите третье значение: '))
    if one >= two and two >= three:
        return one + two
    elif one > two and one < three:
        return one + three
    else:
        return two + three

print (f'Сумма двух наибольших значений равна: {my_func()}')
