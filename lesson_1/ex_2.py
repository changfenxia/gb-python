'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

time_seconds = int(input("Enter time in seconds: "))
hours = time_seconds // 3600
minutes = (time_seconds % 3600) // 60
seconds = time_seconds - (hours * 3600) - (minutes * 60)

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")