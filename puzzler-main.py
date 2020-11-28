from external_levels import *
import random

FAIL = 0
PASS = 1

insults_array = ["Seriously!?", "I expected better", "This is going even worse than they said it would", "I'm a bit embarassed we're still doing this", "Weak_sauce", "N00B"]

def level1():
    print('welcome to level 1. The password for this one is just n00b')
    resp = input()
    print('your response was' + resp)
    if resp == "n00b":
        return PASS
    else:
        return FAIL

def level2():
    print('welcome to level 2. The password for this one is hanging out in a file called level2.txt')
    resp = input()
    f = open("level2.txt", "r")
    pw = f.readline()
    pw = pw.rstrip()
    f.close()
    # print(pw)
    if resp == pw:
        return PASS
    else:
        return FAIL

def level4_local():
    print('Ok, this one’s for real. Now you actually need to crack some code, check out the level4 function you used for the last level')
    resp = input()
    return level4( resp )


def level5():
    print('That one was actually kind of tricky. Enough of that CS stuff, now let’s play with the command line a bit. If you poke around, there’s a file called “level5.png”. Turns out this thing can show pictures with a command called fbi... ')
    resp = input()
    if (resp == "level5_pw"): #SAH - need to update this pw depending on what picture we use
        return PASS
    else:
        return FAIL
def level6():
    print("All right, nice work. This one is a bit trickier- there is a file around for this level but extensions aren't always what they seem")
    resp = input()
    if (resp == "bait_and_switch"): #SAH - need to update this pw depending on what picture we use
        return PASS
    else:
        return FAIL
def level7():
    print('This one is a bit funky. Turns out there are many ways to hide text in pictures- check out level7.png')
    resp = input()
    if (resp == "HELP_IM_TRAPPED_IN_THIS_PHOTO"): #SAH - need to update this pw depending on what picture we use
        return PASS
    else:
        return FAIL
def level8():
    print("All right let's get multimedia in here. Turns out you can play audio files with these things...")
# We need a level8.mp3 file to play
    resp = input()
    if (resp == "mixmaster"): #SAH - need to update this pw depending on what audio file we create
        return PASS
    else:
        return FAIL

def insult_generator():
    index = len(insults_array)
    index = random.randint(0, index-1)
    return insults_array[index]

def save_level(level_to_save):
    f = open("max_level.txt", "w")
    level = f.write(str(level_to_save))
    print("New level Saved: " + str(level_to_save))
    f.close()

def leveln( level_num):
    if(level_num <= 1):
        return level1()
    if(level_num == 2):
        return level2()
    if(level_num == 3):
        return level3()
    if(level_num == 4):
        return level4_local()
    if(level_num == 5):
        return level5()
    if(level_num == 6):
        return level6()
    if(level_num == 7):
        return level7()
    if(level_num == 8):
        return level8()


print("Welcome to Steve puzzle box! Let's begin the puzzling...")
f = open("max_level.txt", "r")
level = f.readline()
f.close()
level = int( level.rstrip() )
print("Your current level is "+str(level))

random.seed(None, 2)


while 1==1 :
    if leveln(level) == PASS:
        level = level+1
        save_level(level)
    else:
        print(insult_generator())
