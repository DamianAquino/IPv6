import sys
import funciones as f

if __name__ == '__main__':
    if(f.definir_sistema_operativo() == 1):
        f.linux()
    if(f.definir_sistema_operativo() == 2):
        f.windows()
    if(f.definir_sistema_operativo() == 0):
        sys.exit()
