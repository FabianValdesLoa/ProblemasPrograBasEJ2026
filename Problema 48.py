#Problema 48
n=int(input("Productos a agregar"))
prod=[""]*n
cod=[""]*n
ex=[0]*n
for i in range(n):
    prod[i]=input("Nombre del producto")
    cod[i]=input("Número de código de barras")
    ex[i]=input("Productos existentes")
a=input("Producto a encontrar")
for i in range(n):
    if prod[i]==a:
        print("Producto: ",prod[i],"Código de barras: ",cod[i],"y",ex[i],"productos en existencia")
else:
    print("no se encontró el producto")
