#edad = 7
#if 0<edad<100: #concatenación de condicionales
	#print("Edad Correcta")
#else:
	#print("Edad incorrecta")
salario_presidente = int(input("Introduce el salario del presidente: "))
print("Salario del Presidente: " + str(salario_presidente)) 
#con str convierto el valor ingresado a string para poder concatenar

salario_director = int(input("Introduce el salario del director: "))
print("Salario del Director: " + str(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe de área: "))
print("Salario del Jefe de área: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario del Administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
	print("todo funciona correctamente")
else:
	print("algo funciona mal")
	