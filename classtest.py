value = 0

def first():
    global value 
    value += 53
    print(value)

def second():
    print(value)

first()
second()