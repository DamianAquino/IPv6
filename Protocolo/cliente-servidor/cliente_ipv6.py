import socket

def opciones():
    pass

servidor = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
ip = str(input('IP:'))
print('             ')
puerto = int(input('Puerto: '))

solicitud = opciones()

dir_servidor = (ip, puerto)
servidor.connect(dir_servidor)

print(f'Enviando: {solicitud}')
servidor.sendall(solicitud.encode())

data = servidor.recv(1024)
print(f'Recibido: {data.decode()}')

servidor.close()
