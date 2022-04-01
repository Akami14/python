'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * j'

    def __add__(self, other):
        print('Сумма комплексных чисел равна')
        return  f'{self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        print('Произведение комплексных чисел равно')
        return f' {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * j'

    def __str__(self):
        return f' {self.a} + {self.b} * j'


с1 = ComplexNumber(7, 2)
с2 = ComplexNumber(1, 9)
print(с1)
print(с1 + с2)
print(с1 * с2)