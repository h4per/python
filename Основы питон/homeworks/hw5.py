# 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)


# 2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# for value in numbers:
#     numbers[value] *= 5
# print(numbers)


# 3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *= 2
# print(student)


# 4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] -= 1
# print(student)


# 5
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)


# 6
# student = {'name' : 'Askhat'}
# student.setdefault('address', 'Западный Анар')
# print(student)


# 7
# passwords = set()
# while True:
#     password1 = input("Введите пароль: ")
#     if len(password1) < 8:
#         print("Короткий пароль!")
#     elif '123' in password1:
#         print("Простой пароль!")
#     else:
#         password2 = input("Подтвердите пароль: ")
#         if password1 != password2:
#                 print("Различаются.")
#         else:
#                 passwords.add(password1)
#                 print("OK")
#                 print("Пароль создан!")
#                 print(f"Ваш пароль:", passwords)
#                 break
