# 做法一
class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25

    # 引用private property方式：
    def greet(self):
        print(f"Hi, I am {self.__age} years old.")


my_robot = Robot("Ice")
my_robot.greet()


# 做法2 不常見的做法
class Robot2:
    def __init__(self, name):
        self.name = name
        self.__age = 25

    # getter, setter

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age += 1


my_robot2 = Robot2("Icee")
my_robot2.set_age()
print(my_robot2.get_age())


# 做法3
class Robot3:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25

    # private method
    def __this_is_private(self):
        print("hello from private method.")

    def greet(self):
        print("hi im a robot")
        self.__this_is_private()


my_robot3 = Robot3("Iceee")
my_robot3.greet()
