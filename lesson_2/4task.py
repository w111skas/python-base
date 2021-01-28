"""Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове."""



line = input ("Введите несколько слов: ")
word = []
string = 1

for word_string in range (line.count(' ') + 1):
    word = line.split ()

    if len (str (word)) <= 10:
        print (f" {string} {word [word_string]}")
        string += 1

    else:
        print(f" {string} {word [word_string] [0:10]}")
        string += 1