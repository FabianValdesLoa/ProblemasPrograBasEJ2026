#Problema 29:División segura
print("dé un número para que sea el dividendo")
x=float(input())
print("dé un número para que sea el divisor")
y=float(input())
if y==0:
    print("ERROR, el divisor no puede ser 0")
else:
    z=x/y
    print("el resultado es: ",z)
