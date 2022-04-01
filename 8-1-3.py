"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данн
"""

class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        mdate = []
        for el in date.split('-'):
            mdate.append(el)
        return int(mdate[0]), int(mdate[1]), int(mdate[2])

    @staticmethod
    def validate(day, month, year):
        if day >= 1 and day <= 31 and month >= 1 and month <= 12 and year >= 0 and year <= 2022:
                    return ('Верно')
        else:
            return ('Неправильные данные')





the_day = Date('11 - 1 - 2001')
print(the_day)
print(Date.validate(1, 8, 2022))
print(the_day.validate(1, 3, 2011))
print(Date.extract('1 - 5 - 2011'))
print(the_day.extract('8 - 7 - 2020'))
print(Date.validate(1, 66, 2000))