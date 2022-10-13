
a = int (input("Primer numero \n"))
b = int (input("Segundo numero \n"))

suma = a + b;
resta = a - b;
multiplicacion = a * b;
division = a / b;

print ("Operaciones \n1 = Suma \n2 = Resta \n3 = Multiplicacion \n4 = Division")

oper = int (input())

if oper == 1:
    print  ("Resultado:" ,suma)

elif oper == 2:
    print  ("Resultado:" ,resta)

elif oper == 3:
    print  ("Resultado:" ,multiplicacion)

elif oper == 4:
    print  ("Resultado:" ,division)



