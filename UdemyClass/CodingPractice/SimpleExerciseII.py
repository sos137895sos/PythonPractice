# 1.Write a function called "stars" which prints out layers of stars
# in the following pattern:
def stars(star):

    for i in range(1, star+1):
        print("*" * i)


stars(1)
stars(5)

print("------------" * 5)
# 2.Write a function called "stars2" which prints out layers of stars
# in the following pattern:


def stars2(star):
    for i in range(1, star+1):
        print("*"*i)
    for i in range(star-1, 0, -1):

        print("*"*i)


stars2(3)

print("------------" * 5)
# 3.Write a function called "table" which takes an input n, and prints out n x 1 to n x 9


def table(n):
    for i in range(1, 10):
        print(f"{n} X {i} = {n * i}")


table(1024)

print("------------" * 5)
# 4.Write a function called "table9to9" that prints out the multiplication table:


def table9to9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} X {j} = {i * j}")


table9to9()

print("------------" * 5)
# 5.Write a function called "swap" that takes a string as input,
# and returns a new string with lowercase changed to uppercase,
# uppercase changed to lowercase.


def swap(string):
    swp = ""
    for i in string:
        if i == i.upper():
            swp += i.lower()
        else:
            swp += i.upper()
    print(swp)
    return swp


swap("Today is ranning day!")
swap("gOOd")

print("------------" * 5)
# 6.Write a function called "findMin" which takes an list as input,
# and returns the minimum element in the input list.


def findMin(lst):
    if len(lst) == 0:
        print("undefined")
        return "undefined"
    min_x = lst[0]
    for i in lst:
        if i < min_x:
            min_x = i
    print(min_x)
    return min_x


findMin([1, 2, 5, 6, 99, 4, 5])  # returns 1
findMin([])  # returns undefined
findMin([1, 6, 0, 33, 44, 88, -10])  # returns -10
