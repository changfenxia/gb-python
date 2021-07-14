'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

companies_data = {}
final_data = []

with open('companies.txt') as companies_file:
  companies = companies_file.read().split('\n')
  for c in companies:
    c_data = c.split()
    companies_data[c_data[0]] = int(c_data[2]) - int(c_data[3])

final_data.append(companies_data)
final_data.append({"average_profit": int(sum(companies_data.values()) / len(companies_data))})


with open('companies_data_report.json', 'w') as report_file:
  json.dump(final_data, report_file)