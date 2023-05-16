# 1
# def hello(x):
#     print(x * x - 10)
# hello(7)
# типа стрелка тут
# print((lambda num: num * num - 10)(7))


# 2
# print(list(filter(map(lambda names: len(names) == len(set(names))))))


# 3
# print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# 4
# print(list(filter(lambda names: names == names[::-1],["azat", "zina", "kuma", "anna", "sas"])))


# 5
# def time_to_sec_calc(time_str:str)-> int:   
#     h, m, s = map(int, time_str.split(':'))
#     return(h * 3600 + m * 60 + s)

# time1 = input("Введите первую отметку времени (в формате Часы:Минуты:Секунды): ")
# time2 = input("Введите вторую отметку времени (в формате Часы:Минуты:Секунды): ")

# time_difference = time_to_sec_calc(time2) - time_to_sec_calc(time1)

# print(f"Разница между отметками: {time_difference} секунд")
