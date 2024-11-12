import socket
import sys

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = ""
while message != "EXIT"  :
    message = input("Enter your message ")
    clientSocket.sendto(message.encode('UTF-8'),(serverName,serverPort))
    data , clientAdress = clientSocket.recvfrom(2048)
    print (data.decode('UTF-8'))

clientSocket.close()
message = input('press enter to exit')
                                                        

