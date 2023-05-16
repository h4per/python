# Модули, работа с файлами

# def add (num1:int=10, num2:int=10) -> int:
#     return num1 + num2

# def hello_world():
#     return "Hello World and Python"

# def welcome(name:str="oleg")-> str:
#     return "Hello" + name

# numbers = [1, 2, 3, 4, 5, 6]
# it = "geeks"


# f = open('hello.txt', 'w')
# f.write("Hello World and Python oleg!")
# f.close()

# r = open('hello.txt', 'r')
# print(r.read())
# r.close()


# py = open('test.py', 'w')
# py.write('print("Hello World and test code")')
# py.close()


# read_code = open('moduls.py', 'r')
# print(read_code.read())
# read_code.close()


# test = open('kg.txt', 'w', encoding='utf-8')
# test.write('Привет Кыргызстан! oleg')
# test.close()

# read_text = open('kg.txt', 'r', encoding='utf-8')
# print(read_text.read())
# read_text.close()


# nums = open('numbers.txt', 'w', encoding="utf-8")
# nums.write("0775151506\n")
# nums.write("0777452238\n")
# nums.write("1328493018590\n")
# nums.close()

# new_numbers = open('numbers.txt', 'a+',encoding="utf-8")
# new_numbers.write("0324141\n")
# new_numbers.close()


# with open('olen.txt', 'w', encoding="utf-8") as olen:
#     olen.write("hello olen!")

# with open('olen.txt', 'r', encoding="utf-8") as olen_read:
#     print(olen_read.read())


# name = "Oleg"
# surname = "Coffi"
# age = 23
# language = "python"
# is_learning = True
# print(f"Hello,my name is {name} {surname}. I'm {age}. Now I'm learning {language}. Is learn {is_learning}")



# def func_contact():
#     with open('contact.txt', 'a+', encoding="utf-8") as c:
#         c.write("МЧС 112\n")
#     while True:
#         command = input("Введите комманду:\n1 - посмотреть контакты, 2 - добавить контакты, 3 - удалить контакты:\n")
#         if command == "1":
#             with open('contact.txt', 'r', encoding="utf-8") as read_contact:
#                 print(read_contact.read())

#         elif command == "2":
#             add_name = input("Имя: ")
#             add_number = input("Номер: ")
#             with open('contact.txt', 'a+', encoding="utf-8") as write_contact:
#                 write_contact.write(f"{add_name} {add_number}\n")
#                 print(f"Контакт {add_name} успешно добавлен")

#         elif command == "3":
#             del_contact = input("Введите имя контакта,которого удалить: ")
#             with open('contact.txt', 'r+') as del_contact:
#                 d = del_contact.readlines()
#                 del_contact.seek(0)
#                 for i in d:
#                     if i != 1:
#                         del_contact.write(i)
#                 del_contact.truncate()
#         else:
#             print("нет такой команды")

# func_contact()