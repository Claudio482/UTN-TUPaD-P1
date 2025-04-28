# Ejercicios Práctico #5.1 Listas
# Alumno: Claudio Fiorito
# Tutor: Franco Gonzalez
# Fecha: 27/4/25

# ----------------------------Ejercicio 1-----------------------------------------------------
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# #Se crea lista multiplico de cuatro con función range (inicio,fin,multi)
# lista_multiplo=list(range(4,101,4))

# #Mostramos lista
# print(lista_multiplo)


# ----------------------------Ejercicio 2-----------------------------------------------------
# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

# Ej2.0
# #Listamos 5 elementos
# lista_elementos=[8.1,"Abril",False,9,"codigo"]

# #Mostramos el elemento solicitado
# print(lista_elementos[3])


# #Ej2.1
# # Listamos 5 elementos
# lista_elementos = [8.1, "Abril", False, 9, "codigo"]

# # Mostramos el elemento solicitado, pero esta vez utilizando el indexing negativo
# print(lista_elementos[-2])


# ----------------------------Ejercicio 3-----------------------------------------------------
# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
# Por ejemplo: lista_vacia = []

# #Se crea lista vacía
# lista_vacia = []

# #Agregar tres palabras con append
# lista_vacia.append("Hola")
# lista_vacia.append("Mundo")
# lista_vacia.append("Total")

# #Mostramos la lista
# print(lista_vacia)


# ----------------------------Ejercicio 4-----------------------------------------------------
# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla.
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing
# con números negativos! animales = ["perro", "gato", "conejo", "pez"]

# #Ej4.0
# #Lista original
# animales = ["perro", "gato", "conejo", "pez"]
# print("Lista original: ",animales)

# #Se remplaza indice 1 y 3
# animales[1]= "loro"
# animales[3] = "oso"

# #Lista con los remplazos
# print("Lista con los remplazos: ",animales)


# # Ej4.1
# # Lista original
# animales = ["perro", "gato", "conejo", "pez"]
# print("Lista original: ", animales)

# # Se remplaza indice 1 y 3
# animales[-3] = "loro"
# animales[-1] = "oso"

# # Lista con los remplazos
# print("Lista con los remplazos: ", animales)


# ----------------------------Ejercicio 5-----------------------------------------------------
# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.


# El programa crea una lista de números enteros desordenados.
# Luego, identifica el valor máximo de la lista y lo elimina utilizando remove().
# Finalmente, imprime la lista ya sin el número máximo.

# numeros =[8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)


# ----------------------------Ejercicio 6-----------------------------------------------------
# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar
# por pantalla los dos primeros.

# # Creamos lista del 10 al 30 con saltos de 5 en 5
# lista_multiplo = list(range(10, 31, 5))

# # Mostramos lista
# print("Se muestra solo los dos primeros de la lista: ", lista_multiplo[0:2])


# ----------------------------Ejercicio 7-----------------------------------------------------
# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos
# valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

# #Lista autos
# autos = ["sedan", "polo", "suran", "gol"]

# #Se remplaza indice 1 y 2, por cualquier valor
# autos[1]= True
# autos[2]= 8

# #Mostramos lista con el remplazo
# print(autos)


# ----------------------------Ejercicio 8-----------------------------------------------------
# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.

# #Se crea una lisa vacía
# dobles=[]

# #Se usa append y se agrega el doble a los valores dados
# dobles.append(5*2)
# dobles.append(10*2)
# dobles.append(15*2)

# #Mostramos la lista
# print(dobles)


# ----------------------------Ejercicio 9-----------------------------------------------------
# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# # Lista compras
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# # a) Agregar "jugo" a la lista del tercer cliente usando append.
# compras[2].append("jugo")
# # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# compras[1][1] = "tallarines"
# # c) Eliminar "pan" de la lista del primer cliente.
# compras[0].remove("pan")
# # d) Imprimir la lista resultante por pantalla
# print(compras)


# ----------------------------Ejercicio 10-----------------------------------------------------
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.


# lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# print(lista_anidada)
