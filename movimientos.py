from consignar_dinero import *
from retiro import *
from recibos import *



def movimientos():
    numero_cuenta = input("Ingrese el numero de cuenta: ")
    if numero_cuenta in cuentas:
        contraseña = input("Ingrese la clave: ")
        if contraseña in cuentas[numero_cuenta]["clave"]:
            archivos_leidos = open(f"Registro cuentas/Movimientos {numero_cuenta}.txt", "r")
            print("TUS MOVIMIENTOS")
            print(archivos_leidos.read())
        else:
            print("Contraseña incorrecta...")
    else:
        print("El numero de cuenta no existe...")
                

            