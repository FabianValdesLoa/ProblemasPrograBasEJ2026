#Problema 35:Orden descendente de tres números
print("dé un número")
x=int(input())
print("dé otro número")
y=int(input())
print("dé el último número")
z=int(input())
if x>=y and x>=z:
    if y>=z:
        a,b,c=x,y,z
    else:
        a,b,c=x,z,y
elif y>=x and y>=z:
    if x>=z:
        a,b,c=y,x,z
    else:
        a,b,c=y,z,x
else:
    if x>=y:
        a,b,c=z,x,y
    else:
        a,b,c=z,y,x
print("el orden descendente es: ",a,b,c)
