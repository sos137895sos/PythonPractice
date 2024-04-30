# def :define定義, 像是數學函式裡的f(x)
# def functionName(input1,input2,...,或是空值):
# function code here
# ex1
def sayHi():
    print("Hello, how are you?")


# function execution,invokation 在程式語言裡執行function較常出現的英文單詞，看文件的時候常出現。
sayHi()
# ex2 加法
# x,y 是paramenters參數，在定義function的時候給的參數


def addition(x, y):
    print(x + y)


# 18 ,12 是 arguments引數，與xy的paramenters不一樣，這邊的引數是給定確切的值
addition(18, 12)
# ex3
a = 10
b = 90


def addition(x, y):
    print(x + y)


addition(a, b)
# -----------------
# global variables全域變數, local variables區域變數:
# ex
a = 10  # global variables


def f1():
    x = 20  # f1的local variables
    y = 30  # f1的local variables
    print(x, y, a)


def f2():
    x = 2  # f2的local variables
    y = 3  # f2的local variables
    print(x, y, a)


f1()
f2()
# print(x, y)  # 錯誤：NameError: name 'x' is not defined 因為xy是在f1,f2裡定義的
# --------------------
# copy by value值 ex
a = 10

# parameters(inputs)參數 are local variables變數 in the function


def change(num):
    # 執行chang(a):
    #  num = a (cpoy by value) => num = 10
    print(num)  # num = 10
    num = 25
    print(num)  # num = 25


change(a)
print(a)  # a = 10
# copy by reference址 ex
a = [1, 2, 3, 4]


def change(lst):
    # 執行change(a):
    # lst = a (copy by reference) lst = a
    lst[0] = 100  # a = [100, 2, 3, 4]


change(a)
print(a)

# 如何在函式內更改copy by value全域變數 ex:
a = 10


def change(num):
    global a
    a = 25


change(a)
print(a)

# 如何在函式裡添加說明：


def myAddition(a, b):
    """這是一個加法函式"""  # 添加三組 ""
    print(a + b)


help(myAddition)  # 查看此函式是什麼用途
# ---------------
# return Keyword
# ex


def myAddition(a, b):
    return a + b  # return 要放在函式裡的最後一行，否則return下面的程式碼不會執行


print(myAddition(10, 20) + myAddition(30, 40))
# or
result1 = myAddition(10, 20)
result2 = myAddition(30, 40)
print(result1 + result2)
