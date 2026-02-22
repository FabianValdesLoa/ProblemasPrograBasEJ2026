#Problema 51
n=int(input("¿Cuántos trabajadores hay?"))
trab=[""]*n
asis=[0]*n
for i in range(n):
      trab[i]=input("nombre del trabajador")
      asis[i]=int(input("¿asistió?, si:1  no:0"))
for i in range(n):
    if asis[i]==0:
        print("el trabajador: ",trab[i],"no asistió")
    else:
        print("el trabajador: ",trab[i],"asistió")
