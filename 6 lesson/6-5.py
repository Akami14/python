"""
Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.


"""
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw():
        return print('«Запуск отрисовки»')


class Pen(Stationery):

    def draw():
        return print('spam and egs')


class Pencil(Stationery):

    def draw():
        return print('42')


class Handle (Stationery):

    def draw():
        return print('14')



my_pen = Pen.draw()

my_pencil = Pencil.draw()

my_handle = Handle.draw()




