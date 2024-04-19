print("bienvenido a la tienda")##le doy la bienvenida al usuario

carrito=()##cro una lista vacia para que se guarden las cosas
producto=[]
##creo un menu que contiene los productos y la opcio que va a realizar
cantidad=[]
precio=[]
menu=f"""
estos son los productos que tenemos disponibles

-pollo      $15000
-carne      $18000
-pescado    $11000

1.añadir cosas al carrito
2.mostrar cosas del carrito
"""
print(menu)##inprimo el menu
opcio=input("que opcion desesa hacer: ")

hoy=True
while hoy==True:
    if opcio=="1":
        producto.append(input("que producto va a llevar: "))
        for i in  producto:
            cantidad.append(int(input("cuantos va a llevar: ")))
            print("producto agregado al carrito")    
            precio=int(input("escribe el precio del producto: "))

    elif opcio=="2":
        print("cosas que lleva en el carrito")
        print(carrito)
        exit()
    else:
        print("opcion no valida")
            