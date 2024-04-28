#import socket module
from socket import *
import sys # In order to terminate the program
from time import strftime

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 8080
serverSocket.bind(("", serverPort))
serverSocket.listen()
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Date: { strftime('%a, %d-%b-%y %H:%M:%S %z') }\r\n".encode())
        connectionSocket.send("\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send(f"Date: { strftime('%a, %d-%b-%y %H:%M:%S %z') }\r\n".encode())
    finally:
        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
