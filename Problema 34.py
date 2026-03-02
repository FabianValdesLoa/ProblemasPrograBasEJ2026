#Problema 34:Clasificación por edad
print("dé su edad para clasificar")
x=int(input())
if x<=0 or x>120:
    print("edad inválida")
elif x<10:
    print("niño")
else:
    if x<18:
        print("adolescente, mayor de edad")
    elif x<30:
        print("joven, mayor de edad")
    else:
        if x<60:
            print("adulto, mayor de edad")
        else:
            print("adulto mayor, mayor de edad")
