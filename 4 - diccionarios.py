#Es como un json, el equivalente al array asociativo en php
#clave valor
#se pueden almacenar listas, tuplas y diccionarios
mi_diccionario = {"Alemania":"Berlin", "Francia":"Paris", "Argentina":"Buenos Aires", "España":"Madrid"}
#print(mi_diccionario)
#print(mi_diccionario["Argentina"])
mi_diccionario["Italia"] = "Romanhj" #agreaga un nuevo par clave valor
mi_diccionario["Italia"] = "Roma" #sobreescribe el valor para la clave
#print(mi_diccionario)
del mi_diccionario["Francia"] #elimina la clave indicada
#print(mi_diccionario)
mi_diccionario2 = {25:"Veinticinco", 5:10, "Diez":10}
#print(mi_diccionario2)
#print(mi_diccionario2["Diez"])

#Puedo usar Tuplas para asignar los valores a un diccionario
mi_tupla = "España", "Francia", "Reino Unido"
mi_diccionario3 = {mi_tupla[0]: "Madrid", mi_tupla[1]: "Paris", mi_tupla[2]: "Londres"}
print(mi_diccionario3)
mi_diccionario4 = {"Tupla": (2018, 2019, 2020), "diccionario": {"elementos": ["Palo", "Mesa", "Silla"]}}
print(mi_diccionario4["diccionario"]["elementos"])
print(mi_diccionario4.keys()) #devuelve las claves
print(mi_diccionario4.values()) #devuelve los valores
print(len(mi_diccionario4)) #devuelve la cantidad de elementos


