#import linecache
#
import os
import time
import re
from datetime import datetime
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)



#caratteri custom

LT = (
  0b00111,
  0b01111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
)

UB = (
  0b11111,
  0b11111,
  0b11111,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000
)

RT = (
  0b11100,
  0b11110,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
)

LL = (
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b01111,
  0b00111
)

LB = (
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111,
  0b11111
)

LR = (
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11110,
  0b11100
)

MB = (
  0b11111,
  0b11111,
  0b11111,
  0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b11111
)


#codice block sostituito da lcd.write(0b11111111)
block = (
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
)



lcd.create_char(0, LT)
lcd.create_char(1, UB)
lcd.create_char(2, RT)
lcd.create_char(3, LL)
lcd.create_char(4, LB)
lcd.create_char(5, LR)
lcd.create_char(6, MB)
lcd.create_char(7, block)

#x indica la posizione del carattere a dx o sx

#definizione numeri da zero a 9
def custom0(x):
    lcd.cursor_pos = (0, x)
    lcd.write(0)
    lcd.write(1)
    lcd.write(2)
    lcd.cursor_pos = (1, x)
    lcd.write(3)
    lcd.write(4)
    lcd.write(5)

def custom1(x):
    lcd.cursor_pos = (0, x)
    lcd.write(1)
    lcd.write(2)
    lcd.write_string(" ")
    lcd.cursor_pos = (1, x)
    lcd.write(4)
    lcd.write(0b11111111)
    lcd.write(4)

def custom2(x):
    lcd.cursor_pos = (0, x)
    lcd.write(6)
    lcd.write(6)
    lcd.write(2)
    lcd.cursor_pos = (1, x)
    lcd.write(3)
    lcd.write(4)
    lcd.write(4)

def custom3(x):
    lcd.cursor_pos = (0, x)
    lcd.write(6)
    lcd.write(6)
    lcd.write(2)
    lcd.cursor_pos = (1, x)
    lcd.write(4)
    lcd.write(4)
    lcd.write(5)

def custom4(x):
    lcd.cursor_pos = (0, x)
    lcd.write(3)
    lcd.write(4)
    lcd.write(0b11111111)
    lcd.cursor_pos = (1, x)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(0b11111111)

def custom5(x):
    lcd.cursor_pos = (0, x)
    lcd.write(3)
    lcd.write(6)
    lcd.write(6)
    lcd.cursor_pos = (1, x)
    lcd.write(4)
    lcd.write(4)
    lcd.write(5)

def custom6(x):
    lcd.cursor_pos = (0, x)
    lcd.write(0)
    lcd.write(6)
    lcd.write(6)
    lcd.cursor_pos = (1, x)
    lcd.write(3)
    lcd.write(4)
    lcd.write(5)

def custom7(x):
    lcd.cursor_pos = (0, x)
    lcd.write(1)
    lcd.write(1)
    lcd.write(2)
    lcd.cursor_pos = (1, x)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(0b11111111)

def custom8(x):
    lcd.cursor_pos = (0, x)
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.cursor_pos = (1, x)
    lcd.write(3)
    lcd.write(4)
    lcd.write(5)

def custom9(x):
    lcd.cursor_pos = (0, x)
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.cursor_pos = (1, x)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(0b11111111)

def print_play():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.write_string(" ")
    lcd.write(0b11111111)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.write_string(" ")
    lcd.write(0)
    lcd.write(4)
    lcd.write(2)
    lcd.cursor_pos = (1, 0)
    lcd.write(3)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(3)
    lcd.write(4)
    lcd.write(4)
    lcd.write_string(" ")
    lcd.write(3)
    lcd.write_string(" ")
    lcd.write(5)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(0b11111111)
    time.sleep(2)
    lcd.clear()



def print_stop():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write(0)
    lcd.write(6)
    lcd.write(6)
    lcd.write_string(" ")
    lcd.write(1)
    lcd.write(0b11111111)
    lcd.write(1)
    lcd.write_string(" ")
    lcd.write(0)
    lcd.write(1)
    lcd.write(2)
    lcd.write_string(" ")
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.cursor_pos = (1, 0)
    lcd.write(4)
    lcd.write(4)
    lcd.write(5)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(0b11111111)
    lcd.write_string(" ")
    lcd.write_string(" ")
    lcd.write(3)
    lcd.write(4)
    lcd.write(5)
    lcd.write_string(" ")
    lcd.write(3)
    time.sleep(2)
    lcd.clear()

#prima input carattere da stampare, secondo posizione
def printDigits(digits,x):
    if digits == 0:
       custom0(x);
    elif digits == 1:
       custom1(x);
    elif digits == 2:
       custom2(x);
    elif digits == 3:
       custom3(x);
    elif digits == 4:
       custom4(x);
    elif digits == 5:
       custom5(x);
    elif digits == 6:
       custom6(x);
    elif digits == 7:
       custom7(x);
    elif digits == 8:
       custom8(x);
    elif digits == 9:
       custom9(x);

def print_time():
    ore = datetime.now().strftime('%H')
    minuti = datetime.now().strftime('%M')
    ore = list(map(int, ore))
    minuti = list(map(int, minuti))
    printDigits(ore[0],0)
    printDigits(ore[1],3)
    lcd.cursor_pos = (0, 6)
    lcd.write_string('.')
    lcd.cursor_pos = (1, 6)
    lcd.write_string('.')
    printDigits(minuti[0],7)
    printDigits(minuti[1],10)

