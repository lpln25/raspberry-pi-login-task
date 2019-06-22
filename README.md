# raspberry-pi-login-task
raspberry pi - login RFID and multi task

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
...* Write it soon

## 4. Sqlite 
1. Create DateBase
~~~python
CREATE TABLE `log` (
	`Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Value`	TEXT DEFAULT 'Default',
	`DateTime`	TEXT DEFAULT 'Time'
);
~~~

## 5. DateTime 
...* Write it soon

## 6. Hash and cryptography 
...* Write it soon

## 7. Main Script 
...* Write it soon

I create login with ID (tag-rfid) and then with tag-rfid run 3 work like "take picture" and "get video" and "timer"
so Thanks from my teacher (Salem Yasamin).

