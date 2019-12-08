print("Verificacion de acceso")

edad = int(input("Ingrese su edad: ")) #int se puede usar también en el input

if edad < 18:
	print("No puedes pasar")
elif edad > 99: #es el elseif
	print("Edad incorrecta")
else:
	print("Puedes pasar")

print("El programa ha finalizado")

