# Ejercicios Práctico #4 Estructuras Repetitivas
# Alumno: Claudio Fiorito
# Tutor: Franco Gonzalez
# Fecha: 12/4/25

# ----------------------------Ejercicio 1-----------------------------------------------------
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# #1.1 Usando inicio
# for i in range (101):
#     print(i)
# #1.2 Usando inicio y fin
# for i in range(0, 101):
#     print(i)

# ----------------------------Ejercicio 2-----------------------------------------------------
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# 2.1 Usando len()
# num1 = int(input("Ingrese un número entero: "))
# longitud = len(str(num1))
# print("La cantidad de dígitos es:", longitud)

# #2.2 Usando while
# num1 = int(input("Ingrese un número entero: "))
# contador = 0 #Contador inicializado en 0

# if num1 > 0: #Verifica si el número es positivo
#     # Si el número es positivo, se procede a contar los dígitos
#     # Se utiliza un bucle while para contar los dígitos del número

# # El bucle se ejecuta mientras num1 sea mayor que 0
#     while num1 > 0:
#         num1 //= 10 #Dividir el número por 10 para eliminar el último dígito
#         contador += 1 #Aumentar el contador en 1 por cada dígito eliminado
# # Al finalizar el bucle, se imprime la cantidad de dígitos
#     print("La cantidad de dígitos es:", contador)

# else:
#     print("El número ingresado no es positivo.")

# ----------------------------Ejercicio 3-----------------------------------------------------
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# suma = 0  # Incializamos suma en cero

# mayor = max(num1, num2)  # Obtenemos el mayor de los numeros
# menor = min(num2, num1)  # Otenemos el menor de los numeros
# # Utilizamos bucle for iniciando en num1 y terminando
# # en num2-1 (-1 para que no sume el ultimo valor asigando por el usuario)
# for x in range(menor, mayor-1):
#     x += 1  # Aumeta contador en uno
#     print(x)
# # Sumamos los valores de cada iteracion y se deposita en suma
#     suma = suma + x
# # Imprimimos por pantalla el resultado
# print("La suma de los valores comprendidos entre",
#       menor, "y", mayor, "es:", suma)


# ----------------------------Ejercicio 4-----------------------------------------------------
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el
# usuario ingrese un 0.


# # Iniciamos suma en 0
# suma = 0
# # Solicitamos un numero al usuario e indicamos que utiliza 0 para detener
# numero = int(input("Ingrese un numero (0 para detener): "))
# # Mientras el número ingresado no sea 0 se sigue pidiendo números y se acumulan en la suma
# while numero != 0:
#     suma += numero
# # Se pide un nuevo número para continuar o detener el ciclo
#     numero = int(input("Ingrese otro numero (0 para detener): "))
# # Se muestra el resultado total de la suma
# print("La suman de los numero ingresados es:", suma)


# ----------------------------Ejercicio 5-----------------------------------------------------
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# # Se genera un número aleatorio entre 0 y 9
# numero = random.randint(0, 9)
# intento = 0
# # Solicitamos el primer intento
# print("Adivina un número entre el 0 y el 9")

# num_ingresado = int(input("Ingresa tu intento: "))
# intento += 1

# # Mientras el intento del usuario no sea igual al número aleatorio seguimos pidiendo nuevos intentos
# while numero != num_ingresado:

#     num_ingresado = int(input("Ingresa un nuevo intento "))

#     intento += 1

# print("Adivinaste el numero en ", intento, " intentos ")


# ----------------------------Ejercicio 6-----------------------------------------------------
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# num1 = 100
# num2 = 0
# print ("Incio")

# for x in range (num1,num2,-2):

#     print ("Numero par ",x)

# print ("Fin numero pares decrecientes")


# ----------------------------Ejercicio 7-----------------------------------------------------
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


# # Se inicializan variables y se le pide al usuario ingresar un número
# num1 = 0
# num2 = int(input("Ingrese un numero entero positivo: "))
# total = 0
# # Se itera sobre cada número en el rango desde num1 hasta num2
# for suma in range(num1, num2):
#     # Se incrementa la variable "suma" en 1 para ajustar el rango y sumar desde 1 hasta num2
#     suma += 1
# # Se agrega el valor actual de "suma" al acumulador total
#     total = suma + total
# # Se muestra el resultado final de la suma
# print("La suma total de los valores comprendido de 0 a", num2, "es:", total)

# ----------------------------Ejercicio 8-----------------------------------------------------
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# # Inicialización de contadores
# pares = 0
# impares = 0
# positivo = 0
# negativo = 0

# # Se solicita al usuario la cantidad de números que se van a analizar.
# num_analizar = int(input("Ingrese cantidad de número a analizar: "))

# # Se itera "num_analizar" las veces para analizar cada número ingresado.
# for contador in range(num_analizar):
#     # Se solicita al usuario un número.
#     num1 = int(input("Ingrese un número: "))
# # Se comprueba si el número es par verificando el resto de la división entre 2.
#     if num1 % 2 == 0:
#         pares += 1  # Si es par, se incrementa el contador de pares.
#     else:
#         impares += 1  # Si no es par, se incrementa el contador de impares.

#  # Se comprueba si el número es positivo.
#     if num1 > 0:
#         positivo += 1  # Si es positivo, se incrementa el contador de positivo
#     elif num1 < 0:
#         negativo += 1  # Si es negativo, se incrementa el contador de negativo

# # Se muestran los resultados finales de los contadores.
# print("Cantidad de número pares", pares)
# print("Cantidad de número impares", impares)
# print("Cantidad de número positivos", positivo)
# print("Cantidad de número negativos", negativo)


# ----------------------------Ejercicio 9-----------------------------------------------------
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# # Incicializamos variables
# media = 0
# suma = 0
# # Se solicita al usuario la cantidad de números que se van a analizar.
# num_analizar = int(input("Ingrese cantidad de número a analizar: "))

# # Se itera "num_analizar" las veces para analizar cada número ingresado.
# for contador in range(num_analizar):
#     # Se solicita al usuario un número.
#     num1 = int(input("Ingrese un número: "))
#     suma = num1 + suma

# # Operamos y luego imprimimos
# # media = suma / num_analizar
# # print("La media de los valores ingresados es: ", media)

# # Imrpimimos con f-strings
# print(f"La media de los valores ingresados es: {suma / num_analizar}")


# ----------------------------Ejercicio 10-----------------------------------------------------
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# # Inicializamos la variable
# invertido = 0
# num_ingresado = int(input("Ingrese un numero entero: "))

# while num_ingresado > 0:
#     # Obtenemos el último dígito del número
#     valor = num_ingresado % 10
#     # Acumulamos el dígito en la variable "invertido"
#     invertido = invertido * 10 + valor
#     # Eliminamos el último dígito del número
#     num_ingresado = num_ingresado // 10
# # Imprimimos el número invertido
# print("El numero invertido es:", invertido)
