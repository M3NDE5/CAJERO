import os
import random

cuentas = {} 
def crear_cuentas():
    saldo = 0  
    nombre = input("Ingrese su nombre: ")
    cedula = input("Ingrese la cédula: ")
    numero = random.randint(10**11, 10**12 - 1) 
    numero_cuenta = str(numero)
    print(f"Su número de cuenta es: {numero_cuenta}")
    clave = input("Ingrese una contraseña de 4 dígitos: ")
    cuenta = {
        "nombre" : nombre,
        "cedula" : cedula,
        "numero cuenta": numero_cuenta,
        "clave": clave,
        "saldo": saldo
    }
    cuentas[numero_cuenta] = cuenta
    # crear carpeta para guardar las cuentas en mi caso se llama "Registro cuentas"
    # y en caso de crear una carpeta diferente debera poner el nombre en las lineas 24 de este modulo
    # y en la linea 13 del modulo "movimientos"
    with open(f"Registro cuentas/{numero_cuenta}.txt", "w") as archivo:
        archivo.write(f"cuenta: {cuenta}")
    print("\nCUENTA CREADA")
    for llave, valor in cuenta.items():
        print(f"{llave}: {valor}")