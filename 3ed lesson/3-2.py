"""
Выполнить функцию, которая принимает несколько параметров,
 описывающих данные пользователя: имя,
фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def data_sets (**kwargs):
    return kwargs
name = input('Выедите ваше имя: ')
surname = input('Выедите вашу фамилию: ')
b_year = input('Выедите год вашего рождения: ')
y_city = input('Выедите ваш город: ')
email = input('Выедите ваш email: ')
phone = input('Выедите ваш телефон: ')
print(data_sets(name=name, surname=surname, b_year=b_year, y_city=y_city, email=email, phone=phone))
