compra = float(input("Ingrese el valor de compra: "))
cuotas = int(input("Ingrese la cantidad de cuotas: "))

while compra > 0:
    if cuotas > 0:
        pago_cuota = compra / cuotas
        print(f"Se pagará {pago_cuota:.2f} en la cuota {cuotas}")
        compra -= pago_cuota
        cuotas -= 1
    else:
        print("Se han agotado todas las cuotas.")
        break

print("El valor ha sido pagado por completo.")