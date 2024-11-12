import socket
import sys 
serverIP = '192.168.24.173'
serverPort = 12001 
serverSocket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverAddress = serverSocket.bind((serverIP,serverPort))  
print("The server address is %s " % serverAddress )
serverSocket.listen(1)
data = ""
print("Waiting for connection ...")
connection , clientAddress = serverSocket.accept()
print("client connected : ",clientAddress)
data = "welcome to the server"
connection.sendall(data.encode('utf-8'))

while data != "exit"  :   
    data =connection.recv(2048)
    if not data :
        break
    print('received "%s" ' % data.decode('utf-8'))
    connection.sendall(data.upper())
   
connection.close()
