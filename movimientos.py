from creacion_cuentas import *

def consignar_saldo():
    cuenta_consignar = input("Ingresa el número de cuenta: ")
    if cuenta_consignar in cuentas:
        monto = float(input("Ingresa el monto a consignar: "))
        cuentas[cuenta_consignar]["saldo"] += monto
        print(f"Consignación exitosa. \nNuevo saldo: {cuentas[cuenta_consignar]['saldo']}")
        print("\nCUENTA ACTIALIZADA: ")
        for llave, valor in cuentas[cuenta_consignar].items():
            print(f"{llave} : {valor}")

        with open(f"Registro cuentas/{cuenta_consignar}.txt", "w") as archivo:
            archivo.write(f"cuenta: {cuentas[cuenta_consignar]}")
        
    
    else:
        print("La cuenta no existe...")