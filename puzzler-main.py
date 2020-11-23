
FAIL = 0
PASS = 1

def level0():
    print('welcome to level 0')
    resp = raw_input()
    print('your response was' + resp)
    if resp == "n00b":
        return PASS
    else:
        return FAIL

def level1():
    print('welcome to level 1')
    resp = raw_input()
    return PASS

def insult_generator():
    return "Seriously!?"



print("Welcome to Steve puzzle box! Let's begin the puzzling...")

while level0() != PASS:
    print(insult_generator())
level1()
