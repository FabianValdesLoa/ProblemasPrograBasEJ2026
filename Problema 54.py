#Problema 54
nom=[]
aho=[]
sn=str("si")
while sn=="si":
    n=input("ingrese un nombre")
    nom.append(n)
    a=input("ingrese su ahorro")
    aho.append(a)
    sn=str(input("desea agregar otro?, si/no"))
for i in range(len(nom)):
    if float(aho[i])<1000:
        print(nom[i],"no tendrás para tu futuro")
    elif float(aho[i])>1000000:
        print(nom[i],"ya merito te retiras")
    else:
        print(nom[i],"ah mira vas bien")
        
