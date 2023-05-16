# 1
# for i in range(1,6):
#     print(i, "0")


# 2
# lst = []
# for num in range(1,101):
#     lst.append(num)
# print(lst)


# 3
# for i in range(1, 497):
#     if i % 2 == 0:
#         print(i, "Четный")


# 4
# lst = list(range(1,1001))
# print(min(lst))
# print(max(lst))
# print(sum(lst)) # за пол секунды посчитал мб меньше


# 5
# lst = []
# for n in range(101):
#     lst.append(0)
# print(lst)


# 6
# it_company = ('Google','Amazon','Microsoft')
# list_it_company = list(it_company)
# list_it_company.append('Tesla')
# print(tuple(list_it_company))


# 7
# it_company = ('Google','Amazon','Microsoft')
# list_it_company = list(it_company)
# list_it_company.append('Tesla')
# print(list_it_company.index('Amazon'))


# 8
# it_company = ('Google','Amazon','Microsoft')
# list_it_company = list(it_company)
# list_it_company.append('Tesla')
# list_it_company[0] = 'Apple'
# print(list_it_company)


# 9
# it_company = ('Google','Amazon','Microsoft')
# list_it_company = list(it_company)
# list_it_company[0] = 'Apple'
# list_it_company.append('Tesla')
# print(list_it_company[:3])


# 10
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
# 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
# 'overview')
# print("В тексте слово Python повторяется", text_tuple.count('Python'), "раза")


# 11
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num1 , num2 = num2 , num1
# print("Новое значение num1 =", num1)
# print("Новое значение num2 =", num2)


# 12
# while True:
#     age = int(input("Введите возраст: "))
#     if age == 18:
#         print("Доступ разрешен")
#         break
#     else:
#         print("Извините, пользование данныe ресурсом только с 18 лет")
