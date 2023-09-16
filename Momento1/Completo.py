import random
import datetime

# Registro de usuarios
usuarios = []

def registrar_usuario():
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    contraseña = input("Contraseña: ")
    usuarios.append({"nombre": nombre, "email": email, "telefono": telefono, "contraseña": contraseña})
    print("Registro exitoso.")

def iniciar_sesion():
    global usuario_actual
    usuario = input("Email o Teléfono: ")
    contraseña = input("Contraseña: ")
    
    for usuario_info in usuarios:
        if (usuario == usuario_info["email"] or usuario == usuario_info["telefono"]) and contraseña == usuario_info["contraseña"]:
            print(f"Inicio de sesión exitoso. Bienvenido, {usuario_info['nombre']}!")
            usuario_actual = usuario_info
            return True

    print("Credenciales incorrectas.")
    return False

def juego():
    vidas = 5
    puntos = 0

    while vidas > 0:
        num = random.randint(0, 9)
        if num == 0:
            vidas -= 1
            print(f"Vidas: {vidas}")
        else:
            puntos += 1
            print(f"Puntos: {puntos}")

def tarjeta_debito():
    saldo = float(input("Ingrese el valor de compra: "))
    cuotas = int(input("Ingrese la cantidad de cuotas: "))
    frecuencia = input("Seleccione la frecuencia de pago (quincenal/mensual): ").lower()

    if frecuencia not in ["quincenal", "mensual"]:
        print("Frecuencia de pago no válida.")
    else:
        cuota_actual = 1
        cuotas_restantes = cuotas
        historial = []
        fecha_actual = datetime.date.today()

        while saldo > 0 and cuotas_restantes > 0:
            if frecuencia == "quincenal":
                pago_cuota = saldo / (cuotas_restantes * 2)
            else:
                pago_cuota = saldo / cuotas_restantes

            saldo -= pago_cuota
            cuotas_restantes -= 1

            cuota_info = {
                "cuota": cuota_actual,
                "monto": pago_cuota,
                "fecha": fecha_actual.strftime("%d/%m/%Y"),
                "saldo_restante": saldo
                }
            historial.append(cuota_info)

            cuota_actual += 1
            fecha_actual += datetime.timedelta(days=15 if frecuencia == "quincenal" else 30)

        print("El valor ha sido pagado por completo.")

        for pago in historial:
            print(f"Cuota {pago['cuota']} - Monto: {pago['monto']:.2f} - Fecha: {pago['fecha']} - Saldo Restante: {pago['saldo_restante']:.2f}")

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        if iniciar_sesion():
            while True:
                print("\nSubmenú:")
                print("1. Tarjeta de débito")
                print("2. Juego")
                print("3. Volver")
                subopcion = input("Seleccione una opción: ")
                if subopcion == "1":
                    tarjeta_debito()
                elif subopcion == "2":
                    juego()
                elif subopcion == "3":
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")