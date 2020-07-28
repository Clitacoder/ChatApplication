import socket
import sys
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host=input(str("Please enter the hostname of your server: ")
host='192.168.0.120'
port=9999
s.connect((host,port))
print("Connected to the chat server")
while 1:
	incoming_message=s.recv(1024)
	incoming_message=incoming_message.decode()
	print("Server: ", incoming_message)
	print("")
	message=input(str(">>"))
	message=message.encode()
	s.send(message)
	print("Message has been sent")