'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

# helper function to strip non-digits from string
def string_to_int(x):
  return int(''.join(filter(str.isdigit, x)))

classes_dict = {}
with open('classes.txt') as my_file:
  lines = my_file.read().split('\n')
  for line in lines:
    subject_name, hours = line.split(':')
    hours = [string_to_int(x) for x in hours.split() if len(x) > 1]
    classes_dict[subject_name] = sum(hours)

print(classes_dict)