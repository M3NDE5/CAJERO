from creacion_cuentas import *
from csv import reader, writer, DictReader, DictWriter
import json

def tiempo():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    return f"{fecha} // {hora_personalizada}"

def consignar_saldo():
    
    cuenta_consignar = input("Ingresa el número de cuenta: ")

    if cuenta_consignar in cuentas:
        monto = float(input("Ingresa el monto a consignar: "))
        cuentas[cuenta_consignar]["saldo"] += monto
        print(f"Consignación exitosa. \nNuevo saldo: {cuentas[cuenta_consignar]['saldo']}")

        with open(f"Registro cuentas/{cuenta_consignar}.json", "w") as archivo:
            json.dump(cuentas[cuenta_consignar], archivo, indent=4)  
        
            movimientos = [
                [" Movimiento     ", "  cuenta  ", "  valor  ", "  hora  "],
                ["Consignar dinero", f"  {cuenta_consignar}  ", f"  {monto}  ", tiempo()]
            ]
            
            archivo = open(f"Registro cuentas/Movimientos {cuenta_consignar}.csv", "a")
            with archivo:
                    archivo = writer(archivo)
                    archivo.writerows(movimientos)
            
    else:
        print("La cuenta no existe...")