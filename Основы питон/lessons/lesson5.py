# Множества set,frozenset

# nums = {1,2,3,4,5,5}
# print(nums)
# print(nums[0:3])


# it_company = {"Google", "Meta", "Space X"}
# print(it_company)
# it_company.add("Tesla")
# print(it_company)
# it_company.remove("Google")
# print(it_company)
# it_company.pop()
# print(it_company)


# st = {1, 0.1, False ,"hello", (1,3,2), [1,3,4,5]}  #list, set - нельзя хранить 
# print(st)


# num1 = [1,2,3,4,5]
# num2 = [3,4,5,6,7]
# print(list(set(num1 + num2)))


# cars = {"Bmw", "Mazda", "Tesla", "Mercedes"}
# for car in cars:
#     print(car)


# nums = {-2, 34, 34545.3, -34.54, 3443}
# print(sorted(nums))


# st = {1, 1.0, True, "1"}
# print(st)
# print(False + 1)


# frozen_set = frozenset({1,2,3,4,5,5,5})
# print(frozen_set)
# frozen_set.add("Tesla") frozenset - неизменяемый
# print(frozen_set)


# Dict - Словари

# student = {'name': 'Oleg', 'age': '33'}
# print(len(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('language', 'Python')
# print(student)
# student.pop('age')
# print(student)
# student['language'] = 'Java'
# print(student)


# tesla_model_x = {
#     'brand' : 'Tesla',
#     'model' : 'Model X',
#     'year' : 2020 ,
#     'price' : '44500$',
#     'color' : 'while'
# }
# print(tesla_model_x)
# print(tesla_model_x['brand'])
# print(tesla_model_x.keys())
# print(tesla_model_x.values())
# print(tesla_model_x.items())

# for key, values in tesla_model_x.items():
#     print(key, values)


# todo_list = {
#     '08:00': 'Проснуться'
# }
# while True:
#     command = int(input("Введите комманду:\n1 - посмотреть список дел, 2 - добавить, 3 - удалить:\n"))
#     if command == 1:
#         print("СПИСОК ДЕЛ:")
#         print("--------------------")
#         for time, task in todo_list.items():
#             print(time, task)
#         print("--------------------")
#     elif command == 2:
#         add_time = input("Время: ")
#         add_task = input("Задание: ")
#         todo_list.setdefault(add_time, add_task)
#         print("Задание", add_task, "успешно добавлено в", add_time)
#         print("---------------------")
#     elif command == 3:
#         delete_time = input("Введите время для удаления: ")
#         todo_list.pop(delete_time)
#         print("Задание удалено")
#         print("---------------------")
#     elif command == 0:
#         print("Exit todo")
#         break
#     else:
#         print("Такой комманды нет")
