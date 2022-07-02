import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)    #\r\n signifies an EOL (end of line), so \r\n\r\n signifies nothing between two EOL sequences.

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break            #One of the requirements for using the HTTP protocol is the need to send and receive data as bytes objects, instead of strings
    print(data.decode())  #the encode() and decode() methods convert strings into bytes objects and back again.
mysock.close()
