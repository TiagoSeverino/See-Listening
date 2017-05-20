See-Listening
==============

This project gives the opportunity to people with vision problems such as illiterates, low vision people or even blind people for example to go into the supermarket and with this device, be able to make their purchases autonomously.

This project is not finished yet and we'll keep improving it's functionalities.

Feel free to share, improve and give your opinion about this project.

## Awards
  - 3rd Place in Freebots Junior at Portuguese Robotics Open 2017.

## Demonstration
<a href="https://www.youtube.com/watch?v=Mw69nKu73a0" target="_blank"><img src="https://i.ytimg.com/vi/Mw69nKu73a0/hqdefault.jpg" 
alt="Robocup Rescue Maze Robot" width="480" height="360" border="10" /></a>

## Requirements

  - [SPI-Py](https://github.com/lthiery/SPI-Py)

  - [Text To Speech](http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)):
    * Supporting packages
    * Festival Text to Speech
    * Google Text to Speech

If you want to run the program at boot:

    cd /etc
    sudo nano rc.local

Add those lines before "exit 0":

    cd ~/See-Listening/
    ./launch &