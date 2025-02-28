import socket

interfaz = '::'
puerto = 50001
interfaz_servidor = (interfaz, puerto)
socket_servidor = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
socket_servidor.bind(interfaz_servidor)
socket_servidor.listen(10)

try:
    while True:
        coneccion, dir_cliente = socket_servidor.accept()
        string = coneccion.recv(1024).decode('utf-8')
    
        if string:
            print(string)
        else:
            break

    socket_servidor.close()
except:
    print('ERROR EN ALGUN SITIO')
