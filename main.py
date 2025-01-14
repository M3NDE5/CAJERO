from creacion_cuentas import *
from consignar_dinero import *
from retiro import *
from recibos import *
from movimientos import *
import time



opc = 0
while opc != 6:
    try:
        print("\nCAJERO\n1. Crear cuenta\n2. Consignar dinero\n3. Retirar dinero\n4. Pagar recibos\n5. Movimientos\n6. salir")
        opc = int(input("\nIngrese una opción: \n"))
        #time.sleep(2)
        print("\nCargando...\n")
        match opc:
            case 1:
                try:
                    print("CREAR CUENTA")
                    crear_cuentas()
                except Exception as e:
                    print(f"Error al crear cuenta...{e}")
            case 2:
                try:
                    print("CONSIGNAR DINERO")
                    consignar_saldo()
                except Exception as e:
                    print(f"Error al consignar...{e}")
            case 3:
                try:
                    print("RETIRAR DINERO")
                    retirar_dinero()
                except Exception as e:
                    print(f"Error al retirar...{e}")
            case 4:
                try:
                    print("PAGAR RECIBOS") 
                    menu()
                except Exception as e:
                    print(f"Error al pagar resivos...{e}")
            case 5: 
                print("MOVIMIENTOS")
                movimientos()
            case 6: 
                print("Programa terminado ...")
            case _:
                print("Seleccione una opcion valida..")
    except ValueError:
        print("\ningrese un numero valido...")

