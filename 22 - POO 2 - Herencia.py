class Vehiculo():
	def __init__(self, marca, modelo):
		self.tipo=""
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, 
		"\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, 
		"\nFrenando: ", self.frena)

class VElectrico(Vehiculo):
	def __init__(self, marca, modelo): #necesito recibir los parámetros que necesitaré al llamar a super()
		super().__init__(marca, modelo) # LAMO AL CONSTRUCTOR DEL QUE SIEMPRE HEREDARÁ CUALQUIER VEHÍCULO
		self.autonomia=100
		self.cargando=False

	def enchufar(self):
		self.cargando=True

	def desenchufar(self):
		self.cargando=False

	def estaCagando(self):
		if self.cargando:
			return "Está cargando"
		else:
			return "No está cargando"

class Camioneta(Vehiculo):
	carga=False

	def cargar(self, carga):
		self.carga=carga

	def vaCargada(self): #NO SE PUEDE LLAMAR A UN MÉTODO IGUAL QUE A UN ATRIBUTO
		if self.carga:
			return "La camioneta está cargada"
		else:
			return "La camioneta no está cargada"

	def estado(self): #PUEDO SOBRESCRIBIR UN MÉTODO Y CUANDO LO LLAME DESDE LA INSTANCIA DE ESTA CLASE, 
					  #SOBRESCRIBE AL MÉTODO DE LA CLASE DE LA QUE LO HEREDA
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, 
		"\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, 
		"\nFrenando: ", self.frena, "\n", self.vaCargada())

class Moto(Vehiculo): #ESTA ES LA FORMA DE HEREDAR
	caballito=""

	def hacerCaballito(self):
		self.caballito="Voy haciendo caballito"

	def estado(self): #PUEDO SOBRESCRIBIR UN MÉTODO Y CUANDO LO LLAME DESDE LA INSTANCIA DE ESTA CLASE, 
					  #SOBRESCRIBE AL MÉTODO DE LA CLASE DE LA QUE LO HEREDA
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, 
		"\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, 
		"\nFrenando: ", self.frena, "\n", self.caballito)

class BicicletaElectrica(VElectrico, Vehiculo): # DE ESTA MANERA PUEDO UTILIZAR LA HERENCIA MULTIPLE, SE LE DA LA PREFERENCIA AL CONST. DE 
											    # LA PRIMERA (A LA IZQUIERDA) CLASE INFORMADA
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, 
		"\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, 
		"\nFrenando: ", self.frena, "\n", self.estaCagando())


miMCamioneta=Camioneta("Ford", "Ranger")
miMCamioneta.cargar(True)
miMCamioneta.arrancar()
miMCamioneta.estado() #AL LLAMAR AL MÉTODO HEREDADO DESDE LA ISTANCIA DE ESTA CLASE QUE HEREDA, SE SOBRESCRIBE EL MÉTODO ANTERIOR

miMoto=Moto("Honda", "CBR")
miMoto.hacerCaballito() #AL LLAMAR AL MÉTODO HEREDADO DESDE LA ISTANCIA DE ESTA CLASE QUE HEREDA, SE SOBRESCRIBE EL MÉTODO ANTERIOR
miMoto.estado()

miBicicletaElectrica=BicicletaElectrica("Style", "EC10")
miBicicletaElectrica.arrancar()
miBicicletaElectrica.acelerar()
miBicicletaElectrica.estado()