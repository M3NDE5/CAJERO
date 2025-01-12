from creacion_cuentas import *
from consignar_dinero import *
from retiro import *
from recibos import *



opc = 0
while opc != 5:
    print("\nCAJERO\n1. Crear cuenta\n2. Consignar dinero\n3. Retirar dinero\n4. Pagar recibos\n5. Salir")
    opc = int(input("\nIngrese una opción: "))
    match opc:
        case 1:
            print("CREAR CUENTA")
            crear_cuentas()
        case 2: 
            print("CONSIGNAR DINERO")
            consignar_saldo()
        case 3:
            print("RETIRAR DINERO")
            retirar_dinero()
        case 4:
            print("PAGAR RECIBOS") 
            menu()
        case 5: 
            print("Programa terminado...")
        case _:
            print("Seleccione una opcion valida..")
