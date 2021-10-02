#!/bin/python3

import sys
import socket
import os
from datetime import datetime
 
os.system("clear")
print("\033[0;31m _________              __   __________________     _____    _______     ")
print("\033[0;31m \______   \____________/  |_/   _____/\_   ___ \   /  _  \   \      \   ")
print("\033[0;31m  |     ___/  _ \_  __ \   __\_____  \ /    \  \/  /  /_\  \  /   |   \   ")
print("\033[0;31m  |    |  (  <_> )  | \/|  | /        \\     \____/    |    \/    |    \  ")
print("\033[0;31m  |____|   \____/|__|   |__|/_______  / \______  /\____|__  /\____|__  /  ")
print("\033[0;31m                                   \/         \/         \/         \/  ")
print("\033[0;33m                      BY JIMMY X SHADOW                                 ")

t_host = str(raw_input("\033[0;32mEnter the target host :\033[0;33m "))
t_ip = socket.gethostbyname(t_host)

#print the address
print('\033[0;33m_' * 50)
print ("\033[0;31mScanning target :\033[0;32m " + t_host)
print("\033[0;31mScanning started at:\033[0;32m" + str(datetime.now()))
print('\033[0;33m_' * 50)
try:
    for port in range (1,65535):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result=sock.connect_ex((t_ip, port))
	if result ==0:
	   print "\033[0;33mPort {}: \033[0;32mOpen" .format (port)
	   sock.close()

except KeyboardInterrupt:
	print("\033[0;34mPort Scanning complete")
	sys.exit()
