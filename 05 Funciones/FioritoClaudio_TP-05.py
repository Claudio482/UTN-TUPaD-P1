# Ejercicios Práctico #5 Funciones en Python
# Alumno: Claudio Fiorito
# Tutor: Franco Gonzalez
# Fecha: 17/4/25

# ----------------------------Ejercicio 1-----------------------------------------------------
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.


# # Funcion def imprimir_hola_mundo
# def imprimir_hola_mundo():
#     print ("Hola Mundo!")

# #Programa principal
# imprimir_hola_mundo()


# ----------------------------Ejercicio 2-----------------------------------------------------
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


# # Funcion def saludar_usuario
# def saludar_usuario(nombre):
#   return nombre

# # Programa principal
# usuario = input("El nombre del usuario es: ")
# saludo = saludar_usuario(usuario)
# print("Hola!", saludo)


# ----------------------------Ejercicio 3-----------------------------------------------------
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre][apellido], tengo[edad] años y vivo en[residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.


# Funcion def informacion_personal

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# # Programa principal
# # Solicitamos los datos al usuario
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# resi = input("Ingrese su residencia: ")
# # Llamamos a la funcion con los valores ingresados
# datos_usuario = informacion_personal(nombre, apellido, edad, resi)


# ----------------------------Ejercicio 4-----------------------------------------------------
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

# import math

# # Función que calcula el área de un círculo dado su radio

# def calcular_area_circulo(radio):
#      area = math.pi * (radio**2)
#      return area

# # Función que calcula el perímetro de un círculo dado su radio

# def calcular_perimetro_circulo(radio):
#     perimetro = 2 * math.pi * radio
#     return perimetro

# # Programa principal
# # Solicita el radio al usuario
# a = float(input("Ingrese el radio del criculo: "))

# # Llama las funciones
# area = calcular_area_circulo(a)
# perimetro = calcular_perimetro_circulo(a)

# # Muestra los resultados con 2 decimales
# print (f"El area del circulo es {area:.3f}, y el perimetro  {perimetro:.2f}")


# ----------------------------Ejercicio 5-----------------------------------------------------
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

# # Funciones def segundos_a_horas
# def segundos_a_horas(segundos):
#     convercion = segundos / 3600
#     return convercion

# # Programa principal
# seg = float(input("Ingrese la cantidad de segundos: "))
# horas = segundos_a_horas(seg)

# # Se muestra el resultado convertido con dos decimales
# print(f"{seg} segundos son {horas:.2f} horas")


# ----------------------------Ejercicio 6-----------------------------------------------------
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# # Funcion def tabla_multiplicar

# def tabla_multiplicar(numero):
#     # Recorremos del 1 al 10 para generar la tabla
#     for i in range(1, 11):

#         resultado = numero * i  # Calculamos el resultado de la multiplicación
# # Imprimimos el resultado
#         print(f"{numero} x {i} = {resultado}")

# # Programa principal
# num = int(input("Ingrese un numero: "))
# tabla_multiplicar(num)  # Llamamos a la función


# ----------------------------Ejercicio 7-----------------------------------------------------
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

# # Funcion def operaciones_basicas entre dos numeros
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     div_entera = a // b
#     return suma, resta, multiplicacion, div_entera


# # Programa principal
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# # Se Llama a la función y se obtiene los resultados
# suma, resta, multiplicacion, div_entera = operaciones_basicas(num1, num2)
# # Se muestra los resultados
# print(f"La suma de {num1} + {num2} es ", suma)
# print(f"La resta de {num1} - {num2} es ", resta)
# print(f"La multiplicacion de {num1} * {num2} es ", multiplicacion)
# print(f"La divicion entera de {num1} // {num2} es ", div_entera)

# ----------------------------Ejercicio 8-----------------------------------------------------
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal(IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.


# # Funcion calcular_imc
# def calcular_imc(peso, altura):
#     imc = peso / (altura**2)
#     return imc


# # Programa principal
# # Solicitamos al usuario el peso y la altura, y los convertimos a float
# a = float(input("Ingrese su peso en kg: "))
# b = float(input("Ingrese su altura en metros: "))
# # Llamamos a la función
# imc = calcular_imc(a, b)
# # Mostramos el resultado con dos decimales
# print(f"Su índice de masa corporl (IMC),es: {imc:.2f}")


# ----------------------------Ejercicio 9-----------------------------------------------------
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


# # Funcion convercion
# def celsius_a_fahrenheit(celsius):
#     f = (1.8 * celsius)+32
#     return f


# # Programa principal
# # Solicitamos la temperatrua
# c = float(input("Ingrese su temperatura en °C: "))
# # Llamamos a la funcion
# f = celsius_a_fahrenheit(c)
# # Se muestra el resultado
# print(f" {c:.1f} °C equivale a: {f:.1f} °F.")


# ----------------------------Ejercicio 10-----------------------------------------------------
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


# # Funcion
# def calcular_promedio(a, b, c):
#     promedio = (a + b + c) / 3

#     return promedio


# # Programa principal
# # Solicitamos tres valores al usuario
# num1 = float(input("Ingrese el primer valor: "))
# num2 = float(input("Ingrese el segundo valor: "))
# num3 = float(input("Ingrese el tercer valor: "))
# # Llamamos la función
# resultado = calcular_promedio(num1, num2, num3)
# # Se muestra el resultado con dos decimales
# print(f"El promedio de los numeros ingresados es {resultado:.2f}")
