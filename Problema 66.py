#Problema 66
def rep(nom, calif):
    lisrep=[]
    for i in range(len(nom)):
        if calif[i]<70:
            lisrep.append(nom[i])
    return lisrep
nom=[]
calif=[]
while True:
    n=input("Nombre del alumno: ")
    c=float(input("Calificación: "))
    nom.append(n)
    calif.append(c)
    sn=input("si quiere añador otro tecleé 'si'")
    if sn!= "si":
        break
res=rep(nom,calif)
print("Los reprobados son: ",res)
