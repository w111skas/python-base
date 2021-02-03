"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_tsk4 = []

with open ('/home/administrator/PycharmProjects/python-base//lesson_5/tsk4.txt') as tsk4:
    for result in tsk4:
        result = result.split (' ', 1)
        print ('Английские числительные: ', result)
        new_tsk4.append (rus_dict [result[0]] + result [1])

print ('\nРусские числительные: ', new_tsk4)

with open ('tsk4_new.txt', 'w', encoding = 'utf-8') as tsk4_new:
    tsk4_new.writelines(new_tsk4)