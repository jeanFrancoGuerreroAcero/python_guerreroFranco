def prime(numero):
    ##funcion numeros primos
    if numero <= 1:##si es igua o mayor a 1 entonces retorno
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:##si numero es dividido entre 2 sera comparado con 0 o numero dividido entre 3 sera compatado con 0
        return False
    i = 5
    while i * i <= numero:##mientras i se multiplique en si mismo y nos de el numero que ingresa entonces
        if numero % i == 0 or numero % (i + 2) == 0:##si el numero que ingresa es dividido en 2 y es comparado y da 0 o da el numero ingresado entonces se divide entre el acumulador mas 2 dando como resultado comparado a 0
            return False
        i += 6
    return True

def coco():
    capa=True
    
    while capa:
        print("hola bienvenido")##saludo al usuario
        print("espero que estes bien")
        print("vamos a verificar si un numero es primo o no")
        print("escoge una opcion")

        print("")


        print("1. Verificar numero")##le doy las opciones a escoger
        print("2. ya no quieres verificar mas numeros")
        print("3. Información adicional")
        
        opcio = input("Ingrese el número de la opción que desea: ")##agrego la variable opcio
        
        if opcio == '1':##si opcion 1 entonces
            num = int(input("escribe un numero para verificar "))##pido el numero a verificar
            if prime(num):##si num
                print(f" si es numero primo")##escribir que es primo
            else:##si no
                print(f" no es número primo")##escribir que no es primo

        elif opcio == '2':##si opcio 2 entonces se finaliza el programa
            print("paraste el programa")##me despido del usuario
            print("nos vemos luego")
            print("adios,que pases un buen dia")  
            break##uso break para cerrar el programa
        
        elif opcio == '3':##si opcio 3 entonces le explico sobre los numeros primos y le digo que este programa fue realizado por mi
            print("Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero")
            print("autor del aplicativo\njean franco guerrero acero")
        
        else:
            print("esta opcion no es correcta,escribe una opcion nuevamente")##si no esta ingresando una opcion correscta le pido que vuelva a escribir numero

if __name__ == "__main__":##añado la construccion de script
    coco()


##punto numero 2

import random
import string

def cometa(longitud, mayus, minuscu, numeros ):
    caracteres = ''
    if mayus:##si es mayucula el acumulado de string.ascii_uppercase para que me de las letra en mayucula
        caracteres += string.ascii_uppercase
    if minuscu:##si es minuscula el cumulador de string.ascii_lowercase para que me de las letra en minuscula
        caracteres += string.ascii_lowercase
    if numeros:##si es numero el acumulador de string.digits para que me devuelva la cadena
        caracteres += string.digits
   
    if not caracteres:##si no es un numero entonces 
        print("tienes que ingresar almenos una letra ")
        return ''##y me retorno

    password = ''.join(random.choice(caracteres) for _ in range(longitud))##la contraseña es el resultado aleatorio en la lista caracteres en el rango longitud
    return password

def preferen():##defino la funcion preferen
    longitud = input("que longitud va a tener la contraseña ")##longitud es igual a la longitus que ingrese el usuario
    while not longitud.isdigit():##mientras not se identifique que solo tenga numeros
        print("escribe un numero que sea entero")##pido un numero
        longitud = input("escribe la longitud que va a tener la comtraseña ")##le pido que me de la lomgitus que va atener el programa
    longitud = int(longitud)#guardo la longitud

    mayus = input("¿quieres agregar masyuculas? (s/n): ").lower() == 's'##pregunto si quiere agregar mayusculas
    minuscu = input("¿quieres agregar minusculas? (s/n): ").lower() == 's'##pregunto si quiere agregar minusculas
    numeros = input("¿quieres agregar numeros? (s/n): ").lower() == 's'##pregunto si quiere agregar numeros

    return longitud, mayus, minuscu, numeros##me devuelvo a 

def copo():##defino la funcion copo


    print("hola bienvenido")##saludo al usuario
    print("espero que estes bien")
    print("en este programa puedes crear contraseñas a tu gusto ")

    hola=True##defino hola como verdadero

    while hola:##mientras hola sea igual a verdadero entonces
        longitud, mayus, minuscu, numeros = preferen()
        contrasena = cometa(longitud, mayus, minuscu, numeros )

        if contrasena:##si es contraseña entonces
            print("tu contraseña creada es ", contrasena)

        else:##si no entonces escribo
            print("hubo un error al crear la contraseña escribela de nuevo ")

        geneDiferent = input("¿quieres crear una contraseña nuevamente? (s/n): ").lower()##opcion de crear contraseña otra vez
        if geneDiferent != 's':
            print("adios,espero que pases un buen dia ")

            break##si no finalizo


if __name__ == "__main__":##añado la construccion de script
    copo()


   ##realizado por jean franco guerrero acero
