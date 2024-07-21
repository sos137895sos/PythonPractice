import shelve


# 語法範例：儲存資料
# int1 = [1, 2, 3, 4, 5, 7]
# int2 = [3, 5, 6, 99]
# int3 = [1000, 20000, 3000000, 40000000]

# with shelve.open("shelf-example", "c") as shelf:
#     shelf['integers1'] = int1
#     shelf['integers2'] = int2
#     shelf['integers3'] = int3


# 讀取資料
with shelve.open("shelf-example", "r") as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf["integers1"])
    print(shelf["integers2"])
    print(shelf["integers3"])
