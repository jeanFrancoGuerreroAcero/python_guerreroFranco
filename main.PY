#-------------------------------
#----DIA 1 CHEAT SHEET PYTHON-----
#-------------------------------

#imprimir hola mundo
print("hola mundooooo")

#DATOS PRIMITIVOA

#NUMERO

NUMERO = 1 #nombe variable = valor
print(NUMERO)#imprimir(tipo(variable))
print(type(NUMERO))

#DECIMAL

numeroDecimal =1.1
print(numeroDecimal)
print(type(numeroDecimal))

#booleano

miBooleano= True
print(miBooleano)
print(type(miBooleano))

#cadena de texto

texto="tibu linda"
print(texto)
print(type(texto))

#taller

#ingresa por teclado la informacio
print("hola como te llamas")
nombre=input()
print("cuantos años tienes")
edad=input()
print("hola ",nombre," tienes ",edad," años")

#conversion de tipos de variables 

print("numero entero para convertirlo a decimal")
f=(6)
print(float(f))

#
print("vamos a convertir un decimal a entero")
decimal=(1.5)
print(int(decimal))
print(type(decimal))

#
print("vamos a converti por medio de divisio")
division=5/2
print(division)

#bucles for y while
#for
for i in range(0, 5):
   print(i)
   
#WHILE
 
i = 1
while i <= 3:
    print(i)
    i += 1
    print("fin")


numero = int(input("el numero positivo "))
while numero<0:
   print("usted escribio un numero negativo")
   print("escribalo de nuevo")
   numero=int(input("escribe un numero que sea positivo"))
   print("nos vemos luego")


#funciones (4tipos)
#sin retorno
def imprimir_simbo(simbolo,veces):
  for i in range(veces):
    print(simbolo, end=", ")
    print()#este es el salto de linea

    #g
imprimir_simbo ("0", 3)
imprimir_simbo("r", 3)
imprimir_simbo("t", 2)

#parametros y retorno
def escribe_media(x, y):
  media=(x + y) / 2
  print(f"la media de {x} y {y} es: {media}")
  return
f=6
e=9
escribe_media(f, e)
print("programa terminado")
  
#desarrollado por jean franco guerrero acero - 1093909111