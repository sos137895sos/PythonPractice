# for loop 語法：
#  for variable in iterable(String,list 任何東西都可):
#      do somthing here.
# ex1:
# for letter in "Hello World":
#     if (letter == letter.upper()):
#        print(letter)
# ex2
# myList = [1, 3, 5, 7, 9]
# for num in myList:
#     print(num ** 2)
#  a list of tuples
# ex1:
# for tuple in [(1, 2), (3, 5), (5, 7)]:
#     print(tuple)
# # ex2
# for a, b in [(1, 2), (3, 5), (5, 7)]:
#     print(a, b)
# # ex3
# for a, b in [(1, 2), (3, 5), (5, 7)]:
#     print(a + b)
# dictionary (keys)
# ex1
# myDictionary = {"name": "Ice", "age": "25"}

# for item in myDictionary.items():
#     print(item)
# for key, value in myDictionary.items():
#     print(f"The key is {key}")
#     print(f"The value is {value}")
# set
# for i in {1, 3, 5, 7, 9}:
#     print(i)
# while Loop(要設定限制不然會一直重複執行)語法：whie True/False:
#       do somthing here.
# ex
# x = 0
# while x < 5:
#     print(x)
#     x += 1 (必須加入這個限制不然會無限重複執行)
# nested loop 巢狀迴圈
# ex
# counter = 0

# for i in "1234":
#     for j in "abcdefg":
#         print(i, j)
#         counter += 1
# print(f"counter is now {counter}")
# 總共執行 4X7=28次
