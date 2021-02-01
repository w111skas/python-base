"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict."""



number = int (input ('Введите месяц от 1 до 12: '))

years = [ 'Зима', 'Весна', 'Лето', 'Осень']
seasons = {1: 'Это зимний месяц', 2: 'Это весенний месяц', 3: 'Это летний месяц', 4: 'Это осенний месяц'}

if number == 12 or number == 1 or number == 2:
        print (seasons.get (1))
        print (years [0])

elif number == 3 or number == 4 or number == 5:
    print (seasons.get (2))
    print (years [1])

elif number == 6 or number == 7 or number == 8:
    print (seasons.get (3))
    print (years [2])

elif number == 9 or number == 10 or number == 11:
    print (seasons.get (4))
    print (years [3])

else:
        print ("Такого месяца не существует!!! ")
