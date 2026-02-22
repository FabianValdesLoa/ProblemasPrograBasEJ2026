#Problema 47
mat=str(input("Nombre de la materia"))
n=int(input("Calificaciones a ingresar"))
cal=[0]*n
suma=0
for i in range(n):
    cal[i]=float(input("dé la calificación"))
    suma=suma+cal[i]
prom=suma/n
print("En la materia: ",mat,"hay un promedio de: ",prom)
