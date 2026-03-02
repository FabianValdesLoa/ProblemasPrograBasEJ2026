#Problema 37:Interés compuesto por repetición
otro="si"
while otro=="si":
    print("dé su capital inicial")
    c=float(input())
    print("dé la tasa de interés")
    i=float(input())
    print("dé el número de periodos")
    n=int(input())
    m=c*(1+i)**n
    print("su monto final es de: ",m)
    print("si desea calcular otro monto teclee 'si', si no es así teclee cualquier otra cosa")
    otro=input()
print("que tenga un buen día")
