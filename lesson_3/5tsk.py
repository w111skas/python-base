"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу."""



def enter_number (date):
    result = 0
    for number in date.split():
        if number == 'Q':
            return result, True
        try:
            result += int (number)
        except ValueError:
            continue
    return result, False

result = 0
is_end = False

while True:
    string = input ("Введите числа через пробел или символ 'Q' для завершения: ")
    current_summa, is_end = enter_number (string)
    result += current_summa

    print (f"Общая сумма составляет: {result}")

    if is_end:
        break

print ('Программа закрыта')