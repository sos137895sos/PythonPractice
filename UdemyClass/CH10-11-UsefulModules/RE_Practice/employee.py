import re
import os

# 搜尋單一文件裡的電話號碼
with open("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/RE_Practice/Employee/Manager/NewYork.txt", encoding="utf8") as nyk:
    nyktxt = nyk.read()
    # print(nyktxt)
nyktele = re.findall(r"[0-9]{3,}+\-[0-9]{3,}+\-[0-9]{4,}", nyktxt)
print(nyktele)


# 搜尋Employee 裡所有文檔裡的電話然後儲存成一個list
result = []  # 創建一個空list


def search(st):  # 創建一個搜尋電話的function
    r = re.findall(r"[0-9]{3,}+\-[0-9]{3,}+\-[0-9]{4,}", st)
    if r:
        for number in r:
            result.append(number)


# 搜尋整個資料夾
for folder, subfolder, files in os.walk("/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH10-11-UsefulModules/RE_Practice/Employee"):
    for f in files:
        with open(os.path.join(folder, f), encoding="utf8") as my_file:
            text = my_file.read()
            search(text)
print(result)
