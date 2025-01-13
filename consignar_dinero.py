from creacion_cuentas import *
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

        with open(f"Registro cuentas/{cuenta_consignar}.txt", "w") as archivo:
            archivo.write(fecha())
            for llave, valor in cuentas[cuenta_consignar].items():
                if llave != "clave": 
                    archivo.write(f"\n{llave}: {valor}")
        
        with open(f"Registro cuentas/Movimientos {cuenta_consignar}.txt", "a") as archivo:
            archivo.write(f"\nMOVIMIENTOS CUENTA : {cuenta_consignar}")
            archivo.write(f"\nMovimiento Realizado...\n{tiempo()}")
            archivo.write(f"\nDinero consignado: {monto}\n")
            
            
    else:
        print("La cuenta no existe...")