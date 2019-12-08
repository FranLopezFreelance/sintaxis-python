class Moto():
	def desplazamiento(self):
		print("Me desplazo usando 2 ruedas")

class Auto():
	def desplazamiento(self):
		print("Me desplazo usando 4 ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo usando 6 ruedas")

#vehiculo=Moto()
#vehiculo=Auto()
vehiculo=Camion()

def desplazamientoVehiculo(vehiculo): #puedo pasar un objeto por parámetro sin especificar de que tipo es
	vehiculo.desplazamiento()

desplazamientoVehiculo(vehiculo)