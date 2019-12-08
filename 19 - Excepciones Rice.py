def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas") # raise permite enviar un mensaje de error
		# también se puede definir una clase con el nombre que uno elija y que sea un tipo de error custom
	if edad<20:
		print("Eres muy jóven")
	elif edad<40:
		print("Eres jóven")
	elif edad<65:
		print("Eres adulto")
	elif edad<100:
		print("Cuidate...")

evaluaEdad(-15)
