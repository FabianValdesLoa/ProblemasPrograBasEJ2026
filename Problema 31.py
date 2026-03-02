#Problema 31:Evaluación académica
print("dé la calificación")
c=float(input())
if c<0 or c>10:
    print("dé una calificación del 0 al 10")
else:
    if c<6:
        print("la situación del alumno es: irregular")
    elif c==10:
        print("la situación del alumno es: excelencia")
    else:
        print("la situación del alumno es: regular")
