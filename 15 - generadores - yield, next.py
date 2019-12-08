# Los generadores son estructuras que extraen de una funcion valores  
# que se almacenan en objetos iterables. Cada vez que se almacena un valor
# permanece pausado hasta que se solicita el siguiente (suspensión de estado)
# Son muy útiles con listas  de valores infinitos
# Es mas eficiente que una función tradicional ya que esta devuelve los valores todos juntos
# en cambio los generadores de uno en uno (con next() puedo solicitarlos de a uno).
#---------------------------------
def funcNumerosPares(limite):
	num=1
	miLista=[]

	while num-1<limite:
		miLista.append(num*2)
		num=num+1

	return miLista

print(funcNumerosPares(5))
#----------------------------------
def genNumerosPares(limite):
	num=1

	while num-1<limite:
		yield num*2 #El generador utiliza yield, y puede o no también utilizar un return
		num=num+1

for i in genNumerosPares(5):  #recorro uno por uno
	print(i)

numerosPares = genNumerosPares(5) #puedo almacenar los resultados en una variable y luego pedirlos de a uno

print("Probando next()...")
print(next(numerosPares)) #el generador avanza un índice y queda en estado de suspensión entre llamada y llamada
print("mas código...")
print(next(numerosPares))
print("mas código...")
print(next(numerosPares))