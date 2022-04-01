
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ErrorDivision(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def div (a, b):
        try:
            return (a / b)
        except:
            return ('Деление на ноль')




print(ErrorDivision.div(10, 0))
print(ErrorDivision.div(23,9))



