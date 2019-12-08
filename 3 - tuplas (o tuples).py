#las Tuplas "tuple" son listas inmutables, que son más rápidas en ejecución y ocupan menor espacio en memoria
#Se puede extraer partes, pero esto da una nueva tupla
#Se pueden formatear cadenas y se puede utilizar como clave en un diccionario (las listas no)
#Van encerradas entre (), que hasta pueden obviarse
mi_tupla = ("Juan", 13, True, "Perro", "Juan")
#print(mi_tupla_sin_parentesis)
#print(mi_tupla[:]) #Imprime tupla completa
#print(mi_tupla[2]) #Imprime el item marcado
#print(mi_tupla[:2]) #Imprime todo hasta antes de la posicion marcada
#print(mi_tupla[2:]) #Imprime todo desde la posicion marcada

#Una tupla se puede convertir en lista y viceversa
mi_lista_de_tupla = list(mi_tupla)
print(mi_lista_de_tupla)

mi_tupla_de_lista = tuple(mi_lista_de_tupla)
print(mi_tupla_de_lista)

print(mi_tupla.count("Juan")) #Cuenta las apariciones
print(len(mi_tupla)) #muestra la cantidad de items
mi_tupla_unitaria = ("Juan",) #con la , define una tupla unitaria
print(mi_tupla_unitaria)

mi_tupla_sin_parentesis = "Juan", 13, 1, 1995 # Se dice empaquetado de tupla
nombre, dia, mes, anio = mi_tupla_sin_parentesis # Esto es desempaquetado de tupla
print(nombre, dia, mes, anio)
