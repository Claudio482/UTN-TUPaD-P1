# Ejercicios Práctico #11 Recursividad
# Alumno: Claudio Fiorito
# Tutor: Franco Gonzalez
# Fecha: 20/5/25

# ----------------------------Ejercicio 1-----------------------------------------------------
# Crea una función recursiva que calcule el factorial de un número. Luego,
# utiliza esa función para calcular y mostrar en pantalla el factorial de
# de todos los números enteros entre 1 y el número que indique el usuario

# def factorial(n):
#     if n == 0 or n == 1:  # Caso base: el factorial de 0 o 1 es 1
#         return 1
#     else:
#         return n * factorial(n - 1)  # Llamada recursiva: n! = n * (n-1)!


# # Solicita al usuario un número entero positivo
# n = int(input("Ingrese un número entero positivo: "))

# # Mostrar los factoriales del 1 hasta n
# for i in range(1, n + 1):
#     print(f"{i}! = {factorial(i)}")


# ----------------------------Ejercicio 2-----------------------------------------------------
# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# def fibonacci(n):
#     if n <= 0:  # Caso base: si n es menor o igual a 0, devuelve 0
#         return 0
#     elif n == 1:  # Caso base: si n es 1, devuelve 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva: F(n) = F(n-1) + F(n-2)
# # Solicita al usuario un número entero positivo
# n = int(input("Ingrese un número entero positivo: "))
# # Mostrar la serie de Fibonacci hasta la posición n
# print("Serie de Fibonacci:")
# for i in range(n + 1):
#     print(f"Fibonacci({i}) = {fibonacci(i)}")


# ----------------------------Ejercicio 3-----------------------------------------------------
# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

# def potencia(base, exponente):
#     if exponente == 0:  # Caso base cualquier número elevado a la potencia 0 es 1
#         return 1
#     else:
#         return base * potencia(base, exponente - 1)  # Llamada recursiva: n^m = n * n^(m-1)
# # Solicita al usuario la base y el exponente
# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente: "))
# # Calcula la potencia utilizando la función recursiva
# resultado = potencia(base, exponente)
# # Muestra el resultado
# print(f"{base} elevado a la {exponente} es: {resultado}")


# ----------------------------Ejercicio 4-----------------------------------------------------
# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y
# devuelva su representación en binario como una cadena de texto.

# def decimal_a_binario(n):
#     if n == 0:  # Caso base: si n es 0, devuelve una cadena vacía
#         return ""
#     else:
#         # Llamada recursiva: divide n entre 2 y concatena el residuo
#         return decimal_a_binario(n // 2) + str(n % 2)

# # Solicita al usuario un número entero positivo
# n = int(input("Ingrese un número entero positivo: "))
# # Calcula la representación binaria utilizando la función recursiva
# resultado = decimal_a_binario(n)

# # Muestra el resultado
# if resultado == "":
#     resultado = "0"  # Si el número es 0, la representación binaria es "0"
# print(f"La representación binaria de {n} es: {resultado}")


# ----------------------------Ejercicio 5-----------------------------------------------------
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de
# texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar[::-1] ni la función reversed().

# def es_palindromo(palabra):
#     # Caso base: si la longitud de la palabra es 0 o 1, es un palíndromo
#     if len(palabra) <= 1:
#         return True
#     # Compara el primer y último carácter
#     if palabra[0] != palabra[-1]:
#         return False
#     # Llamada recursiva: verifica el resto de la palabra sin los extremos
#     return es_palindromo(palabra[1:-1])

# # Solicita al usuario una palabra
# palabra = input("Ingrese una palabra: ")
# # Verifica si es un palíndromo utilizando la función recursiva
# resultado = es_palindromo(palabra)
# # Muestra el resultado
# if resultado:
#     print(f"La palabra '{palabra}' es un palíndromo.")

# else:
#     print(f"La palabra '{palabra}' no es un palíndromo.")


# ----------------------------Ejercicio 6-----------------------------------------------------
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero
# positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, // ) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# def suma_digitos(n):
#     # Caso base: si n es 0, la suma es 0
#     if n == 0:
#         return 0
#     else:
#         # Toma el último dígito con n % 10
#         # Llama recursivamente con el resto del número (sin el último dígito) usando n // 10
#         return n % 10 + suma_digitos(n // 10)


# # Solicita al usuario un número entero positivo
# n = int(input("Ingrese un numero entero positivo: "))
# # Llama a la función para calcular la suma de los dígitos
# resultado = suma_digitos(n)
# # Muestra el resultado al usuario
# print(f"La suma de los digitos ingresados es: {resultado}.")


# ----------------------------Ejercicio 7-----------------------------------------------------
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
# en el siguiente nivel uno menos(n - 1), y así sucesivamente hasta llegar al último nivel
# con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel
# más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)


# def contar_bloques(n):
#     # Caso base: si no hay bloques en la base, no hay pirámide
#     if n == 0:
#         return 0
#     else:
#         # Suma los bloques del nivel actual (n)
#         # y llama a la función para sumar los del nivel superior (n - 1)
#         return n + contar_bloques(n-1)


# # Solicita al usuario la cantidad de bloques de la base (nivel más bajo)
# n = int(input("Ingrese cant de bloques de la base: "))
# # Llama a la función para calcular el total de bloques
# resultado = contar_bloques(n)
# # Muestra el resultado
# print(f"La suma de los bloques es:{resultado}.")


# ----------------------------Ejercicio 8-----------------------------------------------------
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número
# entero positivo(numero) y un dígito(entre 0 y 9), y devuelva cuántas veces aparece ese dígito
# dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        # Si el último dígito coincide con el buscado, sumamos 1
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


# Solicita los datos al usuario
numero = int(input("Ingrese numero entero positivo: "))
digito = int(input("Ingrese un digito entre 0 y 9: "))

resultado = contar_digito(numero, digito)

print(f"La suma de los bloques es:{resultado}.")
