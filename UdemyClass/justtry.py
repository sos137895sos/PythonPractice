# 1.請將str1,str2中的c,C刪除 並將str1, str2合併
str1 = "abcde"
str2 = "ABCDE"

str1.replace("c", "")
str2.replace("C", "")

print(str1 + str2)

# 2.請在q2ans中加入元素"a","b"
q2ans = []

q2ans.append("a")
q2ans.append('b')

print(q2ans)


# 3.請將字典q3ans 依序加入 {"k1":"v1"} 跟 {"k2":"v2"}
q3ans = {"k0": "v0"}
q3ans["k1"] = "v1"
q3ans["k2"] = "v2"
print(q3ans)
# 4.取出list1中的元素 "b"
list1 = [["a", "b"], ["c", "d"]]
E_b = list1[0][1]

print(E_b)

# 5.請寫出一迴圈,算出ans5, ans5為1~1024的的總和


ans5 = 0
for i in range(1, 1025):
    ans5 += i

print(ans5)
