from creacion_cuentas import *
from consignar_dinero import *
from retiro import *
from recibos import *
from movimientos import *



opc = 0
while opc != 6:
    print("\nCAJERO\n1. Crear cuenta\n2. Consignar dinero\n3. Retirar dinero\n4. Pagar recibos\n5. Movimientos\n6. salir")
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
            pagar()
        case 5: 
            print("MOVIMIENTOS")
            movimientos()
        case 6: 
            print("Programa terminado ...")
        case _:
            print("Seleccione una opcion valida..")
