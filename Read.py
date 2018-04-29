#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import ASUS.GPIO as GPIO
import MFRC522
import signal
import time
import http

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")

# Preper HTTP module to send request to the server
http = http.Http()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        GPIO.output(18, GPIO.LOW)
        # Print UID
        nfcid = ",".join(map(str,uid))
        print ("Card read UID: %s" % nfcid)
        res = http.post('posts', nfcid)
        res = res['data']['trackMyAss']
        if (res['ack']['ok']):
            print(res['ack']['message'])
            # TODO blinking flash 3 times fast
            for x in range(0,3):
                GPIO.output(18, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(18, GPIO.LOW)
                time.sleep(0.1)
        else:
            print(res['ack']['message'])
            # TODO blink 3 time slow
            for x in range(0,3):
                GPIO.output(18, GPIO.LOW)
                time.sleep(0.3)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(0.3)
        # This is the default key for authentication
        # key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        # MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        # status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        # if status == MIFAREReader.MI_OK:
            # MIFAREReader.MFRC522_Read(8)
            # MIFAREReader.MFRC522_StopCrypto1()
            # print (http.post('posts', '1,2,3,4'))

        # Kill execution for 10 seconds
        time.sleep(10)
