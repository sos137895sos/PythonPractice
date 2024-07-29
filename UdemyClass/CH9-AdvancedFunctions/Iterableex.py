# iterable => 第1種做法 __iter__() method returns an iterator
# any generator is an iterator
class Something:
    def __iter__(self):
        yield 5
        for x in range(1, 4):
            yield x


s = Something()
# s is an iterable
# iter(iterable) return an iterator
print(iter(s))
for i in s:
    print(i)


# iterable => 第2種做法 implements __getitem__()
class Building(object):
    def __init__(self, floors):
        self.__floors = [None] * floors

    def __setitem__(self, floor_number, data):
        self.__floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self.__floors[floor_number]


building1 = Building(4)
building1[0] = 'Reception'
building1[1] = 'AVVC Corp'
building1[2] = 'DEF Inc'

for thing in building1:
    print(thing)

print(building1[0])
