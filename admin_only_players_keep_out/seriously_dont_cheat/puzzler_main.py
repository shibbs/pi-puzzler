from external_levels import *
import sys
sys.path.insert(0, '../../')
from main_code_base_stay_out import *
from halp_bot_9000 import *
import random
import os.path
from os import path

FAIL = 0
PASS = 1
HELP = 2

insults_array = ["Seriously!?", "I expected better", "This is going even worse than they said it would", "I'm a bit embarassed we're still doing this", "Weak_sauce", "N00B"]


def insult_generator():
    index = len(insults_array)
    index = random.randint(0, index-1)
    return insults_array[index]

def save_level(level_to_save):
    f = open("admin_only_players_keep_out/seriously_dont_cheat/max_level.txt", "w")
    level = f.write(str(level_to_save))
    print("New level Saved: " + str(level_to_save))
    f.close()

def puzzle_time():
    print("Welcome to Steve's puzzle box! Don't forget about the handy commands scratchpad, and that HelpBot is always a halp away. Let's begin the puzzling...")
    f = open("admin_only_players_keep_out/seriously_dont_cheat/max_level.txt", "r")
    level = f.readline()
    f.close()
    level = int( level.rstrip() )
    print("Your current level is "+str(level))

    random.seed(None, 2)

    while 1==1 :
        print('\n')
        result = leveln(level)
        if result == PASS:
            level = level+1
            save_level(level)
        if result == HELP:
            generate_help(level)
        if result == FAIL:#else FAIL
            print(insult_generator())
