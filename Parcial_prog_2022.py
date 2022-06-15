#################################################################################################
########PARCIAL INTRODUCCION A LA PROGRAMACION 2022##############################################
#################################################################################################
#Apellido y nombre: Gonzalez Carla Micaela.
#D.N.I: --------
#Legajo: ------
##################################################################################################

#Segundo Parcial 2022 (Tema 1)
#CONSIGNAS
#Consigna 1: Enuncie cuáles son las características de una lista. Explique brevemente.
#Consigna 2:
#Escriba una función en Python que permita procesar el nombre y la cantidad de amigos 
# que posee un conjunto de 200 usuarios de Facebook.
#  Por ejemplo, una entrada válida del programa sería "Juan Manuel Fernández" para el nombre y 2500 para los amigos.
#Una vez procesados todos los usuarios, el programa debe informar:
#d) El promedio de amigos de los usuarios.
#e) Indicar (por sí o por no) si algún usuario se llama "Diego Maradona".
#f) El nombre del usuario con mayor cantidad de amigos.
#Consigna 3:
#Escriba una función que reciba un string como parámetro y retorne un booleano que
#  identifique si existe la letra 'z' en el mismo.
#  Por ejemplo, si la función recibe 'Programación' retornará False.
#Consigna 4:
#Escriba una función en Python que reciba como parámetro una lista y retorne la cantidad de elementos pares e impares. 
# Así, si por ejemplo la función recibe la lista L = [5, 4, 2, 11, 3, 8, 21] deberá retornar 3 y 4 respectivamente.


#Tranquil@y éxitos en el examen!

#CONSIGNA 1:
#Dinamicas: la cantidad de elementos de una lista puede modificarse y puede definirse una lista vacia o puede ser creada 
#a partir de un conjunto de elementos.
#Son heterogeneas: es decir, que los elementos que forman una lista pueden ser diferentes tipos de datos.
#Indexadas: es posible acceder a cada uno de sus elementos.
#Mutables: sus elementos pueden ser modificables.

#CONSIGNA 2:
def facebook():
    contador = -999
    usuarios = 0
    for x in range(200):
        ingreso = input("Ingrese su nombre de usuario:")
        cantidad_usuarios = int(input("Ingrese la cantidad de amigos:"))
        if ingreso == "Diego Maradona":
            dato = "SI"
        else:
            dato = "NO"

        if cantidad_usuarios > contador:
            contador = usuarios
            amigomax = ingreso

        contador += cantidad_usuarios
    cantidad_usuarios = contador / 200
    print(f"El promedio de amigos de los usuarios es de {usuarios}")
    print(f"Existe algun usuario con el nommbre Diego Maradona? {dato}.")
    print(f"El usuario con mas amigos es: {amigomax}.")

facebook()

#CONSIGNA 3:
#Escriba una función que reciba un string como parámetro y retorne un booleano que
#  identifique si existe la letra 'z' en el mismo.
#  Por ejemplo, si la función recibe 'Programación' retornará False.

def booleano(z):
    letra = False
    for x in z:
        if x == "z":
           letra = True
    return letra

print(booleano("programacion"))


#CONSIGNA 4:

def par_impar(l):
    par = 0
    impar = 0
    for x in l:
        if x % 2 == 0:
            par += 1
        else:
            impar += 1
    return(par, impar)

print(par_impar([1, 2, 3, 4, 5, 6, 7, 8]))
