debet = float(input('Введите выручку: '))
credit = float(input('Введите издержки: '))
rent = debet/credit
if debet > credit:
    print('Фирма работает с прибылью. Рентабельность выручки составила:', rent)
    emploes = int(input('Введите количество сотрудников фирмы: '))
    debet_for_one_emploes = debet / emploes
    print('прибыль в расчете на одного сторудника сотавила: ', debet_for_one_emploes)
elif debet == credit:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток' )