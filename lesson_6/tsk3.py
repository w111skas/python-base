"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""



class Worker:

    name = None
    surname = None
    position = None
    income = None
    __sallary = None

    def __init__ (self, name, surname, position, income, sallary):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        self.sallary = sallary

class Position(Worker):

    def __init__ (self, name, surname, position, income, bonus):
        super().__init__ (name, surname, position, income, bonus)

    def get_full_name (self):
        return self.name + self.surname + self.position

    def get_total_income (self):
        self.__income = {'Зарплата': self.income, 'Премия': self.sallary}
        return self.__income

manager = Position ('Сергей ','Иванов:\n ', '=Управляющий=\n\n', 500, 100)

print (manager.get_full_name(), manager.get_total_income())