# archivo=open("archivo.txt", "r")
#print(archivo.read())
# archivo.seek(11) # mueve el puntero al principio del archivo
# print(archivo.read(5)) #dentro de read() el parámetro me dice cuantos caracteres leer
# print(archivo.read())
# archivo.seek(len(archivo.readline())/2) 
    #esto podria usarlo para situar el puntero a la mitad del archivo
#print(archivo.read())
# archivo.close()

archivo2=open("archivo.txt", "r+") 
    #abre el archivo en modo lectura/escritura
    #con el puntero al principio del archivo
#print(archivo2.readlines())
# lineas_texto=archivo2.readlines()
# lineas_texto[len(lineas_texto)-1]="Linea editada por lista\n"
# archivo2.seek(0)
# archivo2.writelines(lineas_texto) #se le pasa una lista
# archivo2.seek(0)
#archivo2.write("Agrego algo al Comienzo del texto... ")
# print(archivo2.read())
# archivo2.close()

#archivo2.seek(0)
lista2=["Primera Linea\n", "Segunda Linea\n", "Tercera Linea\n", "Cuarta Linea\n"]
archivo2.writelines(lista2)
archivo2.seek(0)
print(archivo2.read())


