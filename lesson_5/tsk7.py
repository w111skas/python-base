"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""


import json

profit_company = {}
unprofit_company = {}
general_profit = 0

with open ('/home/administrator/PycharmProjects/python-base//lesson_5/tsk7.txt', 'r', encoding = 'utf-8') as tsk7:
    for line in tsk7:
        company_name, revenue, expenses = line.split ()
        revenue = int (revenue)
        expenses = int (expenses)
        profit = revenue - expenses
        if profit >= 0:
            profit_company [company_name] = profit
            general_profit += profit
        else:
            unprofit_company [company_name] = profit

profit_company_count = len (profit_company)
result = [
    profit_company,
    {'Общая прибыль': general_profit / profit_company_count if profit_company_count > 0 else None}
]

if len (unprofit_company) > 0:
    result.append (unprofit_company)

with open('tsk7.json', 'w', encoding = 'utf-8') as tsk7:
    json.dump (result, tsk7, indent = True, ensure_ascii = False)
