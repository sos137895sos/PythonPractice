import RaiseEx

try:
    num = -1
    RaiseEx.enter_age(num)
except RaiseEx.NegativeNumberException as error:
    print(error)
except:
    print("unknow error")
