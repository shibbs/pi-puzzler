# pi-puzzler
steve's puzzle box set built in python 3 and meant to create a little bootable puzzle set for a raspberry pi. There are some bashrc scripts that need to go along with this to ensure that it opens up on startup. but I'll prolly clean some of this info out to make sure that we don't give too much away to the participants

To start playing type in python3 run_this.py

As is tradition, this readme will rapidly become out of date, but right now there are a few notes: 
there is a file called max_level.txt that saves your level so you don't have to input a million passwords as you go. Set it to 1 to start at the beginning. Technically you can cheat by just changing that file so we'll have to lock that down a bit longer term

TODO:
Hide/encrypt the max_level.txt file somehow
Obfuscate/compile the puzzeler-main file, or stop hiding passwords in cleartext somehow
finish all of the levels, obviously
Add more insults, obviously
