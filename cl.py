import socket


HOST = ('127.0.0.1', 2234)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect(HOST)
f = input()

l = sock.sendall(f.encode())

data = sock.recv(1024)

print(data)
