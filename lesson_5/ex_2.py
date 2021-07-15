'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

Я решил немного усложнить задачу, интересно было посчитать сколько примерно слов в "Мастер и Маргарита", сколько из них уникальных и какие слова самые частотные.
'''
from collections import Counter

with open('master.txt') as my_file:
  document = my_file.read()
  lines = document.split('\n')
  words = document.split()
  my_counter = Counter(words)
  
  print(f'В документе {len(lines)} строки.')
  print(f'В документе {len(words)} слов.')
  print(f'Из них {len(set(words))} уникальных слов.')
  print(f'В одной строке в среднем {int(len(words)/len(lines))} слов.')
  print(f'10 слов, которые чаще всего встречаются - {my_counter.most_common(10)}')