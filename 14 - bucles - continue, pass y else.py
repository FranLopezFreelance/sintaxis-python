for letra in "Python":
	if letra =="h":
		continue #saltea las siguientes instrucciones del bucle
	print("Letra: " + letra)

# Pass se suele usar para declarar una clase e implementarla más adelante. Ej_
# Class MiClase:
	#pass

email = input("Ingrese un Email: ")
for i in email:
	if i =="@":
		arroba = True
		break;
else: # este else forma parte del bucle for (podría ser de un while)
	  # se ejecuta cuando el bucle haya completado todas sus vueltas
	arroba = False

print(arroba)