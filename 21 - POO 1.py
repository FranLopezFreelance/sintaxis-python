class Auto():

	def __init__(self): # CONSTRUCTOR
		self.largoChasis=250 # LAS PROPIEDADES VAN ANTECEDIDAS DE self.
		self.anchoChasis=120
		self.__ruedas=4 # CON 2 GUINOES BAJOS SE ENCAPSULA LA PROPIEDAD
		self.__enMarcha=False
		print(self.__estado())

	def __estado(self):
		if self.__enMarcha:
			return "El auto está en marcha"
		else:
			return "El auto está detenido"

	def accion(self, accion):
		if self.__enMarcha:
			self.__enMarcha=accion
			print(self.__estado())
		elif not self.__enMarcha and not self.__checkeoInterno():
			print("No se puede arrancar")
		else:
			self.__enMarcha=accion
			print(self.__estado())

	def __checkeoInterno(self):
		print("Realizando checkeo interno ...")
		self.gasolina="ok"
		self.aceites="ok"
		self.puertas="cerradas"
		if self.gasolina == "ok" and self.aceites == "ok" and self.puertas == "cerradas":
			return True
		else:
			return False

print(" -- Instanciando el primer auto -- ")
miAuto = Auto()

miAuto.accion(True)
miAuto.accion(False)

print(" -- Instanciando el segundo auto -- ")
miAuto2 = Auto()

miAuto2.accion(True)
miAuto2.accion(False)
