#para crear un paquete hace falta que la carpeta del paquete tenga un archivo con nombre __init__.py
#cuando hago la importacion indico la carpeta donde tengo los modulos, y deonde cree el __init__.py COMO SI FUERA UN OBJETO
from modulos.funciones_matematicas import * #indico la carpeta.nombre_modulo
from modulos.sub_modulos.potencia import * #indico carpeta.subcarpeta.nombre_modulo

sumar(2, 1)
restar(2, 1)
multiplicar(2, 1)
potencia(4, 2)