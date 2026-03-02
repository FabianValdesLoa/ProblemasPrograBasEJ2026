#Problema 58
sn=""
def lis():
    lista=[]
    z=int(input("¿Cuántos son los números a agregar?"))
    for i in range(z):
        x=float(input("Ingrese su número"))
        lista.append(x)
    return lista
lista1=lis()
print("La lista de números es: ", lista1)
