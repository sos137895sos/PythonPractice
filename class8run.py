e2f ={'dog':'chien','cat':'chat','walrus':'morse'}

f2e = {fr: eng for eng, fr in e2f.items()}
print(f2e['chien'])
e2f_eng = set(e2f.keys())
print(e2f_eng)

life = {
    'animals': {
        'cat':['Henri','Grumpy','Lucy'],
        'octopi':{},
        'emus':{}
        
    },
    'plants':{},
    'other' : {}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cat'])

squares = {x : x**2  for x in range(10)}
print(squares)
odd = {x for x in range(10)  if x % 2 !=0}
print(odd)

