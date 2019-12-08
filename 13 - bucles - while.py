i=1

while i<=5: #la tabulación determina el alcance del while salvo que aparezca break
	print(f"El valor de i es: {i}")
	i=i+1



edad=int(input("Introduce una edad: "))
intentos = 3

while edad < 0 or edad > 100  : 
	intentos = intentos - 1
	if intentos:
		if intentos == 1:
			print(f"Edad incorrecta, te resta {intentos} intento.")
		else:
			print(f"Edad incorrecta, te restan {intentos} intentos.")

		edad=int(input("Introduce una edad válida: "))	
	else:
		break; 

if not intentos:
	print("Has perdido las 3 oportunidades")
else:
	print(f"{edad} años, bien. Puedes pasar")
	
