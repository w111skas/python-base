"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""


from time import sleep

class TrafficLight:
    __color = ['Красный - STOP', 'Желтый - READY?', 'Зеленый - GO!']
    def running (self):
        start = 0
        while start < 3:
            print (f'Сигнал светофора:\n'
                   f'{TrafficLight.__color [start]}')
            if start == 0:
                sleep (3)
            elif start == 1:
                sleep (4)
            elif start == 2:
                sleep (5)
            start += 1

TrafficLight = TrafficLight ()
TrafficLight.running ()