# Ejercicios Práctico #6 Datos Complejos
# Alumno: Claudio Fiorito
# Tutor: Franco Gonzalez
# Fecha: 11/6/25

# ----------------------------Ejercicio 1-----------------------------------------------------
# Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
#  ● Naranja= 1200
#  ● Manzana= 1500
#  ● Pera = 2300

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# # Añadiendo frutas al diccionario
# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300
# # Imprimiendo el diccionario actualizado
# print("Diccionario actualizado de precios de frutas:")
# for fruta, precio in precios_frutas.items():
#     print(f"{fruta}: {precio} pesos")


# ----------------------------Ejercicio 2-----------------------------------------------------
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
# en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
# Actualizando los precios de las frutas en el diccionario
# precios_frutas['Banana'] = 1330 # Actualizando el precio de Banana
# precios_frutas['Manzana'] = 1700 # Actualizando el precio de Manzana
# precios_frutas['Melón'] = 2800 # Actualizando el precio de Melón
# # Imprimiendo el diccionario actualizado con los nuevos precios
# print("\nDiccionario actualizado de precios de frutas con nuevos precios:")
# for fruta, precio in precios_frutas.items():
#     print(f"{fruta}: {precio} pesos")


# ----------------------------Ejercicio 3-----------------------------------------------------
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# frutas_lista = list(precios_frutas.keys())  # Obteniendo las claves (frutas) del diccionario
# print("\nLista de frutas sin precios:")
# for fruta in frutas_lista:
#     print(fruta)  # Imprimiendo cada fruta de la lista


# ----------------------------Ejercicio 4-----------------------------------------------------
# Un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# # Definimos un diccionario para almacenar los contactos
# contactos = {}
# # Bucle para permitir al usuario cargar 5 contactos
# for i in range(5):
#     # Solicita el nombre del contacto
#     nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
#     # Solicita el número de teléfono
#     numero = input(f"Ingrese el número de teléfono de {nombre}: ")
#     contactos[nombre] = numero  # Almacena el contacto en el diccionario
# # Imprime el diccionario de contactos
# print("\nContactos almacenados:")
# for nombre, numero in contactos.items():
#     print(f"{nombre}: {numero}")  # Imprime cada contacto con su número
# # Solicita al usuario un nombre para buscar el número asociado
# nombre_buscar = input("\nIngrese el nombre del contacto que desea buscar: ")
# # Verifica si el nombre existe en el diccionario y muestra el número asociado
# if nombre_buscar in contactos:
#     # Muestra el número asociado
#     print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
# else:
#     print(f"No se encontró el contacto con el nombre: {nombre_buscar}")


# ----------------------------Ejercicio 5-----------------------------------------------------
# Solicita al usuario una frase e imprime:
# • Las palabras únicas(usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


# # Solicita una frase al usuario
# frase = input("Ingresá una frase: ")

# # Divide la frase en palabras
# palabras = frase.split()

# # Crea un set con las palabras únicas
# palabras_unicas = set(palabras)

# # Crea un diccionario para contar las apariciones de cada palabra
# recuento = {}
# for palabra in palabras:
#     if palabra in recuento:
#         recuento[palabra] += 1
#     else:
#         recuento[palabra] = 1

# # Muestra los resultados
# print("Palabras_únicas:", palabras_unicas)
# print("Recuento:", recuento)

# ----------------------------Ejercicio 6-----------------------------------------------------
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Inicializa un diccionario para almacenar los alumnos y sus notas

# alumnos = {}
# # Pedir datos de 3 alumnos
# for i in range(3):
#     nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
#     notas = input(f"Ingresá las 3 notas de {nombre} separadas por coma: ")
#     # Convertir las notas a enteros y guardarlas como una tupla
#     tupla_notas = tuple(map(int, notas.split(',')))
#     alumnos[nombre] = tupla_notas

# # Mostrar el promedio de cada alumno
# print("\nPromedios:")
# for alumno, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{alumno}: {promedio:.2f}")

# ----------------------------Ejercicio 7-----------------------------------------------------
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial(sin repetir).

# # Listas de estudiantes que aprobaron cada parcial (usamos sets)
# parcial1 = {"Ana", "Luis", "Marta", "Juan"}
# parcial2 = {"Luis", "Sofía", "Juan", "Pedro"}

# # Estudiantes que aprobaron ambos parciales (intersección)
# ambos = parcial1 & parcial2

# # Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
# solo_uno = parcial1 ^ parcial2

# # Estudiantes que aprobaron al menos un parcial (unión)
# al_menos_uno = parcial1 | parcial2

# # Mostramos los resultados
# print("Aprobaron ambos parciales:", ambos)
# print("Aprobaron solo uno de los dos:", solo_uno)
# print("Aprobaron al menos un parcial:", al_menos_uno)

# -----------------------------Ejercicio 8-----------------------------------------------------
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# # Creamos un diccionario con algunos productos
# stock = {
#     "manzana": 10,
#     "banana": 5
# }

# # Pedimos al usuario un producto
# producto = input("Ingresá el nombre de un producto: ")

# # Verificamos si el producto ya está en el diccionario
# if producto in stock:
#     print("Stock actual:", stock[producto])
#     unidades = int(input("¿Cuántas unidades querés agregar?: "))
#     stock[producto] += unidades
#     print("Nuevo stock:", stock[producto])
# else:
#     unidades = int(
#         input("El producto no existe. ¿Cuántas unidades querés agregar?: "))
#     stock[producto] = unidades
#     print(f"{producto} agregado con {unidades} unidades.")

# # Mostramos el stock completo
# print("Stock total:", stock)

# -----------------------------Ejercicio 9-----------------------------------------------------
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.


# # Agenda con tuplas como clave: (día, hora)
# agenda = {
#     ("lunes", "10:00"): "Reunión",
#     ("lunes", "14:00"): "Clase de matemáticas",
#     ("martes", "09:00"): "Clase de Arq y Sistemas",
#     ("martes", "11:00"): "Clase de programación",
#     ("miércoles", "13:00"): "Reunión de equipo",
#     ("jueves", "16:00"): "Clase de Organizacion Empresarial",
#     ("viernes", "10:30"): "Clase de Bases de Datos",
#     ("martes", "15:00"): "Clase de inglés"
# }

# # Pedimos al usuario el día y la hora que quiere consultar
# dia = input("Ingresá el día: ").lower()
# hora = input("Ingresá la hora (formato HH:MM): ")

# # Consultamos agenda
# clave = (dia, hora)

# if clave in agenda:
#     print("Actividad:", agenda[clave])
# else:
#     print("No hay ninguna actividad agendada en ese horario.")


# -----------------------------Ejercicio 10-----------------------------------------------------
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# Diccionario original: país:capital
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

# Diccionario invertido: capital:país
invertido = {}

# Recorremos el original para invertirlo
for pais, capital in original.items():
    invertido[capital] = pais

# Mostramos el resultado
print("Diccionario invertido:", invertido)
