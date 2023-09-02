""" est = 1.51
edad = 18

if est >= 1.50 and edad >= 17:
    print ("Puede ingrear al sube y baja")

if est >= 1.50 or edad >= 13:
    print ("Puede ingrear ") """

#si es estudiante que permite el ingreo si mo 

""" persona = "Estudiante"

if persona == "Estudiante":
    print ("Bienvenido")
else :
    print ("No puede ingresar") """
#tercer ejercicio

""" payment=int(input("Indique el valor a pagar"))
goToPaid = int (input("Desea agregar el servicio? (y=1/n=0)"))
y=1
n=0

if goToPaid != 0:
    print("El valor a pagar es: ",str(payment))
    payService=int(input("desea agregar el servicio (y=1/n=0)"))
    payment=payment(payment*0.1)
    if payService == y:
        print("El valor a pagar es de: "+str(payment))
    print("Gracias por su visita")
else:
    print("Indique el producto a pedir") """

#hacer login y validar tel o telefono y contraseña y validar captcha

# Registro de usuarios
usuarios = []

# Registro de un nuevo usuario
""" def registrar_usuario():
nombre = input("Nombre: ") 
email = input("Email: ")
telefono = input("Teléfono: ")
contraseña = input("Contraseña: ")
usuarios.append({"nombre": nombre, "email": email, "telefono": telefono, "contraseña": contraseña})
print("Registro exitoso.") """

# Inicio de sesión
""" def iniciar_sesion():
usuario = input("Email o Teléfono: ")
contraseña = input("Contraseña: ")
captcha_correcto = 5 * 2 + (3 ** 2)
captcha = input(f"Por favor, resuelve el captcha (5*2+(3**2)): ")
try:
    captcha_ingresado = int(eval(captcha))
    except:
        print("Captcha incorrecto. Intenta de nuevo.")
        return
    
    if captcha_ingresado != captcha_correcto:
        print("Captcha incorrecto. Intenta de nuevo.")
        return
    
    for usuario_info in usuarios:
        if (usuario == usuario_info["email"] or usuario == usuario_info["telefono"]) and contraseña == usuario_info["contraseña"]:
            print(f"Bienvenido, {usuario_info['nombre']}!")
            return
    print("Credenciales incorrectas.")

# Menú principal
while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida." """
                