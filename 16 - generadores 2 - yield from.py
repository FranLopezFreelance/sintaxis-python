# yield from permite prescindir de un bucle for anidado

def devuelve_ciudades(*ciudades): #el * antes del argunmento marca que no se sabe la cantidad elementos serán
	 							  # y además que es una tupla	
	 for elemento in ciudades:
	 	#for subElemento in elemento: #	  
	 		#yield subElemento
	 	yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia") 

print(next(ciudades_devueltas))							  
print(next(ciudades_devueltas))	
						  
