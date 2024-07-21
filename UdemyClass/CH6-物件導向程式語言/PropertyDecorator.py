class Employee:
    def __init__(self):
        self.income = 0
        self.__tax = 0

    def earn_money(self, money):
        self.income += money
        self.__tax = self.income * 0.05

    def get_tax(self):
        return self.__tax


ice = Employee()
ice.earn_money(100000)
print(ice.get_tax())

ice.earn_money(150000)
print(ice.get_tax())


# @property decorator做法較不佔記憶體以及簡化code
class Employee2:
    def __init__(self):
        self.income = 0

    def earn_money(self, money):
        self.income += money

    @property
    def tax_amount(self):
        return self.income * 0.05

    # 設定virtual property的值
    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20


icee = Employee2()
icee.earn_money(50000)
print(icee.tax_amount)  # tax_amount是一個虛擬property，僅能讀取
icee.tax_amount = 5000
print(icee.income)
