class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # 定義 一個 private method __key()
    def __key(self):
        return (self.name, self.age, self.address)

    # implement __hash__() function
    def __hash__(self):
        return hash(self.__key())

    # 比較兩個物件是否一樣，如果未使用 "__eq__" function會顯示false，
    # 因為存放的記憶體位址不一樣
    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented

    # 計算長度
    def __len__(self):
        return len(self.name)  # 也可以放self.age,self.address...等。

    # 輸出字串
    def __str__(self):
        return f"{self.name} is now {self.age} years old,living in {self.address}"

    # debug用

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, address: {self.address}"

    # 相加
    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented

    # 比大
    def __gt__(self, other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented


# 可以將robot 拿來當 key 範例：
robot = Robot("Ice", 18, "TW")
dictionary = {robot: "Ice"}
print(dictionary[robot])

# 比較兩個機器人是否一樣
robot1 = Robot("Ice", 18, "TW")
robot2 = Robot("Ice", 18, "TW")
print(robot1 == robot2)

print(len(robot1))
print(str(robot1))
print(robot1)  # 與上一行輸出相同
print(repr(robot1))
print(robot1 + robot2)
print(robot1 > robot2)
