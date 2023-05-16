# Tuple - Кортежи. Циклы for и while

# int,float,bool,str,tuple - неизмен 
# list - измен

# names = ('Kurmanbek','Islam','Oleg')
# print(names)
# print(names[1:3])
# print(names[::2])

# names.append('') # tuple неизменяемый тип данных
# names.remove('')

# tup = ('hello',)
# print(type(tup))

# tup = ('key', 23, True, 0.1, [1,2,3,5])
# print(tup)
# print(tup[4][0])


# cars = ('BMW','Honda','Audi')
# print(cars)
# list_cars = list(cars)
# print(list_cars)
# list_cars.append('Tesla')
# print(list_cars)
# print(tuple(list_cars))


# import dis
# lst = [1, 2, 3, 4, 5]
# tup = (1, 2, 3, 4, 5)

# dis.dis('lst')
# dis.dis('tup')



# Циклы for, while

# for num in range(101):
    # print(num, 'oleg')

# for i in range(10, 51):
#     print(i)


# for i in range(1,11,2):
#     print(i)


# numbers = [1, 2, 3, 4, 5, 53, 25, 234, 2342]
# print(numbers)
# for n in numbers:
#     if n % 2 == 0:
#         print(n, "Четный")
#     else:
#         print(n, "Нечетный")


# it = ["Geeks","Meta","Google","Neobis"]
# for i in it:
#     print(i)
#     if i == "Meta":
#         break #break досрочно прерывает цикл, continue продолжает цикл


# name = "Nurbolot"
# for n in name:
#     print(n, end=" ")


# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 +=1
    # num1 = num1 + 1 сокращение num1 +=1
    # print(num1)


# n = 0
# while True:
#     n += 1
#     print("Geeks", n)


# while True:
#     num1 = int(input("Num1: "))
#     operator = input("+, -, *, /: ")
#     num2 = int(input("Num2: "))
#     if operator == "+":
#         print("Answ:", num1 + num2)
#     elif operator == "-":
#         print("Answ:", num1 - num2)
#     elif operator == "*":
#         print("Answ:", num1 * num2)
#     elif operator == "/":
#         print("Answ:", num1 / num2)
#     elif num1 == 0 and num2 == 0 and operator == "0":
#         print("Stop")
#         break
#     else:
#         print("Такого оператора не существует")



# import random

# print(random.randint(1, 10))
# random_number = random.randint(1, 10)
# attempt = 0
# while True:
#     input_number = int(input("Введите число от 1 до 10: "))
#     if input_number >= 1 and input_number <= 10: 
#         attempt += 1
#         if attempt == 5:
#             print("Вы проиграли")
#             break
#         elif input_number == random_number:
#             print("Вы выиграли!")
#             break
#         else:
#             print("Неправильно у вас", 5 - attempt, "попыток")
#     else:
#         print("Введите число от 1 до 10!")
