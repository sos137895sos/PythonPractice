# 1. Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.
def printMany():
    for i in range(1, 101):
        print(i)


printMany()

print("---------------"*5)
# 2. Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.


def printEvery3():
    for i in range(1, 89, 3):
        print(i)


printEvery3()

print("---------------"*5)
# 3. Write a function called "position" that returns a tuple of the first uppercase
# letter and its index location. If not found, returns -1.


def position(string):
    for num, s in enumerate(string):
        if s == s.upper():
            return (s, num)
    return -1


print(position("abcd"))
print(position("AbcD"))
print(position("abCD"))

print("---------------"*5)
# 4. Write a function called "findSmallCount" that takes one list of integers and
# one integer as input, and returns an integer indicating how many elements
# in the list is smaller than the input integer.


def findSmallCount(lst, num):
    counter = 0
    for i in lst:
        if i < num:
            counter += 1
    return counter


print(findSmallCount([1, 2, 3], 2))  # returns 1
print(findSmallCount([1, 2, 3, 4, 5], 0))  # returns 0
print(findSmallCount([1, 2, 3, 4, 5], 10))  # returns 5

print("---------------"*5)
# 5. Write a function called "findSmallerTotal" that takes one list of integers
# and one integer as input, and returns the sum of all elements in the list
# that are smaller than the input integer.


def findSmallerTotal(lst, num):
    total = 0
    for i in lst:
        if i < num:
            total += i
    return total


print(findSmallerTotal([1, 2, 3], 3))
print(findSmallerTotal([1, 2, 3], 1))  # returns 0
print(findSmallerTotal([3, 2, 5, 8, 7], 999))  # returns 25
print(findSmallerTotal([3, 2, 5, 8, 7], 0))  # returns 0

print("---------------"*5)
# 6.Write a function called "findAllSmall" that takes one list of integers
# and another integer as input, and returns an list of integers
# that contains all elements that are smaller than the input integer.


def findAllSmall(lst, num):
    smaller = []
    for i in lst:
        if i < num:
            smaller.append(i)
    return smaller


print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
print(findAllSmall([1, 2, 3], 2))  # returns [1]
print(findAllSmall([1, 3, 5, 4, 2], 4))  # returns [1, 3, 2]

print("---------------"*5)
# 7. Write a function called "summ" that takes one list of numbers,
# and return the sum of all elements in the input list.


def summ(lst):
    total = 0
    for i in lst:
        total += i
    print(total)
    return total


summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # returns 55
summ([])  # return 0
summ([-10, -20, -30])  # return -60
