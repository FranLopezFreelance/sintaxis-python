for i in range(5, 50, 3): #recorre desde el 5 hasta el 49, saltantando de 3 en 3
	print(f"El valor de i es: {i}") 
	#poniendo la f (es una función de formato) antes del string, 
	#sin espacio, se puede imprimir un string con una variable dentro

diccionario = {"Argentina":"Buenos Aires", "España": "Barcelona"}

for i in diccionario.values(): #sin el .values() , por defecto imprime los .keys()
	print(i)

nombre = "Juan"

for i in range(len(nombre)): #se puede usar la función len de un string para el range
	print(nombre[i] + str(i), end=" ")