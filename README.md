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
...* Write it soon

## 2. PiCamera
...* Write it soon

## 3. RFID
...* Write it soon

## 4. Sqlite 
4.1. Create DateBase
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

