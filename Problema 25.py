#Problema 25:Ecuación de la recta
print("dé el número x1")
x1=int(input())
print("dé el número y1")
y1=int(input())
print("dé el número x2")
x2=int(input())
print("dé el número y2")
y2=int(input())
m=(y2-y1)/(x2-x1)
b=y1-m*x1
print("La ecuación de la recta es:y=",m,"x+",b)
