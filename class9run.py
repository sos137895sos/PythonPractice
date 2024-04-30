def agree():
    return False
if agree():
    print('Splendid!')
else:
    print('ahahahahah')
def echo(anything):
    return anything + ' ' + anything
print(echo(''))

def commentary(color):
    if color == 'red':
        
        return "tomato"
    elif color == 'green':
        return "green papper"
    elif color == 'bee purple':
        return "Idontknow"
    else:
        return "ive never heard of the color " + color + "."
print(commentary(''))

def donothing():
    pass
print(donothing())

def good():
    return ['Harry','Ron','Hermione']
result = good()
print(result)

class OopsException(Exception):
    pass
try:
    raise OopsException
except OopsException :
    print("Caught an oops")
