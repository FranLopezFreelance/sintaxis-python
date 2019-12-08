from vehiculos import *

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