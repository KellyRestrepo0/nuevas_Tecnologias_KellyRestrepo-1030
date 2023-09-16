pago = input("¿Desea pagar? (si/no): ")

if pago == "si":
    print("Pagando...")
else :
    otro_pedido = input("¿Desea realizar otro pedido? (si/no): ")
    if otro_pedido == "no":
        print("¡Hasta luego!")