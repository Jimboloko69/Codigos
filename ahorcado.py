from itertools import count

import getpass
from re import A

palabra = getpass.getpass("Hola jugador 1, cual es la palabra? \n")

palabra = str (palabra)

intentos = 0

x =len(palabra)

x =int(x)

print ("La palabra tiene "+str (x)+" letras \n")

intento = input()

intento = str (intento)

while intentos < 6:
        print("Intentalo")

        intento = input()
        intento = str (intento)
        intentos = intentos + 1

        if intento == palabra:
            break


if palabra == intento:
    print("Has acertado, mi palabra era "+str (palabra)+", lo has hecho en "+str (intentos)+" intentos")

if palabra != intento:
    print ("No lo conseguiste, mi palabra era "+str (palabra)+"")
