from creacion_cuentas import *
from retiro import *
from consignar_dinero import *


def pagar(tipo):
    cuenta_retirar = input("Ingresa el número de cuenta: ")
    clave_retirar = str(input("Ingresa la clave: "))
    if clave_retirar in cuentas[cuenta_retirar]["clave"]:
        if cuenta_retirar in cuentas:
            valor = float(input("\nIngrese el valor a pagar: "))
            if valor > cuentas[cuenta_retirar]["saldo"]:
                print("Saldo insuficiente, si tiene algún problema contactarse con su banco!")
            elif valor <= cuentas[cuenta_retirar]["saldo"]:
                cuentas[cuenta_retirar]["saldo"] -= valor
                print(f"Pago realizado con exito!. \nNuevo saldo: {cuentas[cuenta_retirar]['saldo']}")
            with open(f"Registro cuentas/{cuenta_retirar}.txt", "w") as archivo:
                archivo.write(fecha())
                for llave, valor in cuentas[cuenta_retirar].items():
                    if llave != "clave":
                        archivo.write(f"\n{llave}: {valor}")       
                with open(f"Registro cuentas/Movimientos {cuenta_retirar}.txt", "a") as archivo:
                    archivo.write(f"\nMOVIMIENTOS CUENTA : {cuenta_retirar}")
                    archivo.write(f"\nMovimiento Realizado...\n{tiempo()}")
                    if tipo == "gas":
                        archivo.write(f"\nRecibo del GAS pagado con exito\n")
                    elif tipo == "agua":             
                        archivo.write(f"\nRecibo del AGUA pagado con exito\n")
                    elif tipo == "energia":
                        archivo.write(f"\nRecibo de la ENERGIA pagado con exito\n")
        else:
            print("La cuenta no existe...")
    else:
        print("Contraseña incorrecta...")

def menu():
    opc = 0
    while opc != 4:
        print("\nMENU RECIBOS\n1. Pagar Energia\n2. Pagar Gas\n3. Pagar Agua\n4. Salir")
        opc = int(input("\nIngrese una opción: "))
        match opc:
            case 1:
                print("PAGAR ENERGIA")
                pagar("energia")
            case 2: 
                print("PAGAR GAS")
                pagar("gas")
            case 3:
                print("PAGAR AGUA")
                pagar("agua")
            case 4:
                print("Programa terminado...")
            case _:
                print("Seleccione una opcion valida..")