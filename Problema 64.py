#Problema 64
def mul():
    if y==0:
        return "No se divide /0"
    if x%y==0:
        return x," es múltiplo de", y
    else:
        return x, " no es múltiplo de ",y
x=int(input("dé el primer número"))
y=int(input("dé el segundo número"))
print(mul())
