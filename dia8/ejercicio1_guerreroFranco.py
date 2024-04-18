subscripcion=20000
print("\nhola bienvenido a nuestra pagina de peliculas")
print("para ver nuestras peliculas debes comprar una subscripcion")
print("que opcion deseas hacer")

quitar=20000
saldo=20000
resta=20000
saldo={}
subscripciones={ "valor de subscripcion" : 20000}

campus=True
def suscribirse():
    tiempo=int(input("cuantos años se va a suscribir: "))##cuanto tiempo se va a suscribir
    pool=tiempo*resta
    if tiempo > 0 :##si cantidad es mayo a 0 entonces
        while campus==True:
            final=saldo-pool
            if final==0:
                print("te has suscrito")
                campus==False


    else:
       print("tienes que suscribirte mas de un año")


def agregar_saldo():
    plata=int(input("cuanto dinero quieres recargar"))



def salir():
    print("espero pronto te suscribas")
    exit()





menu=f"""
1.subscripcion premiun
2.regalar subcripcion a ususario
3.agregar saldo a la cuenta
4.sali
"""
opcion=input()



internet=True
while internet==True:

    if opcion== "1":
        suscribirse()
    elif opcion=="2":
        mostrarCarrito()
    elif opcion=="3":
        agregar_saldo()
    elif opcion=="5":
        salir()
    else:
        print("por favor seleccione una opcion valida")