#Problema 50
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
        x=0
        x=int(input("si desea buscar por nombre presione:1, si desea por código presione:2"))
        if x==1:
            a=input("Producto a encontrar por nombre")
            for i in range(n):
                if prod[i]==a:
                    print("Producto: ",prod[i],"Código de barras: ",cod[i],"y",ex[i],"productos en existencia")
            else:
                print("no se encontró el producto")
        elif x==2:
            b=input("producto a encontrar por código")
            for i in range(n):
                if cod[i]==b:
                    print("Producto: ",prod[i],"Código de barras: ",cod[i],"y",ex[i],"productos en existencia")
                else:
                    print("no se encontró el producto")
    elif z==2:
        for i in range(n):
            print("producto",prod[i],"código de barras",cod[i],"existencia",ex[i])
    else:
        print("programa cerrado")
