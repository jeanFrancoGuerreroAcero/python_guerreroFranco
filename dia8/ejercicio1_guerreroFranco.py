subscripcion=20000
print("\nhola bienvenido a nuestra tienda de periodicos")##saludo al usuario
print("para ver nuestras peliculas debes comprar una subscripcion")
saldo=int(input("Ingresa saldo "))##pido al usuario el saldo que va a agregar para hacer las compras
def suscribirse():##creo la funcion suscribirse
    print("nuestra subscripcion tiene un valor de ",subscripcion)
    tiempo=int(input("cuantos años se va a suscribir: "))##le prefunto cuanto tiempo se va a suscribir

    desde=int(input("desde que años desa que empiece a trascurrir la subscripcion"))##creo la variable desde para preguntar cdesde cuando empezara a transcurrir la subscripcion
    if desde >= 2024:##si la variable desde es mayor o igual al 2024 entonces
        fin=desde+tiempo##creo variable fin para que se sume,el tiempo en que empezara a transcurrir la sub con el tiempo que dura la sub
        print("su susbcripcion va a empezar a ser valida desde",desde,"hasta",fin)##muestro al usuario cuanto le costo y cuanto durara la sub
    else:##si ingresa un año que sea menor a 2024 entonces le imprimo 
        print("\nla subscripcion debe empezar a transcurrir desde 2024")
    valor=tiempo*subscripcion
    if saldo >= valor :##si el saldo es mayor a lo que cuesta por el tiempo que va a pagar
        print(f"Has comprado la suscripcion por {tiempo} Años")##muestro por cuanto tiempo compro
        quita=valor-saldo##creo variable que le quite al saldo
        print("")
        print(f"tu subscripcion por {tiempo} año te costo: {valor}")##muestro cuanto le costo y cuanto dura la sub
        print("te queda un saldo restante de: ",quita)##muestro cuanto le quedo de saldo
    else:##ssi no tiene el sufciente saldo inprimo 
       print("no tienes suficiente saldo")##si no le alcanza entonces inprimo


def regalar():##creo la funcion de regalar
    if saldo >= 20000:##si tengo un saldo mayor al valor de la subscripcion entonces
        nombreRegalar=input("ingresa el nombre de el ususario al que le quieres regalar la subscripcion")##pido al usuario el nombre de la persona a la que le va a ergalar al sub
        cuantoTiempo=int(input("por cuanto tiempo desea regalare la subscripcion"))##pido cuanto tiempo va a durar la sub
        desde=int(input("desde que años desa que empiece a trascurrir la subscripcion"))##desde que año empezara a transcu
        if desde >= 2024:##si el año que ingresa es mayor a 2024 entonces
            fin=desde+cuantoTiempo##creo la variable fin para qur muestre hasta cuando durara la sub
            print("su susbcripcion va a empezar a ser valida desde",desde,"hasta",fin)##muestro al usuario desde cuanto y hasta cuando durara la sub
            print("le regalo una subscripcion a ",nombreRegalar)##muestro a quien le regalo la sub
        else:
            print("\nla subscripcion debe empezar a transcurrir desde 2024")##si el año es menor a 2024 esntonces inprimo que tiene que ser mayor
    else:##si no tiene el saldo suficiente inprimo 
        print("no tiene saldo suficiente para regalar una subscripcion")



def salir():##creo la funcion de salir
    print("espero pronto te suscribas")##me despido del usuario
    exit()##finalizo el progra,a

##creo un menu interactivo con el usuario
menu=f"""#
que opcion deseas realizar

1.subscripcion premiun
2.regalar subcripcion a ususario
3.salir
"""
print(menu)###muestro el ,emu
opcion=input()##leo que opcion desea elegoir el usuario

if opcion== "1":##si escoge la opcion 1 llamo a la funcion suscribirse
    suscribirse()
elif opcion== "2":##si escoge la opcion 2 llamo a la funcion regalar
    regalar()
elif opcion=="3":#si escoge la opcion 3 llamo a la funcion salir
    salir()
else:##si no escoge una opcion correcta inprimo
    print("por favor seleccione una opcion valida")

##realizado por jean franco guerrero acero --1093909111
