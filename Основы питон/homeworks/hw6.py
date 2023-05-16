# 1
# def abbrev():
#     word = "For your interest"
#     word_spl = word.upper().split()
#     print(word_spl[0][0] + word_spl[1][0] + word_spl[2][0])
# abbrev()


# 2
# def checker(text):
#     dict = {}
#     words = text.lower().split()
#     for word in words:
#         dict[word] = words.count(word)
#     print(dict)
# checker("Money, money, money, it\s always sunny, in the richmen\s world")


# 3
# word = input("Введите слово: ")
# if len(set(word)) == len(word):
#     print(True)
# else:
#     print(False)


# 4
# def reverse(n):
#     print(str(n)[::-1])
# reverse(21)


# 5
# def chat_bot():
#     while True:
#         ans = input("Введите что-то: ")
#         if "?" in ans:
#             print("Конечно!")
#         elif ans.isupper():
#             print("Усбакойся")
#         elif ans == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# chat_bot()