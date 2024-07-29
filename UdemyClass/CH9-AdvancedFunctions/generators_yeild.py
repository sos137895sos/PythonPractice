def cube(n):
    result = []  # result長度越長會佔用越多的記憶體
    for x in range(n):
        result.append(x ** 2)
    return result


for i in cube(5):
    print(i)


# 使用genertor yield
def cube(n):
    for x in range(n):
        yield x ** 3


for element in cube(6):
    print(element)


# 使用genertor yield from
def sub_generator(x):
    for i in range(x):
        yield i ** 5


def gen(y):
    yield from sub_generator(y)


for num in gen(3):
    print(num)
