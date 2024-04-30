# Pass可以用在loop,if...(),functions,classes.
# ex1 result:hi
# for i in "How are you":(加了pass所以不會做任何事)
#     pass
# print("hi")
# ex2 (因為True會被執行所以不會出現任何東西),result :
# if True:
#     pass
# else:
#     print("hi")
# BREAK------
# ex1 result=1234
# print("Before the for loop")

# for i in "123456789":
#     if i == "5":
#         break
#     else:
#         print(i)

# print("After the for loop")
# 巢狀迴圈break
# ex2 result= 1a 1b 2a 2b 3a 3b 4a 4b
# for i in "123456789":
#     if i == "5":
#         break  # 到5就不執行
#     for j in "abcdefg":
#         if j == "c":
#             break  # 到C就不執行
#         print(i, j)
# Continue----強制執行下一個順序,continue底下的code不會被執行
# ex1 result= ACDE
# for i in "ABCDE":
#     if i == "B":
#         continue
#     print(i)
# ex2
# for i in "ABCDE":
#     print("我是" + i)
#     continue
#     print("我在contiune的後面") #不會被執行，因為在上一行continue就被跳過了
