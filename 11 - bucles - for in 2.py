for i in ["Ingeniería", "Informática", 3]: #recorre tantas veces como elementos hay en una lista
	print("Hola", end=" ") # se usa para evitar saltos de línea y se puede concatenar un string

for i in "Francisco": #si lo hago contra un string recorre caracter por caracter
	print(i)


personas = ["Rodrigo", "Rocío"]

def verificar_email(email):
	valido=False
	print("Vericación del Email: " + email)
	for i in email:
		if(i == "@"):
			valido = True
	if valido:
		print("El Email es correcto")
	else:
		print("El Email es incorrecto")

for i in personas:
	verificar_email(input("Ingrese un Email para verificar: "))