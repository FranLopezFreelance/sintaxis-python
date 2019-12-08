print("Programa de evaluación de notas de alumnos")

nota=input("Introduce la nota del alumno: ") #pide valor por teclado
def evaluacion(nota):
	valoracion="Aprobado"
	if nota<4:
		valoracion="Desaprobado"
	return valoracion

print(evaluacion(int(nota))) #se usa int porque por defecto python toma valor como string
