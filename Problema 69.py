#Problema 69
def val(correo):
    if "@" in correo:
        return "Correo válido"
    else:
        return "Correo inválido"
correo=input("Ingresa tu correo: ")
resultado=val(correo)
print(resultado)
