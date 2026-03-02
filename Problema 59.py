#Problema 59
def suma():
    lis=[]
    z=int(input("Cantidad de números a ingresar"))
    for i in range(z):
        x=float(input("Ingrese un número para la sumatoria"))
        lis.append(x)
    suma1=sum(lis)
    return lis,suma1
suma2=suma()
print("La sumatoria de los números dados es: ",suma2)

