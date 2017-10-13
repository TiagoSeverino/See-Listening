See-Listening
==============

This project gives the opportunity to people with vision problems such as illiterates, low vision people or even blind people for example to go into the supermarket and with this device, be able to make their purchases autonomously.

This project is not finished yet and we'll keep improving it's functionalities.

Feel free to share, improve, give your opinion and ideas about the future of this project.

## Awards
  - 2nd Place in the 14th edition of the Ilídio Pinho Foundation "Science in the School Award"
  - 3rd Place in Freebots Junior at Portuguese Robotics Open 2017.

## Demonstration
<a href="https://www.youtube.com/watch?v=seoem99iT20" target="_blank"><img src="https://i.ytimg.com/vi/Mw69nKu73a0/hqdefault.jpg" 
alt="Robocup Rescue Maze Robot" width="480" height="360" border="10" /></a>

## Requirements

    git clone --recursive https://github.com/TiagoSeverino/See-Listening

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
