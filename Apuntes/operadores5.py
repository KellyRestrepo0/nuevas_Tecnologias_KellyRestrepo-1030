# Registro de usuarios
usuarios = []

# Registro de un nuevo usuario
def registrar_usuario():
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    contraseña = input("Contraseña: ")
    usuarios.append({"nombre": nombre, "email": email, "telefono": telefono, "contraseña": contraseña})
    print("Registro exitoso.")

# Inicio de sesión
def iniciar_sesion():
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
        print("Opción inválida. Por favor, seleccione una opción válida.")
