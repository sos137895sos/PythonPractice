import random                 # 1. import moduleName
import random as rd           # 2. import moduleName as something
from random import *          # 3. from moduleName import *
# 4. from moduleName import oneFunction,anotherFunction,...
from random import randint


print(random.randint(0, 5))
print(rd.randint(6, 10))
print(randint(11, 15))  # 3,4 的return
