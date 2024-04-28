#!/usr/bin/env python
from socket import *
from sys import argv
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)

start = {}
for seq in range(10):
    t1 = start[seq] = time.time()
    clientSocket.sendto(f"Ping {seq} { t1 }".encode(),(serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        msg = modifiedMessage.decode()
        t2 = time.time()
        who = int(msg.split(" ")[1])
        if who == seq:
            print(f"{ msg }\tRTT\t { t2 - t1 }")
    except timeout:
        print("Request timed out")

clientSocket.close()