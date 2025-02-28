import os

def definir_sistema_operativo():
    if os.name == 'nt':
        return 2
    elif os.name == 'posix':
        return 1
    else:
        operativo_sistema = os.name
        return 0

def linux():
    configuracion_linux()
    backup()

def windows():
    configuracion_windows()
    backup()

def configuracion_windows():
    pass

def configuracion_linux():
    pass

def backup():
    pass