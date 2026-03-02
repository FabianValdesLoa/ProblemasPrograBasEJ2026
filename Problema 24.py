#Problema 24:Interés simple y compuesto
print("dé el capital inicial")
capi=float(input())
print("dé la tasa del interés anual")
inte=float(input())
print("número de periodos")
per=float(input())
cfs=capi*(1+(inte*per/100))
cfc=capi*(1+inte/100)**per
print("Capital final con interés simple es: ",cfs,"Capital final con interés compuesto es: ",cfc)
