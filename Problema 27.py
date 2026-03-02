#Problema 27:Área o perímetro de un cuadrado
print("si desea calular el área de un cuadrado teclee 'c', si desea el perímetro teclee 'p'")
g=str(input())
if g=='c':
    print("dé un la medida de un lado del cuadrado")
    x=float(input())
    if x<=0:
        print("dé una cantidad mayor a 0")
    else:
        y=x**2
        print("el área del cuadrado es :",y)
elif g=='p':
    print("dé la medida de un lado del cuadrado")
    a=float(input())
    if a<=0:
        print("dé una cantidad mayor a 0")
    else:
        b=a*4
        print("el perímetro del cuadrado es: ",b)
else:
    print("dé el caracter 'c' o 'p'")
