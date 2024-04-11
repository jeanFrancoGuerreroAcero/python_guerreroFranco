#-------------------------------
#----DIA 1 CHEAT SHEET PYTHON-----
#-------------------------------

def adivi_num():
 print("hola bienvenido")
 print("juguemos a adivinar el numero que esta escrito en el papel")
 print("el numero esta entre 0 y 100")



 num_secret= random.randit(0, 100)
 intents= 0

while True:
    try:
            azar= int(input("escribe que numero creees que es "))
    except ValueError:
            print("este numero no esta dentros de las pisbilidades del que esta en  el papel")
            continue

    if azar < 0 or azar > 100:
            print("noooo, el numero debe estar entre 0 y 100")
            continue

    intents= intents+1

    if azar < num_secret:
         print("nooo te estas equivocando y estas lejos de el numero")
    if azar < num_secret:
         print("noo no le atinaste")
    elif azar > num_secret:
         print("sigue intentando te pasate")
    else:
      print(f"uyyy felicitaciones,adivinaste el numero que estaba escrito en el papel")
      print("el numero que estaba escrito en el papel era ({num_secret}) en {intenst} intentos")
           
    break

if __name__ == "__main__":
    adivi_num()
