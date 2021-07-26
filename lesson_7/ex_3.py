class Cell:
  def __init__(self, num):
    self.num = num
  
  def __add__(self, other):
    return Cell(self.num + other.num)
  
  def __sub__(self, other):
    if ((self.num - other.num) > 0):
      return Cell(self.num - other.num)
    else:
      print("The difference should be more or equal to zero")
      return None

  def __mul__(self, other):
    return Cell(self.num * other.num)
  
  def __truediv__(self, other):
    return Cell(self.num // other.num)
  
  @classmethod
  def make_order(cls, cell, num):
    rows = cell.num // num
    single_row = str("*" * num) + "\n"
    return (single_row) * rows + ("*" * (cell.num % num))

cell_a = Cell(20)
print(Cell.make_order(cell_a, 3))