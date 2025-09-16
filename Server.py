import socket


users= {}
HOST = ('127.0.0.1', 2234)
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST)
sock.listen()
print("-----start-----")
while 1:
    conn, addr= sock.accept()
    print(conn, addr)
    data = conn.recv(1024).decode( )
    if "command:reg" in data:
        gygy= data.split("; ")
        u=[]
        g= list('124567890')
        for i in range(1, 3):
            e=gygy[i].split(":")
            u.append(e[1])
        if any(c.isdigit() for c in u[1]) and len(u[1])>5:
            conn.sendall("{дата время} - пользователь {login} зарегистрирован".encode())
        else:
            conn.sendall("{дата время} - ошибка регистрации {login} - неверный пароль/логин".encode())
        print(u)
    elif "command:signin" in data:
        gygy= data.split("; ")
        u=[]
        for i in range(1, 3):
            e=gygy[i].split(":")
            u.append(e[1])
        if u[1] in users:
            conn.sendall("{дата время} - пользователь {login} произведен вход".encode())
        else:
            conn.sendall("{дата время} - ошибка входа {login} - неверный пароль/логин".encode())
        print(u)
    else:
        conn.send("пришли неизвестные  данные - <присланные данные>".encode())
    print(data)

print('-----stop-----')

sock.close()
