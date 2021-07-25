'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
'''

class Matrix:
  list = []
  def __init__(self, list):
    self.list = list

  def __str__(self):
    result = ""
    for el in self.list:
      result += f"{el}\n"
    return result

  def __add__(self, other):
    result = []
    for el in zip(self.list, other.list):
      result.append([sum(x) for x in zip(el[0], el[1])])
    
    return Matrix(result)

test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_little_matrix = Matrix(test_list)
print(my_little_matrix)
my_second_little_matrix = Matrix(test_list)
print(my_little_matrix + my_second_little_matrix)


