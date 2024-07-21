import pickle


# 序列化，基本語法
# x = 10
# y = [1, 2, 3, 5]

# with open("pickle_file", "wb") as p_file:
#     pickle.dump(x, p_file)
#     pickle.dump(y, p_file)

# 反序列化 讀取資料，基本語法
# with open("pickle_file", "rb") as p_file:
#     print(pickle.load(p_file))
#     print(pickle.load(p_file))


# 常見寫法:新存進dictionary裡再存進pickle

# x = 10
# y = 100
# my_list = [1, 2, 3, 4, 10]


# def save_data():
#     global x, y, my_list
#     data = {'x': x, 'y': y, "my_list": my_list}

#     with open("my_pickle_file", "wb") as pfile:
#         pickle.dump(data, pfile)


# save_data()


# 讀取
x = None
y = None
my_list = None


def restore_data():
    global x, y, my_list
    with open("my_pickle_file", "rb") as pfile:
        data = pickle.load(pfile)
        x = data['x']
        y = data['y']
        my_list = data['my_list']


restore_data()
print(x, y, my_list)
