"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
import sys


class Car:
    def __init__(self, color, cost, old, country, owner, number):
        self.color = color
        self.cost = cost
        self.old = old
        self.country = country
        self.owner = owner
        self.number = number


class SlotCar:
    __slots__ = ['color', 'cost', 'old', 'country', 'owner', 'number']

    def __init__(self, color, cost, old, country, owner, number):
        self.color = color
        self.cost = cost
        self.old = old
        self.country = country
        self.owner = owner
        self.number = number


my_car = Car(color='red',
             cost='free',
             old='new',
             country='USSR',
             owner='I',
             number='001')


my_slot_car = SlotCar(color='red',
             cost='free',
             old='new',
             country='USSR',
             owner='I',
             number='001')


print(sys.getsizeof(my_car.__dict__))  # 152
print(sys.getsizeof(my_slot_car.__slots__))  # 112
