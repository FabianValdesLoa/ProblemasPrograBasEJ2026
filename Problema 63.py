#Problema 63
def cuad():
    return[num**2]
nume=[]
while True:
    num=float(input("Dé un número"))
    nume.append(num)
    sn=input("Si quiere añador otro número tecleé 'si'")
    if sn!="si":
        break
res=cuad()
print("La lista es: ",num," y sus cuadrados son: ",res)
