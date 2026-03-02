#Problema 65
def numeros():
    lis=[]
    while True:
        num=int(input("dé un número"))
        lis.append(num)
        sn=input("si quiere añadir otro número tecleé 'si'")
        if sn!="si":
            break
    return lis
nume=numeros()
def fact():
    if nume<0:
        return "no hay factorial para negativos"
    res=1
    for i in range(1, n+1):
        res*=i
    return res
x=fact()
print("Factorial de: ",nume,"es: ",x,"y los números leídos son: ",len(nume))
