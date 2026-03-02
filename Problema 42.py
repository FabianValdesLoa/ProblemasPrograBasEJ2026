#Problema 42:Confirmación de contraseña(con límite)
i=1
print("ingrese su contraseña")
contra=int(input())
for i in range(3):
    print("ingresa contraseña")
    x=int(input())
    if x==contra:
        print("contraseña correcta")
        break
else:
    print("demasiados intentos, contraseña incorrecta")
