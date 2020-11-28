from external_levels import *
import random
import os.path
from os import path

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
    print('welcome to level 2. The password for this one is hanging out in a file called level2.txt. I recommend checking out nano, like whatever that is AIMRITE!?')
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
    print('That one was actually kind of tricky, not bad. Enough of that CS stuff, now let’s play with the command line a bit. If you poke around, there’s a file called “level5.png”. Turns out this thing can show pictures with a command called fbi... ')
    resp = input()
    if (resp == "IN_VISIBLE"):
        return PASS
    else:
        return FAIL
def level6():
    print("Level 6, nice work. This one is a bit trickier- there is a file around for this level but extensions aren't always what they seem")
    resp = input()
    if (resp == "bait_and_switch"):
        return PASS
    else:
        return FAIL
def level7():
    print("Welcome to Level 7. I won't pretend I'm not a little surprised to see you've made it this far This one is a bit funky, good luck")
    resp = input()
    if (resp == "HIDDEN_MEANINGS"): #SAH - need to update this pw depending on what picture we use
        return PASS
    else:
        return FAIL
def level8():
    print("All right let's get multimedia up in this bitch. Turns out you can play audio files with these things...")
    resp = input()
    if (resp == "bad_santa"):
        return PASS
    else:
        return FAIL
def level9():
    print("All Right, welcome to Level9. To proceed onto the next level, you'll have to edit the correct file to have 'first_emo_best_emo' as the very first line. Hit Enter when you're ready for me to check your work")
    resp = input()
    f = open("why_is_it_called_a_folder_if_I_cant_fold_it/level9.txt", "r")
    pw = f.readline()
    pw = pw.rstrip()
    f.close()
    if (pw == "first_emo_best_emo"):
        return PASS
    else:
        return FAIL
def level10():
    print("Well that was cute, but do you know how to make a file from scratch? I'll be looking for a level10.txt file to appear where one might least expect to find a folder...")
    resp = input()
    #we're looking for level10.txt to show up in an_unfoldable_folder
    if (path.exists("an_unfoldable_folder/level10.txt") ):
        return PASS
    else:
        return FAIL
def level11():
    print("Well fair enough, now you’ve gotta transport that file into a folder called magic_portal")
    resp = input()
    if (path.exists("magic_portal/level10.txt") ):
        if (path.exists("an_unfoldable_folder/level10.txt") ):
            print("it's a magic portal, not a magic photocopier")
            return FAIL
        else:
            return PASS
    else:
        return FAIL
def level12():
    print("This level not yet built. Shame on the game master")
    resp = input()
    if (resp == "XX"):
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
    if(level_num == 9):
        return level9()
    if(level_num == 10):
        return level10()
    if(level_num == 11):
        return level11()
    if(level_num == 12):
        return level12()


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
