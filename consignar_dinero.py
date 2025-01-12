from creacion_cuentas import *

def consignar_saldo():
    cuenta_consignar = input("Ingresa el número de cuenta: ")
    if cuenta_consignar in cuentas:
        monto = float(input("Ingresa el monto a consignar: "))
        cuentas[cuenta_consignar]["saldo"] += monto
        print(f"Consignación exitosa. \nNuevo saldo: {cuentas[cuenta_consignar]['saldo']}")

        with open(f"Registro cuentas/{cuenta_consignar}.txt", "w") as archivo:
            archivo.write(fecha())
            for llave, valor in cuentas[cuenta_consignar].items():
                if llave != "clave":  # Excluir la clave
                    archivo.write(f"\n{llave}: {valor}")
            
    else:
        print("La cuenta no existe...")

    