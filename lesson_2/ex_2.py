'''
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().
'''
my_list = []
size = int(input('Введите количество элементов: '))
for i in range(size):
    el = input('Введите значение элемента: ')
    my_list.append(el)
print(f'Ваш список: {my_list}')
for i in range(0, size, 2):
    if (i + 1 != size):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(f'Новый список: {my_list}')