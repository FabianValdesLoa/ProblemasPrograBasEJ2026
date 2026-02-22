#Problema 49
n=int(input("Productos a agregar"))
prod=[""]*n
cod=[""]*n
ex=[0]*n
for i in range(n):
    prod[i]=input("Nombre del producto")
    cod[i]=input("Número de código de barras")
    ex[i]=input("Productos existentes")
z=0
while z!=2:
    z=int(input("si desea buscar un producto presione:1, si desea mostrar todo el inventario:2, si desea salir presione cualquier otro botón"))
    if z==1:
        a=input("Producto a encontrar")
        for i in range(n):
            if prod[i]==a:
                print("Producto: ",prod[i],"Código de barras: ",cod[i],"y",ex[i],"productos en existencia")
        else:
            print("no se encontró el producto")
    elif z==2:
        for i in range(n):
            print("producto",prod[i],"código de barras",cod[i],"existencia",ex[i])
    else:
        print("programa cerrado")
