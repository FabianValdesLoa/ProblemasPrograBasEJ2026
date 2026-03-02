#Problema 45:Calculadora con repetición por opreación
s="si"
while s=="si":
    print("si desea hacer una suma, teclee:'1', una resta:'2', una multiplicaión:'3', una división:'4', un exponente:'5' o un módulo(residuo):'6'")
    oper=int(input())
    x="si"
    while True:
        if oper==1:
            print("1er número")
            a=float(input())
            print("2do número")
            b=float(input())
            c=a+b
            print("resultado: ",c)
        elif oper==2:
            print("1er número")
            a=float(input())
            print("2do número")
            b=float(input())
            c=a-b
            print("resultado: ",c)
        elif oper==3:
            print("1er número")
            a=float(input())
            print("2do número")
            b=float(input())
            c=a*b
            print("resultado: ",c)
        elif oper==4:
            print("1er número")
            a=float(input())
            print("2do número")
            b=float(input())
            if b==0:
                print("no se divide entre 0")
            else:
                c=a/b
                print("resultado: ",c)
        elif oper==5:
            print("1er número")
            a=float(input())
            print("2do número")
            b=float(input())
            c=a**b
            print("resultado: ",c)
        elif oper==6:
            print("1er número")
            a=float(input())
            print("2do número")
            b=float(input())
            c=a%b
            print("resultado: ",c)
        else:
            print("opción inválida")
        print("¿deseas repetir la misma operación? 'si'/'no'")
        x=str(input())
        if x!="si":
            break
    print("¿deseas hacer una operación diferente?'si'/'no'")
    y=str(input())
    if y!="si":
        print("calculadora cerrada")
        break
    print("si desea hacer otra operación teclee 'si'")
    s=str(input())
