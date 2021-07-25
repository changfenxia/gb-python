from abc import ABC, abstractmethod

class Clothes(ABC):
  @abstractmethod
  def fabric_consumption(self):
    pass

class Coat(Clothes):
  def __init__(self, v):
    self.v = v
  
  @property
  def fabric_consumption(self):
      return f"Расход ткани на пальто: {self.v / 6.5 + 0.5} м2"

class Suit(Clothes):
  def __init__(self, h):
    self.h = h

  @property
  def fabric_consumption(self):
    return f"Расход ткани на костюм: {self.h * 2 + 0.3} м2"


my_shiny_suit = Suit(1.8)
print(my_shiny_suit.fabric_consumption)
my_super_coat = Coat(13)
print(my_super_coat.fabric_consumption)
