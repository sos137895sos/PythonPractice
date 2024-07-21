# 1.Write a function called "mySort" that takes an list of integers as input,
# and returns the sorted version of the input list.
# You are not allowed to use the built-in sorted() function.
import math


def findMin(lst):
    if len(lst) == 0:
        print("undefined")
        return "undefined"
    min_x = lst[0]
    for i in lst:
        if i < min_x:
            min_x = i
    return min_x


def mySort(myList):
    sort = []
    while len(myList) > 0:
        min_e = findMin(myList)
        sort.append(min_e)
        myList.remove(min_e)
    print(sort)
    return sort


mySort([17, 0, -3, 2, 1, 0.5])  # returns [-3, 0, 0.5, 1, 2, 17]

print("----------"*5)


# 2. Write a function called "isPrime" that takes an integer as input,
# and returns a boolean value that indicates if the input number is prim
def isPrime(p):
    if p == 1:
        print(False)
        return False
    for i in range(2, p):
        if p % i == 0:
            print(i)
            print(False)
            return False
    else:
        print(True)
        return True


isPrime(1)  # returns false
isPrime(5)  # returns true
isPrime(91)  # returns false
isPrime(1000000)  # returns false
isPrime(10001)


# 解法2
def isPrime(n):
    if n == 1:
        print(False)
        return False

    stater = 2
    while stater < n:
        if n % stater == 0:
            print(False)
            return False
        stater += 1

    print(True)
    return True


isPrime(1)  # returns false
isPrime(5)  # returns true
isPrime(91)  # returns false
isPrime(1000000)  # returns false
isPrime(10001)


print("----------"*5)


# 3. Write a function called "palindrome" that checks if the input string is a palindrome.
# (Search on google if you don't know what a palindrome is.)
# 解法1
def palindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            print(False)
            return False
        left += 1
        right -= 1
    print(True)
    return True


# 解法2
def palindrome2(string):
    for i in range(0, math.floor(len(string) / 2)):
        if string[i] != string[len(string) - 1 - i]:
            print(False)
            return False
        print(True)
        return True


palindrome2("bearaeb")  # true
palindrome2("Whatever revetahW")  # true
palindrome2("Aloha, how are you today?")  # false

print("-------" * 5)

# 4.Write a function called "pyramid" that takes an integer as input,
#  and prints a pyramid in the following pattern:


def pyramid(n):
    space = n - 1
    star = 1
    for i in range(n):
        print(space * " " + star * "*")
        star += 2
        space -= 1


pyramid(5)

print("--------"*5)


# 5.Write a function called "inversePyramid"
# that draws pyramid upside down.
# 解法1：自己
def inversePyramid(n):
    space = 0
    star = 2*n - 1
    for i in range(n):
        print(space * " " + star * "*")
        space += 1
        star -= 2


# 解法2：
def inversePyramid2(m):
    result = []

    def pyramid(n):
        space = n - 1
        star = 1
        for i in range(n):
            result.append(space * " " + star * "*")
            star += 2
            space -= 1
    pyramid(m)
    result.reverse()
    for line in result:
        print(line)


inversePyramid2(5)

print("------"*5)


# 6.Given a list of ints,
# return True if the list contains a 3 next to a 3.
# 解法1：自己
def has_33(lst):
    if lst == []:
        print(False)
        return False
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            print(True)
            return True
    print(False)
    return False


# 解法2：
def has_33_2(lst):
    result = False
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            return True
    return result


has_33([1, 5, 7, 3, 3])  # True
has_33([])  # False
has_33([4, 3, 2, 1, 0])  # False
has_33([1, 3, 5, 7, 9, 0, 3, 4, 3, 5, 22, 33, 55, 333, 3, 3])
print(has_33_2([1, 5, 7, 3, 3]))  # True
print(has_33_2([]))  # False
print(has_33_2([4, 3, 2, 1, 0]))  # False
print(has_33_2([1, 3, 5, 7, 9, 0, 3, 4, 3, 5, 22, 33, 55, 333, 3, 3]))


print("--------"*5)


# 7.Write a function that check if a list contains a subsequence
# of 007
def spyGame(lst):
    string = "007"
    target_for_lst = 0
    target_for_string = 0
    while target_for_lst < len(lst):
        if lst[target_for_lst] == int(string[target_for_string]):
            target_for_string += 1
            if target_for_string == len(string):
                return True
        target_for_lst += 1

    return False


print(spyGame([1, 2, 4, 0, 3, 0, 7]))  # True
print(spyGame([1, 2, 5, 0, 3, 1, 7]))  # False
print(spyGame([1, 2, 5, 0, 3, 0, 3, 5, 7]))
