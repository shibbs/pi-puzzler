# pi-puzzler
steve's puzzle box set built in python 3 and meant to create a little bootable puzzle set for a raspberry pi. There are some bashrc scripts that need to go along with this to ensure that it opens up on startup. but I'll prolly clean some of this info out to make sure that we don't give too much away to the participants

To start playing type in python3 run_this.py

overhead to do on the pi:
update pip: sudo -H pip3 install --upgrade pip
set the password
set the bashrc file: sudo nano /home/pi/.bashrc
  Go to the last line of the script and add:
  cd ~/Documents/pi-puzzler
install fbi: sudo apt-get update    sudo apt-get -y install fbi

As is tradition, this readme will rapidly become out of date, but right now there are a few notes:
there is a file called max_level.txt that saves your level so you don't have to input a million passwords as you go. Set it to 1 to start at the beginning. Technically you can cheat by just changing that file so we'll have to lock that down a bit longer term

TODO:
Add more insults, obviously
