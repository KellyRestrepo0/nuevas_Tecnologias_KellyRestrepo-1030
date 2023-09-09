pago= int(input("Indique el valor a pagar: "))

pagar = int(input("Desea pagar y=1 n=0: "))
y=1
n=0
if pagar !=0:
    print ("El valor a pagar es: " , str(pago))
    servicio = int(input("Desea agregar el servicio? (y=1/n=0)"))
    pago = pago+(pago* 1.1)
    if servicio == y:
        print("El valor a pagra es de: "+ str(pago))
    print("Gracias por su visita")
else: 
    print("Indique el producto a pedir")