'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
line = input('Вводите данные для записи, для окончания ввода нажмите enter: ')
with open("myfile_1.txt", "w+") as my_file:
  while bool(line):
    my_file.write(f'{line}\n')
    line = input()
