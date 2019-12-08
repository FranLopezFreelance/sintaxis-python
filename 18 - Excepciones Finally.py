def divide():
	try:
		num1=float(input("Introduce el primer número: "))
		num2=float(input("Introduce el segundo número: "))
		print("El resultado es: " + str(num1/num2))
	except ZeroDivisionError: #de tipo ZeroDivisionError
		print("Operación no admitida (dividir por 0)")
	except ValueError:
		print("Se debe introducir valores numéricos")
	finally: #finally hace que se ejecute si o sí una parte del código que querramos
			 #también puede usarse prescindiendo del except. El programa no cae, pero no se capturan errores
		print("Cálculo finalizado")

divide()
