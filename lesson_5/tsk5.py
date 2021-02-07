"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""



def summary ():
    try:
        with open ('tsk5.txt', 'w', encoding = 'utf-8') as tsk5:
            number = input ('Введите числа через пробел: \n')
            tsk5.writelines (number)
            numb = number.split ()
            print (sum (map (int, numb)))

    except ValueError:
        print('Вы ввели не число!!!')

print (summary())