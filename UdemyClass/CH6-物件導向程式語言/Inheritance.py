class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating food")


class Student(People):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def sleep(self):
        print(f"{self.name} is sleeping...")

    def eat(self, food):
        print(f"{self.name} is now eating {food}")  # 可以覆寫上面的eat函式


student_one = Student("Ice", 18, 154)
student_one.sleep()
student_one.eat("beef")
print(student_one.age, student_one.student_id)
