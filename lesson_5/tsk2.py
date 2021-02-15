"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""



with open ('/home/administrator/PycharmProjects/python-base//lesson_5/tsk2.txt') as file:
    lines = 0
    for line in file:
        lines = lines + 1
        words = len (line.split ())
        print (words)

print ('Количество строк в текстовом файле: ', lines)
print ('Количество слов в каждой строке: ', words)