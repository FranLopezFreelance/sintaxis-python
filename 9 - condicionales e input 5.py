print("Asignaturas Optativas: ")
print("Informática Gráfica - Arquitectura de Software - Usabilidad y Accesibilidad")
asignatura=input("Escribe la asignatura escogida: ").lower() #lo pasa a minúsculas

if asignatura in ("informática gráfica", "arquitectura de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura )
else:
	print("Asignatura no contemplada")
