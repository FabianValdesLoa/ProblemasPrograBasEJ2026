#Problema 38:Validación de número entre 1 y 5
print("dé un número entre 1 y 5")
x=float(input())
while x<1 or x>5:
    print("número no aceptado, intenta de nuevo")
    x=float(input())
print("número válido")
