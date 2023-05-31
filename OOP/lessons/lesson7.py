def pair_sum_sequense(n):  # O(N)
    sum = 0
    while sum < n:
        sum += 1
    return sum

def pair_sum(a, b):  # O(1)
    return a + b


letters = ['a', 'b', 'c', 'd', 'e', 'f']
digits = [1, 2, 3, 4, 5, 6]

def func1():  # 6 + 6 = 12  O(N+N) = O(2N) = O(N)
    for i in letters:
        print(i)
    for j in digits:
        print(j)

def func2():  # 6 * 6 = 36  O(N*N) = O(N**2)
    for i in letters:
        for j in digits:
            print(i, j)



def linear_search(lst, value):
    N = len(lst)
    ResOk = False
    Pos = -1
    j = 0
    while True:
        if j < N and Pos == -1:
            if lst[j] == value:
                Pos = j
                ResOk = True
            j += 1
        else:
            if ResOk:
                print("Found! ", j)
                break
            else:
                print("Not found")
                break
            

lst = [i for i in range(2000)]
# linear_search(lst, 87)


# val = 32
# for i in lst:
#     if i == val:
#         print("Founded! ", lst.index(i))
# print("Not found!")


# print(lst.index(732))