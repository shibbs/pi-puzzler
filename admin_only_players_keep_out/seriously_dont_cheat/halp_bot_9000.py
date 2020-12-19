
def generate_help(level):
    print("\n")
    if(level <= 1):
        print("Dude, just type in n00b and then hit enter")
    elif level == 2:
        print("For this one, you'll need to use open up the file level2.txt with the nano command. For some help, try typing nano helpful_commands.txt into another command prompt.")
        print("If nano helpful_commands.txt doesn't open a file, you are either not in a separate command prompt, or you are in the wrong directory, in which case you're in a bit of a pickle. I am a HelpBot, not a miracle worker...")
    elif level == 3:
        print("Use the skills from level 2 to check out the file levels3_and_4.py. Take a look around and see what level 3 may be doing")
    elif level == 4:
        print("Same trick as level 3, but a trickier trick this time")
    elif level == 5:
        print("nano can open files as text, but other commands can open files of different types...")
    elif level == 6:
        print("You've only learned a couple of tricks so far, so use them")
    elif level == 7:
        print("Hmm, this is a tough one. If you really want help, type in halp2, but I recommend sweating it out and using the tricks you've learned so far")
    elif level == 8:
        print("check out the command omxplayer")
    elif level == 9:
        print("did you know that nano lets you edit files?")
    elif level == 10:
        print("Hmm, which of these folders couldn't exist in the real world?")
    elif level == 11:
        print("gotta use the internets for this one, there are commands that'll do what you want")
    elif level == 12:
        print("gotta use the internets for this one, there are commands that'll do what you want")
    elif level == 13:
        print("Check out sudo raspi-config")
    elif level == 14:
        print("For this trick, you'll have to run the correct python file. But there seems to be something wrong with it...For more hep ask halp2")
    elif level == 15:
        print("That link looks like it points to a git repository. I wonder how to clone those...")
    elif level == 16:
        print("Hmm, looks like there's a way to decode arbitrary stuff with this decode_message function")
    elif level == 17:
        print("Looks like there's more than one function in there, how to run it and get the output tho?")
    elif level == 18:
        print("It looks like this is a caesar cipher that currently shifts by 1 character...")
    elif level == 19:
        print("Hmm, this first line makes an S, but what's up with the other stuff? Looks like a bunch of different data types")
    elif level == 20:
        print("this is where you earn your stripes. There are plenty of ways to win")
    elif level == 21:
        print("You're all done, i have nothing left to teach, get out of here")
    else:
        print("Halpbot not enabled for this level. Shame on the game master")
