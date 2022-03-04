"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
with open('5-4.txt', 'r', encoding='utf-8') as f:
    new = []#список для записи перевода и цифры
    translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'} #словарь для замены при копировании данных исходного файла 
    for el in f:
        el = el.split(' — ') # разделили по тире
        new.append(translator[el[0]] + ' - ' + el[1]) #заменили 0 id из словаря а цифру взяли из файла f
    for el in new:
        print(el)

with open('5-4new.txt', 'w+', encoding='utf-8') as nf:
    nf.writelines(new) # запишем все

# вывод без пробелов
with open('5-4new.txt', 'r', encoding='utf-8') as nf2:
    while True:
        content = nf2.read(102)
        print(content)
        if not content:
            break

