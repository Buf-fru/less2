import socket


HOST = ('127.0.0.1', 2234)

# SOCK_DGRAM - UDP,  SOCK_STREAM - TCP, AF_INET - ip v4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect(HOST)
f = input()

l = sock.sendall(f.encode())
#data = sock.recv(1024).decode() # ждем отправки ответа
data = sock.recv(1024)
print(data)