# Функции - Functions

# print("geeks")
# def hello_world():
#     print('hello world')
# hello_world()


# def add():
#     num1 = int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     print(num1 + num2)
# add()


# def count_numbers():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     for num in nums:
#         if num % 2 == 0:
#             print(num, 'четный')
#         else:
#             print(num, 'нечетный')
# count_numbers()


# def reverse_word(word):
#     print(word[::-1])
# reverse_word('Geeks')
# reverse_word('python')
# reverse_word('oleg')


# def hello(name):
#     print('Привет', name) 
# hello('щ')
# hello('oleg')


# def huan(word:str) -> str:
#     'Huan is my friend'
#     print(word + word)
# huan('oleg')


# def mult(num1:int=1, num2:int=1) -> int:
#     print("Ответ:", num1 * num2)
# mult(11, 12)
# mult(12, 1000)


# def calculator(num1:int=1, num2:int=1, operator:str='+') -> int:
#     "Calculator from Huan"
#     if operator == "+":
#         print("Answ:", num1 + num2)
#     elif operator == "-":
#         print("Answ:", num1 - num2)
#     elif operator == "*":
#         print("Answ:", num1 * num2)
#     elif operator == "/":
#         print("Answ:", num1 / num2)
#     else:
#         print("Такого оператора не существует")
# calculator(12, 12, '-')
# calculator(10, 4, '/')
# calculator(2323, 2313, '+')
# calculator(12, 123, '*')
# calculator(12, 0, '/')

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print('Деление на ноль э')

# try:
#     print(10 + '5')
# except TypeError:
#     print('Ошибка типа данных')


# try:
#     print(10 / 0)
# except BaseException:
#     print("Code Error")


# while True:
#     try:
#         num1 = int(input("Num1: "))
#         operator = input("")
#         num2 = int(input("Num2: "))
#         if operator == "+":
#             print("Answ:", num1 + num2)
#         elif operator == "-":
#             print("Answ:", num1 - num2)
#         elif operator == "*":
#             print("Answ:", num1 * num2)
#         elif operator == "/":
#             try:
#                 print("Answ:", num1 / num2)
#             except ZeroDivisionError:
#                 print("Деление на ноль")
#         else:
#             print("Такого оператора не существует")
#     except ValueError:
#         print('Ошибка типа данных')