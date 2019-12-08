import math

print("Cálculo de raíz cuadrada.")
def calculaRaiz(num1):
	if num<0:
		raise ValueError("El número debe ser positivo")
	else:
		return math.sqrt(num1)
num=int(input("Ingresa un número: "))
try:
	print(calculaRaiz(num))
except ValueError as ErrorNumeroNegativo: #si quiero adaptar el error en el excep puedo poner un alias
	print(ErrorNumeroNegativo) #y en el print envío el error que definé anteriormente

print("El programa ha terminado")

