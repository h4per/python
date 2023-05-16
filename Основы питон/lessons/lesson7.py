# def hello_world(name):
#     print("Hello World and Hello", name)
# hello_world(1)


# def div(num1:int=1, num2:int=1) -> float:
#     return num1 / num2
# print(div(5, 1))


# def reverse_name(name:str = 'oleg') -> str:
#     return name[::-1]
# print(reverse_name())
# print(reverse_name('fjk'))


# def hello(word:str = 'Pyhton') -> str:
#     print('Geeks')
#     return 'oleg'
#     print(word)
# print(hello())


# def calculator(num1:int=1, operator:str="+", num2:int=1) -> int:
#     "Calculator from Huan base function in Python"
#     if operator == "+":
#         return "Answ:", num1 + num2
#     elif operator == "-":
#         return "Answ:", num1 - num2
#     elif operator == "*":
#         return "Answ:", num1 * num2
#     elif operator == "/":
#         return "Answ:", num1 / num2
#     else:
#         return "Такого оператора не существует"
# print(calculator(10, "*", 20))



# *args, **kwargs
# print('hello', 'world', 'and', 'python')


# def welcome(name):
#     print("Добро пожаловать", name)
# welcome('oleg')


# def args_welcome(*args):   # можно не только с args, * - решает
#     for name in args:
#         print("Добро пожаловать", name)
# args_welcome('oleg', 'fjk', 'janush', 'kurmanbek', 'askhat')


# def avg_student(name:str = "Oleg", *points) -> str:
#     print(name, sum(points) / len(points), round(sum(points) / len(points)))
# avg_student("janush", 3,4,5,2,2,5,5,2,2)
# avg_student("oleg", 4,5,4,2,4,5,4,5,5,5,5,2)


# def translate(**words) -> dict:
#     print(words)
# translate(USA = "США", apple = "яблоко", car = "машина", phone = "телефон")


# lambda функции
# def simple_function(num:int) ->int:
#     return num * num
# print(simple_function(20))

# lambda_function = lambda num: num * num
# print(lambda_function(20))

# print((lambda num: num * num)(20))


# Пример 2
# def add(num1:int = 10, num2:int = 10) -> int:
#     return num1 + num2
# print(add(20, 20))

# add_lambda = lambda num1=10, num2=10: num1 + num2  # можно по умолчанию поставить
# print(add_lambda(20, 20))

# print((lambda num1,num2: num1 + num2)(20, 20))


# Пример 3
# numbers = [10, 20, 30, 40, 50]
# new_numbers = []
# def mult_two(nums:list) -> list:
#     for n in nums:
#         new_numbers.append(n * 2)
#     return new_numbers
# print(mult_two(numbers))

# numbers = [10, 20, 30, 40, 50]
# new_numbers = list(map(lambda nums: nums * 2, numbers))
# print(new_numbers)

# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda nums: nums * 2, numbers)))

# print(list(map(lambda nums: nums * 2, [10, 20, 30, 40, 50])))


# Пример 4
# nums = [10, 4, 5, 6, 555, 345, 256, 1001]
# even_nums = []
# def even_checker(nums:list) -> list:
#     for num in nums:
#         if num % 2 == 0:
#             even_nums.append(num)
#     return even_nums
# print(even_checker(nums))

# nums = [10, 4, 16, 6, 555, 44, 256, 1001]
# even_nums = list(filter(lambda nums: nums % 2 == 0, nums))
# print(even_nums)

# print(list(filter(lambda nums: nums % 2 == 0, [10, 4, 16, 6, 555, 44, 256, 1001])))