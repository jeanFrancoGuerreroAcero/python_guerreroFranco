import random

print("")
T=input()## el numero de ejercicios que se haran
N=input().split()##los numeros que estaran dentro de est lista, los cuales seran los numeros divisbles entre si para ver si son divisibles entre si
borroCasette=len(N)##divido N entre si para que me muestre cuantos numeros ingrese
k=0##este es el divisor
posibles=0
hoy=True##defino como verdadero para crear el bucle
while hoy==True:##mientras hoy sea verdadero se continuara el ciclo

    for i in  T:
     T=i-1
     
    for i in k:
     k=i+1##cada vez que pase se le añade 1 al divisor,example cuando vuelva a pasar sera 2
    for i in N:
        ai=random.choice(N)
        aj=random.choice(N)
        if ai<=aj:
            if 1<ai and aj:
               if ai!=aj:
                  mañana=(ai+aj)
                  calor=mañana//k
                  if calor==int:
                     posibles=i+1

print(T)
print(N)
print(borroCasette),print(k)
print("")
print("los casos posibles son: ",posibles)


