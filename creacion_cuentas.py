import os
import random
from datetime import date, datetime

cuentas = {} 
def fecha():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    return f"Ultima actualizacion el {fecha} // a la(s): {hora_personalizada}"

def crear_cuentas():
    saldo = 0  
    nombre = input("Ingrese su nombre: ")
    cedula = input("Ingrese la cédula: ")
    numero = random.randint(10**11, 10**12 - 1) 
    numero_cuenta = str(numero)
    print(f"Su número de cuenta es: {numero_cuenta}")
    clave = str(input("Ingrese una contraseña de 4 dígitos: "))
    cuenta = {
        "nombre" : nombre,
        "cedula" : cedula,
        "numero cuenta": numero_cuenta,
        "clave": clave,
        "saldo": saldo
    }
    cuentas[numero_cuenta] = cuenta
    with open(f"Registro cuentas/{numero_cuenta}.txt", "w") as archivo:
        archivo.write(fecha())
        for llave in ["nombre", "cedula", "numero cuenta", "saldo"]:
            archivo.write(f"\n{llave}: {cuenta[llave]} ")

    print("\nCUENTA CREADA")
    for llave, valor in cuenta.items():
        print(f"{llave}: {valor}")
    
    return f"{cuenta}"
    




