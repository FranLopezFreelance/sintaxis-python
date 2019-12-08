#Se requiere la libraría IO del módulo standard de Phyton https://docs.python.org/3.8/library/io.html?highlight=io#module-io
#CREACION - APERTURA - MANIPULACION - CIERRE de archivos
from io import open

archivo_texto1=open("archivo.txt", "w") 
    # nombre de archivo (si no existe lo crea), y el modo (write escritura)
frase="Estupendo dia para estudiar Python.\nMejor me voy..."
archivo_texto1.write(frase) # manipulacion
archivo_texto1.close()

archivo_texto2=open("archivo.txt", "a")
    # nombre de archivo (si no existe lo crea), y el modo (append agregar)
archivo_texto2.write("\nAgregando una nueva linea")
archivo_texto2.close()

archivo_texto3=open("archivo.txt", "r") 
    # nombre de archivo (si no existe lo crea), y el modo (read lectura)
#texto=archivo_texto2.read() # lectura, de todo el archivo
texto_lista=archivo_texto3.readlines() # lectura, linea por linea creando una lista
archivo_texto3.close()
#print(texto)
print(texto_lista[2])


