"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

import copy

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_view = str()
        for el in range(len(self.matrix)):
            matrix_view = matrix_view + '\t'.join(map(str, self.matrix[el])) + '\n'
        return matrix_view

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix): #сравниваем 2 матрицы по общей длине
            return None
        b = copy.deepcopy(self.matrix) # копируем 1ю матрицу для слжения
        #print(b)
        for i in range(len(self.matrix)): # i индекс для списков внутри отвечает за эл = [1, 0, 0] он их нумерует
            #print(i)
            for j in range(len(self.matrix[i])): # j индекс для списка внутри списка отвечает за ел = 1 в каждом списке
                # за счет вложености цикла он пронумерует все внутренее ел внутрених списков
                b[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(b)




x = [[1, 0, 0], [0, 1, 0], [0, 1, 0]]
y = [[1, 1, 0], [1, 1, 0], [1, 0, 0]]
my_matrix_x = Matrix(x)
my_matrix_y = Matrix(y)
print(my_matrix_y)
print(my_matrix_x)
matrix_sum = my_matrix_x + my_matrix_y
print(matrix_sum)
print(type(matrix_sum))


