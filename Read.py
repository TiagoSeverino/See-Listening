#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522.MFRC522
import socket
import signal
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.IN)
GPIO.setup(36, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)

os.chdir("/home/pi/See-Listening") #Read.py folder

continue_reading = True
lastUID = 0

lastRow = -1

input_data = ["Alcoholic beverages", 
              "Baby foods and baby-care", 
              "Breads and bakery products", 
              "Baking needs", 
              "Books, newspapers, and magazines", 
              "Bulk dried foods", "Alexander", 
              "Canned goods and dried cereals", 
              "CDs, audio cassettes, DVDs, and videos", 
              "Cigarettes and other tobacco", 
              "Confections and candies", 
              "Cosmetics", 
              "Dairy products and eggs", 
              "Delicatessen foods", 
              "Diet foods", 
              "Dressings and Sauces"]

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

#On New Data
def new_data(lastRow):
    row = 0 
    
    if GPIO.input(35):
        row += 1
    if GPIO.input(36):
        row += 2
    if GPIO.input(37):
        row += 4
    if GPIO.input(38):
        row += 8
    if lastRow != row:
        print row, " ", input_data[row]
        say(input_data[row])

    return row

def say(text):
    if internet:
        os.system('./speech.sh "' + text + '"')
    else:
        os.system('echo "' + text + '" | festival --tts')

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print "Connected"
        return True
    except Exception as ex:
        print "Not Connected to internet",  ex.message
        return False

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

time.sleep(10) #Wait for wifi connection
internet = internet()

# Welcome message
print "Welcome See-Listening"
print "Press Ctrl-C to stop."
say("Program Started!")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    try:
        if GPIO.input(40):
            lastRow = new_data(lastRow)
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK and lastUID != uid:
            
            lastUID = uid

            # Print UID
            print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            text = ""

            for x in range(6,37):
                data = MIFAREReader.MFRC522_Read(x)

                for nr in data[6:10]:
                    if nr != 0 and nr < 254:
                        text += chr(nr)
                        
            say(text)
            
            MIFAREReader.MFRC522_StopCrypto1()

    except Exception:
        print("Error Reading Product")
        say("Error Reading Product" )
        lastUID=0
