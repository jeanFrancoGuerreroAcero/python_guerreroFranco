import json

with open("large-file.json", "r",encoding="utf-8") as f:
    content= json.loads(f.read())

menu=f"""
################
que opcion escoges 

1- crear un evento
2-eliminar un evento
3-actulizar un evento
4-mostar eventos con id


"""
print(menu)
opcion=input()
odio=True
event={eventos ["id"] for eventos in content}


while odio:
    if opcion== "1":
        print("####################")
        print("crear evento")
        print("####################")
        id_evento = input("ingresa el id que pondras al evento")

        if id_evento in event:
            print("este evento ya esta creado")
        else:
            nombre= input("que nombre le pondras al evento")
            nuevo_event= {"type":nombre,"id":id_evento}
            content.append(nuevo_event)
            event.add(nombre)
            print("se añadio el evento")  

    elif opcion=="2":
        print("####################")
        print("eliminar evento")
        print("####################")
        print("")
        print("que evento desea eliminar")
        idelimi=input("ingrese el id del type que desea eliminar")
        
        for actor in content["id"]:
            if idelimi in content:
                otro= {"id":idelimi}
                otro.clear()
                print("se ha eliminado este evento")

    elif opcion=="3":
        if content:
            id_actu = input("dame el id del evento que deseas actualizar")
            for event in content:
                if event["id"]== id_actu:
                    print("evento actualizado")
                else:
                    print("no es existe este evento")

    elif opcion=="4":
        if content:
            print("####################")
            print("eventos")
            print("####################")
            for i,eventos in enumerate (content, 1):
                print(f"{i}. {eventos["type"]} - {eventos["id"]}" )
        else:
            print("no hay eventos para mostar")

##codigo por mejorar
##realizado por jean franco guerrero acero -1093909111