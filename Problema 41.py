#Problema 41:Confirmación de contraseña(sin límite)
print("ingrese su contraseña")
contra=str(input())
x=""
while x!=contra:
    print("confirme contraseña")
    x=str(input())
print("contraseña válida")
