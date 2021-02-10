"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""



lessons = {}

def all_hours (lessons):
    result = 0

    for subject in lessons.split () [1:]:
        i = '0'

        for count in range (len (subject)):
            if subject [count].isdigit ():
                i = ''.join (i + subject [count])
            else:
                continue
        result += int (i)
    return result

with open('/home/administrator/PycharmProjects/python-base//lesson_5/tsk6.txt', encoding='utf-8') as f_obj:
    f_obj.seek (0)
    my_list = {}
    for line in f_obj:
        my_list [line.split()[0]] = all_hours (line)

    print (my_list)