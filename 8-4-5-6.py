"""
4Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.


"""

class Werhouse:


    def __init__(self):
        self._storage_dict = {}
        self._replase_dict = {}


    def add(self, el):
        """добавляем технику(el) в словарь"""
        self._storage_dict.setdefault(el.ch_class,[]).append(el)
         
    def remove(self, name):
        """ удалили обьект со  склада"""
        try:
            self._storage_dict.setdefault(name).pop(0)
            return ('Обект списан')
        except AttributeError:
             return ('Таких данных нет')

    def change_position (self, el):
        """ Перемещение обьекта во временый словарь что б затем переместить куда надо"""
        try:
            self._replase_dict.setdefault(el.ch_class,[]).append(el)
            self._storage_dict.setdefault(el).pop(0)
            return ('Обект перемещен во временное хранилище')
        except AttributeError:
              return ('Таких данных нет')


    def show(self):
        """показываем что сейчас на складе"""
        return f'Следующая техника находится на складе :{self._storage_dict}'
        # представление того что сечас в словаре лучше отдеьной
        # фунцией что б none не возвращался и разделение функционала


    def validation(self):
        t = int(input('Введите чило техники: '))
        s = int(t)
        n = input('Введите наименование техники')
        #try
        #except ValueError
        if type(t) != int:
            return ('Ошибка количество не может быть не числом')     # не исп принт принт возвращает none retern так не делает
        else:
            return ('Данные коректны')


class OfficeEquipment:

    def __init__(self, name, firm, year, model, cost):
        self.name = name
        self.firm = firm
        self.year = year
        self.model = model
        self.cost = cost
        self.ch_class = self.__class__.__name__


    def reprpresent(self):
        return f'Характеристики оборудования:\n' \
               f'1) Наименовние - {self.name}\n' \
               f'2) Фирма проихвдитель - {self.firm}\n'\
               f'3) Год выпуска - {self.year}\n' \
               f'4) Модель - {self.model}\n' \
               f'5) Цена - {self.cost} рублей'

    def is_working(self, state=True):
        """ Вывод рабочего статуса техники"""
        if state is True:
            return ('Оборудование рабочее')       # не исп принт принт возвращает none retern так не делает
        else:
            return ('Оборудование нуждается в ремонте')

    def name(self):
        return self.ch_class

    def __repr__(self):
            return f'{self.name}, {self.firm}, {self.year}, {self.model}, {self.name}'    # позволяет вернуть данные в словарь а не обьект класса

class Printer(OfficeEquipment):
    def __init__(self, name, firm, year, model, cost, quality_of_print):
        super().__init__(name, firm, year, model, cost)
        self.quality_of_print = quality_of_print

    def printed(self):
        return print(' Принтер делает копии')


class Scaner(OfficeEquipment):

   def __init__(self, name, firm, year, model, cost, resolution_of_scan, speed_of_scaning):
       super().__init__(name, firm, year, model, cost)
       self.resolution_of_scan = resolution_of_scan
       self.speed_of_scaning = speed_of_scaning

   def scaning(self):
       return print(' Сканер сканирует')

class Xerox(OfficeEquipment):

    def __init__(self, name, firm, year, model, cost, other_charastiristic):
        super().__init__(name, firm, year, model, cost)
        self.other_charastiristic = other_charastiristic

    def xerox(self):
        return print(' Ксерокс делает ксерокопии')




my_werhouse = Werhouse()
my_scaner = Scaner('TERA','xita','1999', 'LO9845', '12390', 'k', '0.6 в сек')
my_xerox = Xerox('QWER','sita','3999', 'LO9845', '1-390', 'k' )
my_printer = Printer('rewq','pita','3099', 'pO9846875', '156390', 'k' )
a = my_werhouse.add(my_printer)
b = my_werhouse.add(my_xerox)
c = my_werhouse.add(my_scaner)
d = my_werhouse.remove('ki')
e = my_werhouse.remove('Scaner')
f = my_werhouse.change_position('rt')
g = my_werhouse.change_position('Printer')
print(e)
print(d)
print(f)
print(g)
print(my_werhouse.show())
print(my_werhouse.validation())
print(my_scaner.reprpresent())
print(my_xerox.reprpresent())
print(my_scaner.is_working(False))





