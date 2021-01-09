import socket

s = socket.socket()

host = input(str("Please enter the host address of the sender : "))

port = 8080

s.connect((host,port))

print("Connected ...")

filename = input(str( "Please enter the file name of the incoming file :"))

file = open(filename, 'wb')

file_data = s.recv(1024)
file.write(file_data)
file.close()

print (" Horreeeeeey ! File has been received succesfully. ")