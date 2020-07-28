from socket import *
import select 
import sys
import _thread
serverName = '192.168.43.103'
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
def print_message(): 
	while 1:
		recieved = clientSocket.recv(1024);
		print ('\t\t', recieved.decode()) 
		if(recieved.decode()=="Meaning of Your Name") :
			message = input("Press Enter for confirmation to close the Connection") 
			message ="Your Connection is Closed"
			clientSocket.send(message.encode())	
			print("Your Connection is Closed")
			clientSocket.close()
			sys.exit()
		if(recieved.decode()=="Your Connection is Closed") :
			clientSocket.close()
			sys.exit()
print ('Connection Succesful') 
_thread.start_new_thread(print_message,())
while 1:
	message = input() 
	clientSocket.send(message.encode())	
clientSocket.close()