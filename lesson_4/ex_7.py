'''
Фукнция получения факториала
'''

def fact(n):
  result = 1
  count = 1
  while (count < n):
    result = result * count
    count += 1
    yield result

for el in fact(100):
  print(el)