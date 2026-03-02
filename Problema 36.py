#Problema 36:Repetri la elevación al cuadrado
otro="si"
while otro == 'si':
    print("dé un número para elevarlo al cuadrado")
    x=float(input())
    y=x**2
    print("su número al cuadrado es: ",y)
    otro=input("si quiere dar otro número teclee 'si', de lo contrario teclee 'no'")
