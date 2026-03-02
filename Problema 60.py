#Problema 60
def prom(list):
    if len(list)==0:
        return 0
    return sum(list)/len(list)
nume=[]
sn=""
while True:
    num=float(input("Dé un número"))
    nume.append(num)
    sn=input("tecleé 'si', si desea añadir otro número")
    if sn!="si":
        break
res=prom(nume)
print("El promedio es:",res)
