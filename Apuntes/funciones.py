## Esto es definir la funcion

def saludar ():
    print("Hola")

##Luego hacemos el llamado a la funcion
saludar()

##Funcion que recibe parametros
def saludar2(name):
    print("Hola{name}")

##Hacemos el llamado a la funcion
saludar2("Maria")

##Cuando no conocemos el numeor de argumentos que requiere la funcion
def imprimir_lista(*args):
    print(f"Bienvenidos{args}")

imprimir_lista("Pepito","Luis","Mar")

##funciones con retorno
def sumar(num1,num2):
    return num1 + num2

resultado_suma=sumar(10,5)
print(resultado_suma)


usuario=["1","Pepito","Perez","Pepito@gmail.com","xyz123"]

def imprimirListas(lista):
    for i in range(len(lista)):
        print(lista[i])

print(usuario)