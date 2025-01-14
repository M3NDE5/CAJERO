from creacion_cuentas import*
from creacion_cuentas import fecha
from consignar_dinero import *

def retirar_dinero():
    
    cuenta_retirar = input("Ingresa el número de cuenta: ")

    clave_retirar = str(input("Ingresa la clave: "))


    if clave_retirar in cuentas[cuenta_retirar]["clave"]:

        if cuenta_retirar in cuentas:
            monto = float(input("Ingresa el monto a retirar: "))

            if monto > cuentas[cuenta_retirar]["saldo"]:
                print("Saldo insuficiente, si tiene algún problema contactarse con su banco!")

            elif monto <= cuentas[cuenta_retirar]["saldo"]:
                cuentas[cuenta_retirar]["saldo"] -= monto
                print(f"Consignación exitosa. \nNuevo saldo: {cuentas[cuenta_retirar]['saldo']}")

            with open(f"Registro cuentas/{cuenta_retirar}.json", "w") as archivo:
                json.dump(cuentas[cuenta_retirar], archivo, indent=4) 

            movimientos = [
                [" Movimiento     ", "  cuenta  ", "  valor  ", "  hora  "],
                ["Consignar dinero", f"  {cuenta_retirar}  ", f"  {monto}  ", tiempo()]
            ]
            
            archivo = open(f"Registro cuentas/Movimientos {cuenta_retirar}.csv", "a")
            with archivo:
                    archivo = writer(archivo)
                    archivo.writerows(movimientos)
        else:
            print("La cuenta no existe...")
    else:
        print("Contraseña incorrecta...")
    
    
    
