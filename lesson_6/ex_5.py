'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationary:
  title = 'Канцелярская принадлежность'

  def draw(self):
    print('Запуск отрисовки.')

class Pen(Stationary):
  def __init__(self):
    self.title = 'Ручка'

  def draw(self):
    super().draw()
    print('Рисуем ручкой.')

class Pencil(Stationary):
  def __init__(self):
    self.title = 'Карандаш'

  def draw(self):
    super().draw()
    print('Рисуем карандашом.')

class Handle(Stationary):
  def __init__(self):
    self.title = 'Маркер'

  def draw(self):
    super().draw()
    print('Рисуем маркером.')

my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()