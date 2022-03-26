"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property """


from abc import ABC, abstractmethod


class Clothes(ABC):


    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        pass


class Coat(Clothes):

    def __init__(self, coat):
        self.coat = coat

    @property
    def expense(self):
        _a = 6.5
        _b = 0.5
        return self.coat / _a + _b

    def __str__(self):
        return str(self.coat)


class Suit(Clothes):

    def __init__(self, suit):
        self.suit = suit

    @property
    def expense(self):
        _a = 2
        _b = 0.3
        return self.suit * _a + _b

    def __str__(self):
        return str(self.suit)


my_coat = Coat(52)
my_suit = Suit(1.80)
print(my_suit)
print(my_coat)
print('расход ткани для костюма: ', my_suit.expense)
print('расход ткани для пальто: ',my_coat.expense)