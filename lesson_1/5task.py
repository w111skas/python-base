gain = float (input ('Введите размер выручки фирмы: '))
cost = float (input ('Введите размер издержек фирмы: '))
if gain > cost:
    rate = gain - cost
    print ('Размер ВЫРУЧКИ больше размера издержек на ', rate, 'рублей')

    rates = gain / rate
    print ('Соотношение прибыли к вашей выручке составляет ', rates)

    people = int (input ('Введите численность Вашей фирмы: '))
    salary = rate / people
    print ('Средняя зарплата одного сотрудника в Вашей фирме с учетом издержек составляет ', salary, 'рублей')

if gain < cost:
    costs = cost - gain

    print ('Размер ИЗДЕРЖЕК больше размера выручки фирмы на ', costs,'рублей')
