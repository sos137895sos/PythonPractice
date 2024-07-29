# LBYL approach
def safe_divide_1(x, y):
    if y == 0:
        print("Divide by 0 attempt detected.")
        return None
    else:
        return x / y


# EAFP (Easier to ask forgiveness than permission)
def safe_divide_2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Divide by 0 attempt detected.")
        return None


# 儲存文件的LBYL 與 EAFP的做法比較
# 這不是一個真正的codes寫法

# LBYL 需要想很多預期的錯誤
def save_a_file():
    result = save_prefs()
    if result == 'error':
        print("Preference not saved.")
        return
    result = save_text()
    if result == 'error':
        print("not enough memory")
        return
    result = save_format()
    if result == 'error':
        print("format not saved.")
        return
    

# EAFP 程式碼較為簡潔，先試再說
def save_a_file():
    try:
        save_prefs()
        save_text()
        save_format()
    except:
        print("something went wrong...")