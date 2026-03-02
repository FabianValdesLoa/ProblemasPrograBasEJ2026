#Problema 43:Acumulador de abonos
abono=0
while abono<=100000:
    print("cantidad a abonar")
    x=float(input())
    if x<0:
        print("no se pueden ingresar valores negativos")
        continue
    abono+=x
print("su suma total de abono es de: ",abono)
