#!/usr/bin/env python
import RPi.GPIO as GPIO
from  mfrc522 import SimpleMFRC522
import picamera
import time
import threading
from datetime import datetime
import sqlite3

#********************
#      variable
#********************
# Flag
flag_Timer = False
# Time
hh = 0
mm = 0
ss = 0
maxHH = 5
# user
user = "Persian Mehr"
# Adress File
addressImage = "/home/pi/Image/"
addressVideo = "/home/pi/Video/"
# Database
constring = "datebase.db"
log = ""
# Id login
ID_ = '766156045529'
# Values Task
value1 = 10
value2 = 20
value3 = 30

#********************
#      function
#********************
# get time now
def timeNow():
    DT = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #DT = datetime.now().strftime('%Y-%m-%d')
    return DT

# reset timer
def reset_timer():
    mm = 0
    hh = 0
    ss = 0

# capture image
def capture_():
    name = addressImage + timeNow() + ".jpg"
    camera = picamera.PiCamera()
    camera.capture(name)
    camera.close()

# record video
def video_():
    name = addressVideo + timeNow() + ".h264"
    camera = picamera.PiCamera()
    camera.start_recording(name)
    time.sleep(5)
    camera.stop_recording()
    camera.close()

# record log
def insert_():
    DateTime = timeNow()
    Value = log
    query = "insert into [log] (Value,DateTime) Values ('"+Value +"','"+ DateTime+"');"
    con=sqlite3.connect(constring)
    cm = con.cursor()
    cm.execute(query)
    con.commit()
    con.close()

#  LED 18 notification for user
def notification():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(18,GPIO.LOW)
    #GPIO.cleanup()

# get Time
def timer():
    while flag_Timer :
        ss += 1
        if ss > 59 :
            mm = mm+1
            ss = 0
        if mm > 59 :
            hh += 1
            mm = 0
        if hh >= maxHH :
            #1 flag
            #2 notification
            #3 insert log
            flag_Timer = False
            log = "Pass 5:00:00 Hour"
            insert_()
            reset_timer()

#********************
#      main
#********************
if __name__ == "__main__" :
    log = "Turn on"
    insert_()
    notification()
    reader = SimpleMFRC522()
    # Login Loop
    while True :
        print("ID card: ")
        id_,vl= reader.read()
        if str(id_) == ID_ :
            notification()
            print("Succesful Login\n")
            break
        else:
            print("wrong ID! \n")
    
    # task Loop
    #1 notificaition
    #2 insert log time login
    #3 read tag task
    log = "Login "+user
    insert_()
    notification()
    
    tag = 0
    while True :
        print("task card:::: ")
        notification()
        id_,tag = reader.read()
        if ID_ == str(id_):
            # jump out from this loop
            log = "sign out"
            insert_()
            notification()
            break
        elif value1 == int(tag):
            # capture
            capture_()
            notification()
        elif value2== int(tag):
            # video
            video_()
            notification()
        elif value3== int(tag):
            # timer
            notification()
            if not tr_timer.is_alive():
                tr_timer.start()
            else:
                tr_timer.start()
        

print ("\n==> turn off system")
