import socket
import sys
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostname()
print("Server will start on host-",host)
port=9999
s.bind((host,port))
print("")
print(" Binding has been done successfully")
print("")
s.listen(1024)
conn,addr=s.accept()
print( addr, " has connected to the server succesfully and is now available online to chat")
print("")
while 1:
	message=input(str(">>"))
	message= message.encode()
	conn.send(message)
	print("Message has been sent")
	print("")
	incoming_message=conn.recv(1024)
	incoming_message=incoming_message.decode()
	print("Client: ", incoming_message)
	print("")
