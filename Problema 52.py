#Problema 52
prod=[""]*5
pre=[0]*5
ven=[0]*5
ing=[0]*5
for i in range(5):
    prod[i]=str(input("Nombre del producto"))
    pre[i]=float(input("Precio del producto"))
    ven[i]=float(input("Productos vendidos"))
    ing[i]=float(pre[i]*ven[i])
for i in range(5):
    print("Nombre del producto: ",prod[i],"Precio del producto",pre[i],"Productos vendidos",ven[i],"Ingreso del producto",ing[i])
