print("hola bienvenido")##saludo al usario
print("esta es un negocio de cambio de billetes a monedas ")
print("")

monedas=[1,5,10]##monedas que tengo disponibles
pokemon=True##lo defino como verdadero para crear el bucle
while pokemon==True:##mientras sea verdadero entonces
    monedas=[10,5,1]##monedas que tengo disponibles
    dinero=int(input("cuanto dinero quieres cambiar a monedas: "))##pido que me de el billete que me quiera cambiar
    for i in monedas:##el multiplicador va a estar en las monedas 
        huy=dinero // i##creo la variable huy para que el nunmero que ingrese el usuario se divida entre las monedas en cuanto vuelve a arriba

        print("las monedas que te voy a dar son ",i,"es de ",huy)##muestro al usuario las monedas que le coy a dar y de cuanto son
        dinero=dinero % i ##dinero lo divido entre las monedas 

    if dinero > 1000:##si el dinero es mayor a 1000 entonces le pido que la plata que va a cambiar sea menor a 1000
     print("tienes que escribir un numero que este entre 1000 dolares")##ingrese un numero menor a 1000
     finalizar=print()

    print("adios que tengas un buen dia")##me despido del usuario
    pokemon=False##finalizo el programa 
    
