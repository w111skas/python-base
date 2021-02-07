"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""



with open ('/home/administrator/PycharmProjects/python-base//lesson_5/tsk3.txt', 'r') as tsk3:
    sal = []
    staff = []
    result = tsk3.read ().split ('\n')
    for i in result:
        i = i.split ()
        if int (i[1]) < 20000:
           staff.append (i[0])
        sal.append (i[1])
print (f'Оклад меньше 20.000 рублей: {staff},\n Средний оклад равен {sum (map (int, sal)) / len (sal)}')