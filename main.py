from creacion_cuentas import *
from movimientos import *



opc = 0
while opc != 4:
    print("\nMENU FACTURACIÓN\n1. Crear cuenta\n2. Consignar dinero\n3. Salir")
    opc = int(input("\nIngrese una opción: "))
    match opc:
        case 1:
            print("CREAR CUENTA")
            crear_cuentas()
        case 2: 
            print("CONSIGNAR DINERO")
            consignar_saldo()
        case 3:
            print("Programa terminado...")
