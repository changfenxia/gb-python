'''
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
'''
months_list = [
    'winter',
    'winter',
    'spring',
    'spring',
    'spring',
    'summer',
    'summer',
    'summer',
    'autumn',
    'autumn',
    'autumn'
    'winter'
]

months_dict = {
    '1': 'winter',
    '2': 'winter',
    '3': 'spring',
    '4': 'spring',
    '5': 'spring',
    '6': 'summer',
    '7': 'summer',
    '8': 'summer',
    '9': 'autumn',
    '10': 'autumn',
    '11': 'autumn',
    '12': 'winter'
}
# Через list
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
print(f"Месяц {month} относится к сезону: {months_list[month - 1]}")

# Через dict
month = input('Введите месяц в виде целого числа от 1 до 12: ')
print(f"Месяц {month} относится к сезону: {months_dict[month]}")