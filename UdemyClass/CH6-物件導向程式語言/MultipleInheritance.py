# 簡單語法介紹： A繼承C、D
# class C:
#     def do_stuff(self):
#         print("hello from class C")


# class D:
#     def do_another_stuff(self):
#         print("hello from class D")


# class A(C, D):
#     pass


# a = A()
# a.do_stuff()
# a.do_another_stuff()


# A繼承B、C、D，B繼承E、F，D繼承G
class E:
    pass


class F:
    def do_stuff(self):
        print("doing stuff from F")


class G:
    def do_stuff(self):
        print("doing stuff from G")


class B(E, F):
    pass


class C:
    def do_stuff(self):
        print("doing stuff from C")


class D(G):
    pass


class A(B, C, D):
    pass


a = A()
a.do_stuff()
print(A.mro())
print(A.__mro__)
