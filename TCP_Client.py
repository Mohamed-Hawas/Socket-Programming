import socket
import sys

IP = 'localhost'
Port = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((IP,Port))
message = ""
data = clientSocket.recv(2048)
print (data.decode('UTF-8'))
while message != "exit" :
    message = input("Enter your message ")
    clientSocket.send(message.encode('UTF-8'))
    data = clientSocket.recv(2048)
    print ('"%s" has been sent' % data.decode('UTF-8'))

clientSocket.close()
message = input('press enter to exit')



