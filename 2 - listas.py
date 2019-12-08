#Las listas son arrays

mi_lista = ["Rodrigo", True, "Marta", "Luciana"]
#print(mi_lista[:]) #Imprime lista completa
#print(mi_lista[2]) #Imprime el item marcado
#print(mi_lista[:2]) #Imprime todo hasta antes de la posicion marcada
#print(mi_lista[2:]) #Imprime todo desde la posicion marcada

mi_lista.append("Juan")

#print(mi_lista)

mi_lista.insert(2,"Domingo") #Inserta elemento en la posicion indicada

#print(mi_lista)

mi_lista.extend(["Pedro", 5, "Juanita"]) #amplia la lista

#print(mi_lista)
#print(mi_lista.index("Pedro"))
print(True in mi_lista) #devuelve True si está incluido en la lista
mi_lista.remove(True) #Elimina un el elemento indicado
mi_lista.pop() #Elimina el ultimo elemento
print(mi_lista[:])

mi_lista2 = ["Gato", "Perro", "Pato"]

mi_lista3 = mi_lista + mi_lista2 #el + concatena listas
print(mi_lista3[:])
print(mi_lista3[:] * 2) #el * funciona como repetidor
print(mi_lista3.count("Gato")) #muestra la cantidad de apariciones
print(len(mi_lista)) #muestra la cantidad de items