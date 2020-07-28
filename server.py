from socket import *
import select 
import sys
import _thread
def clientthread(sender, addr): 
	while 1:
		sentence = sender.recv(2048)
		for reciever in list_of_clients :
			if(reciever!=sender) :
				reciever.send(sentence)
serverPort = 13000
serverName = '106.206.8.21'
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(2)
list_of_clients =[] 
print ('The server is ready to receive') 
while 1:
	connectionSocket, addr = serverSocket.accept() 
	list_of_clients.append(connectionSocket)
	_thread.start_new_thread(clientthread,(connectionSocket,addr))