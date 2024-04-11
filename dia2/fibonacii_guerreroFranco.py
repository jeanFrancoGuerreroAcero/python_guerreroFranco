#-------------------------------
#----DIA 2 serie fibonacci-----
#-------------------------------
print("bienvenido")
print("la secuencia fibonacci se basa en el numero dado se suma con el mismo, el numero dado se suma con el anterior")
print("vamos a hacer una secuencia fibonacci")
print("hasta que numero quieres que llegue la secuencia")

def fib(n):
    p=0
    b=1
    for r in range(n):
     e= b+p
     p=b
     b=e

    return p

#desarrollado por jean franco guerrero acero - 1093909111