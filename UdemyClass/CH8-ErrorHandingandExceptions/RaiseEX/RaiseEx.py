class NegativeNumberException(RuntimeError):
    def __init__(self, age):
        super().__init__()  # 調用父類的構造函數
        self.age = age  # 將 age 賦值給實例屬性
        if age < 0:  # 如果年齡是負數
            print("This is not a valid age!")  # 打印錯誤信息

def enter_age(age):
    if age < 0:
        raise NegativeNumberException(age)
    
    if age % 2 == 0:
        print("Your age is an even number.")
    else:
        print("Your age is odd.")