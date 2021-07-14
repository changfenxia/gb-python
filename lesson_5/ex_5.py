'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import random

# writing random numbers to the file
with open('numbers_list.txt', 'w+') as my_file:
  random_nums = random.sample(range(1, 15), 5)
  my_file.write(' '.join(str(num) for num in random_nums))

# reading from the file
with open('numbers_list.txt') as my_file:
  document = my_file.read()
  print(document)
  sum = sum(int(x) for x in document.split())
  print(sum)
