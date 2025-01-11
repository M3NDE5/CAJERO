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
        "nombre": nombre,
        "cedula": cedula,
        "numero cuenta": numero_cuenta,
        "clave": clave,
        "saldo": saldo
    }
    cuentas[numero_cuenta] = cuenta
    print("\nCUENTA CREADA")
    for llave, valor in cuenta.items():
        print(f"{llave}: {valor}")

def consignar_saldo():
    cuenta_consignar = input("Ingresa el número de cuenta: ")
    if cuenta_consignar in cuentas:
        monto = float(input("Ingresa el monto a consignar: "))
        cuentas[cuenta_consignar]["saldo"] += monto
        print(f"Consignación exitosa. \nNuevo saldo: {cuentas[cuenta_consignar]['saldo']}")
        print("\nCUENTA ACTIALIZADA: ")
        for llave, valor in cuentas[cuenta_consignar].items():
            print(f"{llave} : {valor}")
    else:
        print("La cuenta no existe...")

def cuentas_r():
    contador = 0
    for llave, valor in cuentas.items():
         print(f"Cuenta {contador + 1}")
         print(f"{llave}: {valor}")
         contador += 1


opc = 0
while opc != 4:
    print("\nMENU FACTURACIÓN\n1. Crear cuenta\n2. Consignar dinero\n3. Mostrar cuentas\n4. Salir")
    opc = int(input("\nIngrese una opción: "))
    match opc:
        case 1:
            print("CREAR CUENTA")
            crear_cuentas()
        case 2: 
            print("CONSIGNAR DINERO")
            consignar_saldo()
        case 3:
            print("CUENTAS REGISTRADAS")
            cuentas_r()
