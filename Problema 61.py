#Problema 61
def peri():
    a=float(input("Medida de la altura del triángulo"))
    b=float(input("Medida de la base del triángulo"))
    l=((b/2)**2+a**2)**(1/2)
    p=b+2*l
    return p
print("El perímetro del triangulo dado es: ", peri())
