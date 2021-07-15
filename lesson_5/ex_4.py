'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
numbers_en_ru = {
  'One': 'Один',
  'Two': 'Два',
  'Three': 'Три',
  'Four': 'Четыре',
  'Five': 'Пять',
  'Six': 'Шесть',
  'Seven': 'Семь',
  'Eight': 'Восемь' ,
  'Nine': 'Девять',
}
with open('numbers.txt') as numbers_eng, open('numbers-2.txt', 'w+') as numbers_ru:
  for line in numbers_eng:
    print(line)
    num_eng = line.split()[0]
    num_ru = numbers_en_ru[num_eng]
    new_line = f'{num_ru} {" ".join(line.split()[1:])}\n'
    numbers_ru.write(new_line)

