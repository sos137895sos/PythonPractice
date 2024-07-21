class Thing():
    pass
print(Thing)
example = Thing()
print(example)
class Things2:
    letters = 'abc'
print(Things2.letters)

class Thing3:
    def __init__(self) :
        self.letters = 'xyz'
example = Thing3()
print(example.letters)

class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self) :
        print(f"Name:{self.name},Symbol:{self.symbol},Number:{self.number}")
hydrogen = Element('Hydrogen','H',1)
hydrogen.dump()

