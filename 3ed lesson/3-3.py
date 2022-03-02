"""
Реализовать функцию my_func(),
которая принимает три позиционных
аргумента и возвращает сумму наибольших двух аргументов.  через сумму мин и максимум
"""
def sum_of_2max (arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
       return (arg_1 + arg_2)
    elif arg_1 >= arg_2 and arg_3 >= arg_2:
        return (arg_1 + arg_3)
    else:
        return (arg_2 + arg_3)

print(sum_of_2max(float(input('arg1: ' )), float(input('arg2: ' )), float(input('arg1: ' ))))

# версия через минмум
def sum_of_2max_2 (arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min([arg1, arg2, arg3]) # смотрим на аргументы как на список и нахлодим минималтное
print(
    sum_of_2max_2 (float(input('arg1: ' )), float(input('arg2: ' )), float(input('arg1: ' )))
      )
