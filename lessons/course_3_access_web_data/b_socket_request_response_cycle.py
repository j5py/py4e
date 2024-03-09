
import socket


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(('data.pr4e.org', 80))
connection.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode())


# Examine response headers and body

while True:
    data = connection.recv(512) # the maximum amount of data to be received at once (bufsize)
    if len(data) < 1:
        break
    print(data.decode(), end='')


connection.close()
