#Problema 62
def calfin(cal1,cal2,cal3):
    prom=float((cal1+cal2+cal3)/3)
    if prom<70:
        x="Te vas a extra"
    else:
        x="No te vas a extra"
    return "Promedio:",prom,x
cal1=float(input("dé la primera calificación"))
cal2=float(input("dé la segunda calificaión"))
cal3=float(input("dé la tercera calificación"))
res=calfin(cal1,cal2,cal3)
print(res)
