'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

num = 636
num_float = 56.2
name = "user"
password = "adminadmin"
is_admin = False

user_input = input("Enter the password: ")
if user_input == password:
    is_admin = True

print(is_admin)