# Ejercicios de Estructuras Condicionales
# Alumno: Claudio Fiorito
# Tutor: Franco Gonzalez
# Fecha: 5/4/25

# ----------------------------Ejercicio 1-----------------------------------------------------

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad: "))
# if edad > 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

# ------------------------- Ejercicio 2--------------------------------------------------------------------

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá
# mostrar el mensaje “Desaprobado”.

# nota = float(input("Ingrese su nota: "))
# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# --------------------------Ejercicio 3-------------------------------------------------------------------

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa
# un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar
# si un número es par o impar.

# par=int(input("Ingrese un número par: "))
# if par % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

# -------------------------Ejercicio 4--------------------------------------------------------------------

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál
# de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad: "))
# if edad >0 and edad < 12:
#     print("Niño/a")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# elif edad >= 30:
#     print("Adulto/a")
# else:
#     print("Edad no válida")

# ----------------------------Ejercicio 5-----------------------------------------------------------------

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string.


# contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
# #Se utiliza len() para verificar la longitud de la contraseña
# if len(contrasena) >= 8 and len(contrasena) <= 14: # Verificamos la longitud de la contraseña
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ----------------------------Ejercicio 6-----------------------------------------------------------------

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
# Imprimir el resultado por pantalla.

# # Importamos la librería statistics para calcular la moda, mediana y media
# from statistics import mode, median, mean
# import random  # Importamos la librería random para generar números aleatorios
# # Generamos una lista de 50 números aleatorios entre 1 y 100
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# mediana_numeros = median(numeros_aleatorios) # Calculamos la mediana de la lista
# media_numeros = mean(numeros_aleatorios)  # Calculamos la media de la lista
# moda_numeros = mode(numeros_aleatorios)  # Calculamos la moda de la lista
# print("Mediana:", mediana_numeros)  # Imprimimos la mediana
# print("Media:", media_numeros)  # Imprimimos la media
# print("Moda:", moda_numeros)  # Imprimimos la moda

# # Imprimimos la lista de números aleatorios
# print("Lista de números aleatorios:", numeros_aleatorios)

# # Comparamos la media y la mediana para determinar el sesgo
# if media_numeros > mediana_numeros:
#     print("Sesgo positivo") # Si la media es mayor que la mediana, hay sesgo positivo
# elif media_numeros < mediana_numeros:
#     print("Sesgo negativo") # Si la media es menor que la mediana, hay sesgo negativo
# else:
#     print("No hay sesgo") # Si la media es igual a la mediana, no hay sesgo

# ----------------------------Ejercicio 7-----------------------------------------------------------------

# 7) Escribir un programa que solicite una frase o palabra al usuario.
# Si el string ingresado termina con vocal, añadir un signo de exclamación
# al final e imprimir el string resultante por pantalla; en caso contrario,
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# frase = input("Ingrese una frase o palabra: ")
# #-1 para acceder a la última letra de la cadena, utilizamos lower() para convertirla a minúscula
# if frase[-1].lower() in "aeiou": # Verificamos si la última letra es una vocal
#     # Si es una vocal, le agregamos un signo de exclamación al final
#     print(frase + "!")
# else:
#     print(frase)

# ----------------------------Ejercicio 8-----------------------------------------------------------------

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.


# nombre = input("Ingrese su nombre: ")
# print("Seleccione una opción:")
# print("1. Mayúsculas")
# print("2. Minúsculas")
# print("3. Primera letra mayúscula")
# opcion = int(input("Ingrese el número de la opción deseada: "))
# if opcion == 1:
#     print(nombre.upper())  # Convertimos el nombre a mayúsculas
# elif opcion == 2:
#     print(nombre.lower())  # Convertimos el nombre a minúsculas
# elif opcion == 3:
#     print(nombre.capitalize())  # Convertimos la primera letra a mayúscula
# else:
#     print("Opción no válida")  # Mensaje de error si la opción no es válida

# --------------------------Ejercicio 9-------------------------------------------------------------------

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


# magnitud = float(input("Ingrese la magnitud del terremoto: "))
# if magnitud > 0 and magnitud < 3:
#     print("Muy leve (imperceptible)")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve (ligeramente perceptible)")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy Fuerte (puede causar daños significativos)")
# elif magnitud >= 7:
#     print("Extremo (puede causar graves daños a gran escala)")
# else:
#     print("Magnitud no válida")

# -------------------------Ejercicio 10--------------------------------------------------------------------

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
# qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir
# por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.


# Convertimos la entrada a mayúsculas para evitar errores
hemisferio = input("Ingrese la estación del año (N/S): ").upper()
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

if hemisferio == "N":  # Verificamos si el hemisferio es Norte
    # Verificamos si el mes y el día son válidos
    if mes == 12 and dia >= 21 and dia <= 31 or mes == 1 and dia >= 1 and dia <= 31 or mes == 2 and dia >= 1 and dia <= 29 or mes == 3 and dia <= 20:
        print("Invierno")
    elif mes == 3 and dia >= 21 and dia <= 31 or mes == 4 and dia >= 1 and dia <= 30 or mes == 5 and dia >= 1 and dia <= 31 or mes == 6 and dia <= 20:
        print("Primavera")
    elif mes == 6 and dia >= 21 and dia <= 31 or mes == 7 and dia >= 1 and dia <= 31 or mes == 8 and dia >= 1 and dia <= 31 or mes == 9 and dia <= 20:
        print("Verano")
    elif mes == 9 and dia >= 21 and dia <= 31 or mes == 10 and dia >= 1 and dia <= 31 or mes == 11 and dia >= 1 and dia <= 30 or mes == 12 and dia <= 20:
        print("Otoño")
    else:
        print("Fecha no válida")

if hemisferio == "S":  # Verificamos si el hemisferio es Sur
    # Verificamos si el mes y el día son válidos
    if mes == 12 and dia >= 21 and dia <= 31 or mes == 1 and dia >= 1 and dia <= 31 or mes == 2 and dia >= 1 and dia <= 29 or mes == 3 and dia <= 20:
        print("Verano")
    elif mes == 3 and dia >= 21 and dia <= 31 or mes == 4 and dia >= 1 and dia <= 30 or mes == 5 and dia >= 1 and dia <= 31 or mes == 6 and dia <= 20:
        print("Otoño")
    elif mes == 6 and dia >= 21 and dia <= 31 or mes == 7 and dia >= 1 and dia <= 31 or mes == 8 and dia >= 1 and dia <= 31 or mes == 9 and dia <= 20:
        print("Invierno")
    elif mes == 9 and dia >= 21 and dia <= 31 or mes == 10 and dia >= 1 and dia <= 31 or mes == 11 and dia >= 1 and dia <= 30 or mes == 12 and dia <= 20:
        print("Primavera")
    else:
        print("Fecha no válida")

if hemisferio != "N" and hemisferio != "S":  # Verificamos si el hemisferio es válido
    # Si el hemisferio no es N o S, imprimimos un mensaje de error
    print("Hemisferio no válida")