def print_volume(volume):
    volume = int(volume)
    #print(volume)
    if volume == 0:
        volume_s = 0
    elif 1 <= volume <= 6:
        volume_s = 1
    elif 7 <= volume <= 12:
        volume_s = 2
    elif 13 <= volume <= 19:
        volume_s = 3
    elif 20 <= volume <= 25:
        volume_s = 4
    elif 26 <= volume <= 31:
        volume_s = 5
    elif 32 <= volume <= 37:
        volume_s = 6
    elif 38 <= volume <= 44:
        volume_s = 7
    elif 45 <= volume <= 50:
        volume_s = 8
    elif 51 <= volume <= 56:
        volume_s = 9
    elif 57 <= volume <= 62:
        volume_s = 10
    elif 63 <= volume <= 69:
        volume_s = 11
    elif 70 <= volume <= 75:
        volume_s = 12
    elif 76 <= volume <= 81:
        volume_s = 13
    elif 82 <= volume <= 87:
        volume_s = 14
    elif 88 <= volume <= 100:
        volume_s = 15
    lcd.clear()
    lcd.cursor_pos = (0, 3)
    lcd.write_string("volume ")
    lcd.write_string(str(volume))
    lcd.cursor_pos = (1, 0)
    for i in range(volume_s):
        lcd.write(0b11111111)
        #>>> print(math.ceil(50/6.7)) formula per arrotondare
        #importare import math
    time.sleep(2)
    scrivo_musica()

def get_stato():
    fileObj = open("/var/local/www/currentsong.txt", "r")
    words = fileObj.read().splitlines()
    #print(words)
    if words[0] == "file=Bluetooth Active":
        stato = "bt"
        volume = 50
    else:
        stato = words[13].split("=")[1]
        volume = words[11].split("=")[1]
    fileObj.close()
    return(stato,volume)

def scrivo_musica():
    #print(get_artist())
    #print(get_track())
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(get_artist().title())
    lcd.cursor_pos = (1, 0)
    lcd.write_string(get_track().title())

def print_bt_ico(bt):
    if bt:
        #print("BT")
        lcd.cursor_pos = (1, 14)
        lcd.write_string("bt")
    else:
        #print("NO BT")
        lcd.cursor_pos = (1, 14)
        lcd.write_string("  ")

def get_track():
    fileObj = open("/var/local/www/currentsong.txt", "r")
    words = fileObj.read().splitlines()
    if re.search("http*",words[0]):
        #radio streaming
        #print(words[3])
        if words[3] == "title=Streaming source":
            track = "undefined"
        else:
            track = words[3].split(" - ")[1].strip()
    else:
        #mp3
        track = words[3].split("=")[1]
    fileObj.close()
    #print(track)
    return(track)

def get_artist():
    #time.sleep(1)
    fileObj = open("/var/local/www/currentsong.txt", "r")
    words = fileObj.read().splitlines()
    if re.search("http*",words[0]):
        #radio streaming
        artist = words[3].split("-")[0].split("=")[1]
        #artist = artist[0].strip()
    else:
        #mp3
        artist = words[1].split("=")[1]
    fileObj.close()
    return(artist)

def get_volume():
    fileObj = open("/var/local/www/currentsong.txt", "r")
    words = fileObj.read().splitlines()
    volume = words[11].split("=")[1]
    fileObj.close()
    return(volume)

def main():
#setup
    #fileObj = open("/var/local/www/currentsong.txt", "r")
    previousMillis = 0
    interval = 100
    #prev_stato = get_stato()[0]
    orologio = 1
    prev_stato = "undefinded"
    prev_track = "undefinded"
    prev_volume = "undefined"
    #prev_volume = get_volume()

#loop
    while True:
        time.sleep(2)
        #print("ciclo")
        stato = get_stato()
        curr_stato = stato[0]
        #sprint("curr_stato=" + curr_stato)
        #print("prev_stato=" + prev_stato)
        if curr_stato != prev_stato:
            #print("cambio stato")
            lcd.clear()
            prev_stato = curr_stato
            if curr_stato == "stop":
                orologio = 1
                print_bt_ico(0)
                print_stop()
            elif curr_stato == "pause":
                orologio = 1
                print_bt_ico(0)
                print_stop()
            elif curr_stato == "play":
                orologio = 0
                print_bt_ico(0)
                print_play()
                scrivo_musica()
            elif curr_stato == "bt":
                orologio = 1
                print_bt_ico(1)
            else:
                print("salcazzo")
            #se non sta suonando non serve verificare il cambio traccia
        if orologio == 0:
            curr_trac = get_track()
            if curr_trac != prev_track:
                #print("cambio traccia")
                scrivo_musica()
                prev_track = curr_trac
            #se non sta suonando non serve verificare il volume
            curr_volume = stato[1]
                #print(curr_volume)
            if curr_volume != prev_volume:
                print_volume(curr_volume)
                #print("cambio volume")
                prev_volume = curr_volume

        if orologio == 1:

            print_time()
            #print("mostro ora")
            #time.sleep(2)



if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd.close(clear=True)
    #client.disconnect()
