#Problema 68
def primo(num):
    for i in range (2,num):
        if num%i==0:
            return False
    return True
def numeros():
    lis=[]
    while True:
        num=int(input("Dé un número"))
        lis.append(num)
        sn=input("si quiere añadir otro número tecleé 'si'")
        if sn!="si":
            break
    return lis
nume=numeros()
if primo(num):
    print(nume," es primo")
else:
    print(nume," no es primo")
