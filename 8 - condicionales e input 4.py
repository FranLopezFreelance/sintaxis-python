print("Programa de Becas")
distancia = int(input("Introduce la distancia a la escuela en km.: "))
print("Distancia a la escuela: " + str(distancia))
cantidad_hermanos = int(input("Introduce la cantidad de hermanos: "))
print("Cantidad de hermanos: " + str(cantidad_hermanos))
salario_familiar=int(input("Ingresa el salario familiar mensual: "))

#if distancia>40 and cantidad_hermanos > 2 and salario_familiar <= 20000:
if distancia>40 and cantidad_hermanos > 2 or 20000 <= salario_familiar <= 40000 :
#if (distancia>40 and cantidad_hermanos) > 2 or (20000 <= salario_familiar <= 40000) :
	#también se pueden agregar paréntisis, sin paréntesis separa por or y une por and

	print("Tienes derecho a beca")
else:
	print("No tienes derecho a Beca")

