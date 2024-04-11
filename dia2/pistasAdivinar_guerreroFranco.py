def adivi_num():
    print("hola como esta")
    print("acabo de escribir un numero en un papel")
    print("pero ahora va a ser mas dificil")
    print("los intentos van a ser limitados")
    
    num_secret = random.randint(0, 100)
    intents = 0
    maxIntents = 10

    while intents < maxIntents:
        intents_restan = maxIntents - intents
        print(f"Te quedan: {intents_restan}")
        
        try:
            sposici= int(input("dame un numero (entre 0 y 100): "))
        except ValueError:
            print("noooo este numero no ea valido")
            continue

        if sposici < 0 or sposici > 100:
            print("el numero que piensas debe estar entre el 0 y el 100,ingresa de nuevo")
            continue
        
        intents += 1

        if sposici < num_secret:
            print("noo estas muy lejos")
        elif sposici > num_secret:
            print("nooo te pasate pero estas cerca")
        else:
            print(f"uyyyy adivinaste cual era el numero que estaba escrito({num_secret}) en {intents} intentos.")
            break
    else:
        print(f"el numero que estaba escrito en el papel {num_secret} a la proxima sera no te desesperes")
        

if __name__ == "__main__":
    adivi_num()