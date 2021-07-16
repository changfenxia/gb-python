# coding=utf-8
'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
  speed = 0

  def __init__(self, color, name):
    self.color = color
    self.name = name
    self.is_police = False

  def go(self):
    self.speed = 60
    print('Машина поехала.')

  def stop(self):
    self.speed = 0
    print('Машина остановилась.')

  def turn(self, direction):
    print(f'Машина повернула: {direction}')

  def show_speed(self):
    print(f'Текущая скорость: {self.speed}км/ч')

  def speed_up(self):
    self.speed += 10

  def speed_down(self):
    self.speed -= 10

class TownCar(Car):
  def show_speed(self):
    print(f'Текущая скорость: {self.speed}км/ч')
    if self.speed > 60:
      print('Внимание! Превышение скорости! Разрешенная скорость 60км/ч')

class SportCar(Car):
  def __init__(self, color, name):
    super().__init__(color, name)

  def go(self):
    self.speed =90
    print('Машина поехала.')

class WorkCar(Car):
  def go(self):
    self.speed = 40
    print('Машина поехала.')

  def show_speed(self):
    print(f'Текущая скорость: {self.speed}км/ч')
    if self.speed > 40:
      print('Внимание! Превышение скорости! Разрешенная скорость 40км/ч')

class PoliceCar(Car):
  def __init__(self, color, name):
    super().__init__(color, name)
    self.is_police = True

my_towncar = TownCar('Blue', 'Toyota')
my_towncar.go()
my_towncar.show_speed()
my_towncar.turn('налево')
my_towncar.speed_up()
my_towncar.show_speed()

my_sportcar = SportCar('Red', 'Ferrari')
my_sportcar.go()
my_sportcar.show_speed()
my_sportcar.stop()
print(my_sportcar.color)

my_policecar = PoliceCar('white', 'Toyota')
print(my_policecar.is_police)