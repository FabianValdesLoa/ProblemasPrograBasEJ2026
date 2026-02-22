#Problema 53
datos=[]
sn=str("si")
while sn=="si":
    n=input("ingrese un dato")
    datos.append(n)
    sn=str(input("¿Quiere ingresar otro dato?,si/no"))
print(datos)
