import socket
import sys 
serverIP = '192.168.43.173'
serverPort = 12001 
serverSocket =  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind((serverIP,serverPort))
print("The server is ready to recieve ... ")
data = ""
while data != "exit" : 
    data, clientAdress = serverSocket.recvfrom(2048)
    message = data.decode('UTF-8')
    print(message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode("UTF-8"),clientAdress)

