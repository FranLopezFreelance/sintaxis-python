#capturar errores en tiempo de ejecución
#la información con la que nos encontramos son:
	# - pila de llamadas, con el archivo y la líneas del error
	# - nombre del error

def sumar(num1, num2):
	return num1+num2

def restar(num1, num2):
	return num1-num2

def multiplicar(num1, num2):
	return num1*num2

def dividir(num1, num2):
	try: #capturamos un posible error
		return num1/num2
	except ZeroDivisionError: #de tipo ZeroDivisionError
		return "Operación no admitida (dividir por 0)"

print("Programa para realizar operaciones")

while True: # de esta manera podemos capturar un error al ingresar datos y que si son errónos los vuelva a solicitar
	try:
		num1=int(input("Ingresa el primer número: "))
		num2=int(input("Ingresa el segundo número: "))
		break
	except ValueError:
		print("Se debe introducir valores numéricos")

operacion=input("Ingresa la operación a realizar (sumar, restar, multiplicar, dividir): ")

if operacion=="sumar":
	print("El resultado es: " + str(sumar(num1, num2)))
elif operacion=="restar":
	print("El resultado es: " + str(restar(num1, num2)))
elif operacion=="multiplicar":
	print("El resultado es: " + str(multiplicar(num1, num2)))
elif operacion=="dividir":
	print("El resultado es: " + str(dividir(num1, num2)))
else:
	print("Operacion no admitida.")

print("El programa ha finalizado")