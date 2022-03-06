"""
Реализовать класс Road (дорога).

определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв.
 метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""
class Road:
    #атрибуты
    constant_weight = 2
    constant_height = 89

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        print('Для покрыия дороги длиной',self.length, 'м и шириной', self.width, 'м потребуется')
        s = self.length*self.width*self.constant_weight*self.constant_height/1000
        return s


my_road = Road(int(input('введите длину в м: ')),int(input('ввелите ширину в м: ')))
solution = my_road.mass()
print(solution, 'т')
