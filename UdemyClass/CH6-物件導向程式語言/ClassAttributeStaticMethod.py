class Robot:
 # 可以在classes添加文字檔字串(doctring):
    """Robot class is for createing robots"""
    ingredient = "metal"  # 設定類別屬性

    def __init__(self, inputname, inputage):
        self.name = inputname
        self.age = inputage

    # --------定義method------
    def walk(self):
        print(f"{self.name} is walking...")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours. ")

    def greet(self):
        print(
            f"HI, my name is {self.name}, and I am made of {self.__class__.ingredient}.")

    # 使用 Static Method
    @staticmethod
    def greet1():
        print("A robot says hi....")


my_robot_1 = Robot("Ice", 5)
my_robot_2 = Robot("Icee", 1)
my_robot_1.greet()
my_robot_2.greet()
Robot.greet1()
my_robot_1.__class__.greet1()

# 查看類別屬性的方式：
print(Robot.ingredient)
print(my_robot_1.ingredient)
print(my_robot_1.__class__.ingredient)
