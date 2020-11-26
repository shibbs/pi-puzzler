FAIL = 0
PASS = 1

def level3():
    print("Perhaps that one was too easy. This time you’ll have to do a bit of reverse engineering. Check out the file external_levels.py - it’s somewhere around here…")
    resp = input()
    if resp == "R3v3rs3_3ngin33r":
        return PASS
    else:
        return FAIL

def level4( password_in ):
    index = 0
    if password_in[index:index+4] != "Swee":
        return FAIL
    index = 10
    if password_in[index + 6: 25] != "nksgiving":
        return FAIL
    if password_in[index:index+6] != "ForTha":
        return FAIL
    if password_in[index - 6: index] != "tGravy":
        return FAIL
    return PASS
