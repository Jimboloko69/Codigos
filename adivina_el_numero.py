import random

min = 1
max = 20
intentos = 0

print ("Hola, cual es tu nombre?")
usuario = input ()

print ("Hola, "+usuario+" juguemos un juego, trata de adivinar un numero entre "+str(min)+" y "+str (max)+"\n")

numero = random.randint (min, max)
while intentos < 6:
        print("Intentalo")
        intento = input()
        intento = int (intento)

        intentos = intentos + 1

        if numero < intento:
            print ("Estas por arriba de mi numero")

        if numero > intento:
            print ("Estas por debajo de mi numero")

        if numero == intento:
            break

if numero == intento:
    print("Has acertado, mi numero era "+str (numero)+", lo has hecho en "+str (intentos)+" intentos")

if numero != intento:
    print ("No lo conseguiste, mi numero era "+str (numero)+"")



                