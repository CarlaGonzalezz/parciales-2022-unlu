##############################Introducción a la Programación (11071)####################
##Parcialito - Sede Luján##
#Apellido y nombre: Gonzalez Carla Micaela
#Legajo: ------

#IMPORTANTE
#● Tienen tiempo de entregar el examen hasta las 12 hs. No se admitirán entregas fuera de horario.
#● Las hojas que acompañen la entrega del examen deberán tener el nombre y apellido del estudiante así como
#su legajo. En caso de no conocer el legajo, pueden escribir el DNI.
#● Las calificaciones serán publicadas en el aula virtual y, ante dudas en la corrección, podrán asistir a las
#clases de consulta presenciales de la semana siguiente a la entrega de calificaciones a revisar el parcial.


#Consigna 1: ¿Cuál es el mínimo y máximo de iteraciones de un programa que procesa los precios
#de 200 libros, si debe verificar que al menos 5 de los libros cuesten más que 500 pesos? Justifique
#de manera breve y concisa.


#Consigna 2: Escriba una función en Python que permita procesar la información sobre n webinars
#(charlas online). La función recibirá como parámetro la cantidad de webinars que deben ser
#procesados (n).
#Por cada webinar, el programa debe solicitar ingresar el título de la actividad y el número de
#inscriptos. Por ejemplo, una entrada válida del programa sería el valor 77 para el número de
#inscriptos e “Introducción a Redes Neuronales” para el título.
#Una vez procesados todos los webinars, el programa debe informar:
#1. El título del webinar con la mayor cantidad de inscriptos.
#2. El promedio de inscriptos entre todos los webinars.


#Consigna 3: Escriba una función en Python que reciba como parámetros dos números naturales n
#y m, donde n < m, (no hace falta validar) y retorne el producto de todos los números entre n y m
#ellos incluidos. Ejemplo, n=2, m=4, resultado=2*3*4=24

#Consigna 1:
#Si el usuario va a buscar entre 200 libros, los que valgan mas de 500 pesos, como minimo deben haber 5 libros de 500 pesos, 
# por lo que como minimo
#va a itinerar cinco veces y como maximo 200, ya que si el ultimo libro se encuentra en el ultimo dato ingresado,
#se deberia cumplir todo el ciclo para terminar el programa.
 
#Consigna 2:
def webinars(n):
    cont = 0
    promedio = 0
    titulo = ""
    max_inscriptos = 0
    for x in range(1, n + 1):
        nombre = input("Ingrese el titulo de webiner:")
        cantidad = int(input("Ingrese la cantidad de inscriptos:"))
        if cantidad > max_inscriptos:
            max_inscriptos = cantidad
            titulo = nombre
        cont += cantidad / n
    promedio = cont
    print(f"El titulo del webinar con la mayor cantidad de inscriptos es de: {titulo}")
    print(f"El promedio de todos los inscriptos entre todos los webinars es de:{promedio}")

webinars(4)

#Consigna 3:
def numeros_naturales(n, m):
    num = 1
    for x in range(n, m + 1):
        num *= x
    return num
print(numeros_naturales(2,4))

numeros_naturales(2,4)
        

