from collections import Counter
from collections import defaultdict
from collections import namedtuple
from math import sqrt


letter = "aabbbbdssssdhhhhsssaaaahh"
fruits = ["apple", "banana", "orange", "apple",
          "apple juice", "banana", "orange", "watermelon"]

result_letter = Counter(letter)
result_fruits = Counter(fruits)
print(result_letter)
print(result_fruits)
print(result_letter.most_common())


# factory function
def default_factory():
    return 3


d = defaultdict(default_factory)
d["a"] = 1
d["b"] = 2
print(d["a"], d["b"], d["c"])

# factory function 使用lambda
Harry = defaultdict(lambda: "Wrong Key")
Harry["name"] = "Harry Potter"
Harry["age"] = 15
print(Harry["school"])


# namedtuple範例：
# 計算兩點距離的平方根
# EX1.普通做法
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
line_length = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
print(line_length)


# EX1.1.使用namedtuple
Point = namedtuple("Point", ["x", "y"])

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_length = sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
print(line_length)


# EX2.
# Namedtuple creates a class
Worker = namedtuple("Worker", ["job", "salary", "workplace"])

Ice = Worker("Engineer", 200000, "Taiwan")
print(type(Ice))
print(Ice)
print(Ice[0])
print(Ice.job)
