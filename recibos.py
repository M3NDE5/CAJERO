from creacion_cuentas import *
from retiro import *


def pagar_energia():
    cuenta_retirar = input("Ingresa el número de cuenta: ")
    clave_retirar = str(input("Ingresa la clave: "))
    if clave_retirar in cuentas[cuenta_retirar]["clave"]:
        if cuenta_retirar in cuentas:
            valor_energia = float(input("\nIngrese el valor a pagar: "))
            if valor_energia > cuentas[cuenta_retirar]["saldo"]:
                print("Saldo insuficiente, si tiene algún problema contactarse con su banco!")
            elif valor_energia <= cuentas[cuenta_retirar]["saldo"]:
                cuentas[cuenta_retirar]["saldo"] -= valor_energia
                print(f"Pago realizado con exito!. \nNuevo saldo: {cuentas[cuenta_retirar]['saldo']}")
            with open(f"Registro cuentas/{cuenta_retirar}.txt", "w") as archivo:
                archivo.write(fecha())
                for llave, valor in cuentas[cuenta_retirar].items():
                    if llave != "clave":
                        archivo.write(f"\n{llave}: {valor}")
        else:
            print("La cuenta no existe...")
    else:
        print("Contraseña incorrecta...")

def pagar_gas():
    cuenta_retirar = input("Ingresa el número de cuenta: ")
    clave_retirar = str(input("Ingresa la clave: "))
    if clave_retirar in cuentas[cuenta_retirar]["clave"]:
        if cuenta_retirar in cuentas:
            valor_gas = float(input("\nIngrese el valor a pagar: "))
            if valor_gas > cuentas[cuenta_retirar]["saldo"]:
                print("Saldo insuficiente, no se pudo realizar el pago!")
            elif valor_gas <= cuentas[cuenta_retirar]["saldo"]:
                cuentas[cuenta_retirar]["saldo"] -= valor_gas
                print(f"Pago realizado con exito!. \nNuevo saldo: {cuentas[cuenta_retirar]['saldo']}")
            with open(f"Registro cuentas/{cuenta_retirar}.txt", "w") as archivo:
                archivo.write(fecha())
                for llave, valor in cuentas[cuenta_retirar].items():
                    if llave != "clave":
                        archivo.write(f"\n{llave}: {valor}")
        else:
            print("La cuenta no existe...")
    else:
        print("Contraseña incorrecta...")
    
def pagar_agua():
    cuenta_retirar = input("Ingresa el número de cuenta: ")
    clave_retirar = str(input("Ingresa la clave: "))
    if clave_retirar in cuentas[cuenta_retirar]["clave"]:
        if cuenta_retirar in cuentas:
            valor_agua = float(input("\nIngrese el valor a pagar: "))
            if valor_agua > cuentas[cuenta_retirar]["saldo"]:
                print("Saldo insuficiente, no se pudo realizar el pago")
            elif valor_agua <= cuentas[cuenta_retirar]["saldo"]:
                cuentas[cuenta_retirar]["saldo"] -= valor_agua
                print(f"Pago realizado con exito!. \nNuevo saldo: {cuentas[cuenta_retirar]['saldo']}")
            with open(f"Registro cuentas/{cuenta_retirar}.txt", "w") as archivo:
                archivo.write(fecha())
                for llave, valor in cuentas[cuenta_retirar].items():
                    if llave != "clave":
                        archivo.write(f"\n{llave}: {valor}")
        else:
            print("La cuenta no existe...")
    else:
        print("Contraseña incorrecta...") 

def menu():
    opc = 0
    while opc != 4:
        print("\nMENU RECIBOS\n1. Pagar Energia\n2. Pagar Gas\n3. Pagar Agua\n4. Salir")
        opc = int(input("\nIngrese una opción:\n "))
        match opc:
            case 1:
                print("PAGAR ENERGIA")
                pagar_energia()
            case 2: 
                print("PAGAR GAS")
                pagar_gas()
            case 3:
                print("PAGAR AGUA")
                pagar_agua()
            case 4:
                print("Programa terminado...")
            case _:
                print("Seleccione una opcion valida..")



    