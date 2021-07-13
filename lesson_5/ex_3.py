'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

with open('salaries.txt') as my_file:
  employees = my_file.read().split('\n')
  dict_employees = { el.split()[0] : int(el.split()[1]) for el in employees}

print('Employees with salary < 20000:')
for k,v in dict_employees.items():
  if v < 20000:
    print(k)

print('Average salary:')
print(int(sum(dict_employees.values()) / len(dict_employees)))