# 1.Write a function called "mySort" that takes an list of integers as input,
# and returns the sorted version of the input list.
# You are not allowed to use the built-in sorted() function.
def findMin(lst):
    if len(lst) == 0:
        print("undefined")
        return "undefined"
    min_x = lst[0]
    for i in lst:
        if i < min_x:
            min_x = i
    return min_x


def mySort(myList):
    sort = []
    while len(myList) > 0:
        min_e = findMin(myList)
        sort.append(min_e)
        myList.remove(min_e)
    print(sort)
    return sort


mySort([17, 0, -3, 2, 1, 0.5])  # returns [-3, 0, 0.5, 1, 2, 17]
