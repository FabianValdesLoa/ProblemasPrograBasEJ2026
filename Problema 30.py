#Problema 30:Análisis de beneficios
print("dé el precio unitario del producto")
p=float(input())
print("dé la cantidad vendida")
c=int(input())
i=p*c
print("ingresos: ",i)
print("dé los egresos de la empresa")
e=float(input())
if i<e:
    print("la empresa está en pérdidas")
elif i>e:
    print("la empresa está generando ganancias")
else:
    print("la empresa está en punto de equilibrio")
