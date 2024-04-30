# ex 數字平方 result:1 4 9 16
# 一般方法
# x = [1, 2, 3, 4]
# squared_x = []
# for item in x:
#     squared_x.append(item ** 2)
# print(squared_x)
# List Comprehensions :
# new_list= [operation for variable in original_list (if condition)]
# ex 數字平方 result:1 4 9 16
# x = [1, 2, 3, 4]
# squared_x = [item ** 2 for item in x]
# print(squared_x)
# Dictionary Comprehensions:
# new_dict = {key:value(operation) for variable in original_dict/list (if condition)}
# ex 數字平方，result:{1:1,2:4,3:9,4:16}
# x = [1, 2, 3, 4]
# x_squared_dict = {item: item ** 2 for item in x}
# print(x_squared_dict)
# Set Comprehensions:
# new_set = {operation for variable in original_set (if condition)}
# x = [1, 2, 3, 4]
# x_squared_set = {item**2 for item in x}
# print(x_squared_set)
# Generator Comprehensions:
# new_generator = (operation for variable in original_list (if condition))
# x = [1, 2, 3, 4]
# x_squared_generator = (item ** 2 for item in x)
# for i in x_squared_generator:
#     print(i)
