saldo=800
monedaDigital=["BTC", "LTC", "ETH"]

print("\t.:MENU:.")
print("1. Recibir dinero")
print("2. Transferir")
print("3. Balance de moneda")
print("4. Balance general")
print("5. Historial de transferencia")
print("6. Salir del programa")
opcion = int(input("Que desea Hacer (Ingrese una opción valida): "))
print()
if opcion==1:
    print()
    print("Monedas validas para Recibir 'BTC', 'LTC' y 'ETH'")
    monedaDigital=input("Ingrese la moneda Digital a recibir: ")
    cantidad=float(input("Ingrese la cantidad de " +monedaDigital+ " a Recibir: "))
    codigo=float(input("Ingrese Codigo de transacción: "))
    print("Transacción realizada con exito. Moneda recibida: " +monedaDigital+ " Cantidad: ", str(cantidad), "Codigo: ", str(codigo), ". El total en su Wallet es de: ", str(saldo + cantidad))
elif opcion==2:
    print()
    print("Monedas validas para Transferir 'BTC', 'LTC' y 'ETH'")
    monedaDigital=input("ingrese la moneda Digital a Transferir: ")
    cantidad=float(input("Ingrese la cantidad de " +monedaDigital+ " a Transferir: "))
    if cantidad>saldo:
        print("No tiene saldo suficiente")
    elif cantidad<=saldo:
        cantidad = float(input("Ingrese la cantidad de " + monedaDigital + " a Transferir: "))
    else:
        print("Error")
    codigo=float(input("Ingrese Codigo de transacción: "))
    print("Transacción realizada con exito. Moneda Transferida: " +monedaDigital+ " Cantidad Transferida: ", str(cantidad), "Codigo: ", str(codigo), ". El total en su Wallet es de: ", str(saldo - cantidad))




