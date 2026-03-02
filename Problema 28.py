#Problema 28:Mayoría de edad
print("¿Cuál es tu edad?")
x=int(input())
if x>=18:
    print("eres mayor de edad")
elif 0<x<18:
    print("eres menor de edad")
else:
    print("edad inválida")
