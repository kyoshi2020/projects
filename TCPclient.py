#goal is to open a port and then listen to it. then after go to local host and put port # in to test it. will tell you IP that it gets connected from
#first we are going to import the socket library
import socket

#Next we create a socket object

s = socket.socket()

print("Socket successfully created")

#reserve a port

port = 1979

#bind
s.bind(('', port))
print("Socket is bound to %s" %(port))

#put the socket into listening mode
s.listen(5)
print("Socket is now listening")

# a forever loop until we exit
while True:
	#establish connection with client
	c, addr = s.accept()
	print("Got connection from", addr)
