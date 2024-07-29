# 內建命名空間
print(len)  # <built-in function len>

# 全域命名空間
x = 'global'


def outer():
    # 內部命名空間
    x = 'outer'

    def inner():
        # 局部命名空間
        x = 'inner'
        print(x)  # inner

    inner()
    print(x)  # outer


outer()
print(x)  # global
