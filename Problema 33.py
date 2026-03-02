#Problema 33:Evaluación de vendedor según volumen de ventas
print("dé el nombre del vendedor")
nom=str(input())
print("ventas en pesos")
vol=float(input())
if vol<1000:
    print("el vendedor: ",nom," está despedido")
elif vol<5000:
    print("el vendedor: ",nom,"está en periodo de prueba")
else:
    if vol<10000:
        print("el vendedor: ",nom," tiene un bono del 5%")
    else:
        print("el vendedor: ",nom," tiene un bono del 10%")
