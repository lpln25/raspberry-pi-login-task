# raspberry-pi-login-task

This Project can help you to create `login system` with ID (tag-rfid) and then with three tag-rfid, we could `run three Task` :
1. Take picture
2. Get video
3. Timer"

Library :
○ RFID
○ PiCamera
○ Sqlite3
○ GPIO
○ DateTime
○ threading

## Pieces

![Raspberry pi zero - RFID - Picamera - LED ](http://s8.picofile.com/file/8364366234/result.jpg)

## Create Project Main and Install library
1. update our Raspberry Pi 
~~~python
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-dev python3-pip
sudo pip3 install spidev
~~~
2. install the MFRC522 library
~~~python
sudo pip3 install mfrc522
~~~
3. install the Sqlite3 library
~~~python
sudo apt-get install sqlite3
~~~
4. install the PiCamera library
~~~python
sudo pip install picamera
~~~

## 1. LED
Test part of LED to do show ending process of task
~~~python
import RPi.GPIO as GPIO
import time

def notification():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(18,GPIO.LOW)
    #GPIO.cleanup()
~~~

## 2. PiCamera
1. Capture Image
~~~python
import PiCamera
def capture_():
    camera = picamera.PiCamera()
    camera.capture('name.jpg')
    camera.close()
~~~
2. Record Video
~~~python
import PiCamera
def video_():
    camera = picamera.PiCamera()
    camera.start_recording('name.h264')
    time.sleep(5)
    camera.stop_recording()
    camera.close()

~~~

## 3. RFID
~~~python
from  mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
Id, Value = reader.read()
~~~

## 4. DateTime 

~~~python
from datetime import datetime
def timeNow():
    DT = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #DT = datetime.now().strftime('%Y-%m-%d')
    return DT
    
~~~

## 5. Sqlite 
1. Create DataBase in shell of command then use it
~~~python
$ sqlite3 datebase.db
~~~
~~~python
sqlite> CREATE TABLE `log` (
	`Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Value`	TEXT DEFAULT 'Default',
	`DateTime`	TEXT DEFAULT 'Time'
);
~~~
~~~python
sqlite> .exit
~~~
2. The code of insert row in `datebase.db`
to help get time-now of system, use `timeNow()`
~~~python
import sqlite3

def insert_():
    DateTime = timeNow()
    Value = log
    query = "insert into [log] (Value,DateTime) Values ('"+Value +"','"+ DateTime+"');"
    con=sqlite3.connect(constring)
    cm = con.cursor()
    cm.execute(query)
    con.commit()
    con.close()
~~~

## 6. Timer
The timer will counting to 5 hours and then stop
this Function help `reset_timer()` to reset the `timer()`
~~~python
def reset_timer():
    mm = 0
    hh = 0
    ss = 0
    
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

~~~

## 7. Hash and cryptography 
...* Write it soon

## 8. Main Script 
~~~python
ID_ = "[your id tag-RFID]"
user = "[user name]"
value1 = 10 # task one (value of tag RFID)
value2 = 20 # task two (value of tag RFID)
value3 = 30 # task three (value of tag RFID)

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
    log = "Login " + user
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
            #print("timer")
            notification()
            if not tr_timer.is_alive():
                tr_timer.start()
            else:
                tr_timer.start()
        

print ("\n==> turn off system")
~~~

## 9. Auto run code after reboot raspberry pi
First save Script with name `main.py`, then add it in the ` crontab ` file
~~~python
$ sudo crontab -e
~~~
~~~python
@reboot python3 /home/pi/main.py
~~~
To Save it press `^X` then press `Y`

## 10. Thanks
So Thanks from my teacher (Mis ` Yasamin Salem `) that She was inspiring me.



