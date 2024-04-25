import json

with open('python_guerreroFranco/python_guerreroFranco/dia12/large-file.json', encoding= "utf-8") as openfile:
    miJSON= json.load(openfile)

#print(type(miJSON))
'''
for i in range (5):
  print(miJSON[i])
'''
crearEventos=[]
PullRequestEvent=[]
PushEvent=[]
IssueCommentEvent=[]
opened=[]
IssuesEvent=[]
ReleaseEvent=[]
WatchEvent=[]
CommitCommentEvent=[]
GollumEvent=[]
MemberEvents=[]
PullRequestReviewCommentEvent=[]
DeleteEvent=[]
nombre=[]

nuevoEvento=[]

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=="PullRequestEvent"):
        PullRequestEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=="PushEvent"):
        PushEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=="WatchEvent"):
        WatchEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=="IssueCommentEvent"):
        IssueCommentEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=="IssuesEvent"):
        IssuesEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=="ReleaseEvent"):
        ReleaseEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='PullRequestReviewCommentEvent'):
        PullRequestReviewCommentEvent.append(miJSON[i])
        
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CommitCommentEvent'):##
        CommitCommentEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='MemberEvents'):
        MemberEvents.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='GollumEvent'):
        GollumEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='DeleteEvent'):
        DeleteEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='DeleteEvent'):
        DeleteEvent.append(miJSON[i])

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='DeleteEvent'):
        DeleteEvent.append(miJSON[i])


#print(crearEventos[5]['actor']['id'])

with open("eventos_createEvent.json","w") as outfile:
    json.dump(crearEventos,outfile)

with open("eventos_PullRequestEvent.json","w") as outfile:
    json.dump(PullRequestEvent,outfile)

with open("eventos_PushEvent.json","w") as outfile:
    json.dump(PushEvent,outfile)

with open("eventos_WatchEvent.json","w") as outfile:
    json.dump(WatchEvent,outfile)

with open("eventos_IssueCommentEvent.json","w") as outfile:
    json.dump(IssueCommentEvent,outfile)

with open("eventos_IssuesEvent.json","w") as outfile:
    json.dump(IssuesEvent,outfile)

with open("eventos_ReleaseEvent.json","w") as outfile:
    json.dump(ReleaseEvent,outfile)

with open("eventos_PullRequestReviewCommentEvent.json","w") as outfile:
    json.dump(PullRequestReviewCommentEvent,outfile)

with open("eventos_CommitCommentEvent.json","w") as outfile:
    json.dump(CommitCommentEvent,outfile)

with open("eventos_MemberEvents.json","w") as outfile:
    json.dump(MemberEvents,outfile)


menu= f"""

1-crear un nuevo evento
2-actualizar in evento
3-eliminar evento

"""
print(menu)
opcio=input("que opcion desea realizar : ")
star=True

while star :
    if opcio=="1":
        for i in crearEventos:
            print("#######################")
            print("#### crear evento #####")
            print("#######################")
            print("")
            tipoEvento=input("que tipo de evento quiere crear : ")

            if tipoEvento == "CreateEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (24):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ",crearEventos[q]['id'])
                    print("Tipo:",crearEventos[q]['type'])
                    print("Actor:")
                    print("------- ID:",crearEventos[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_createEvent.json":
                     "CreateEvent".append("eventos_createEvent.json"[i])
                     nombre.append("eventos_createEvent.json"[i])
                     nombre.append("eventos_createEvent.json"[i])
                     nombre.append("eventos_createEvent.json"[i])
             ##evento 2        
            if tipoEvento == "PullRequestEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (29):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ", PullRequestEvent[q]['id'])
                    print("Tipo:", PullRequestEvent[q]['type'])
                    print("Actor:")
                    print("------- ID:", PullRequestEvent[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_PullRequestEvent.json":
                     "PullRequestEvent".append("eventos_PullRequestEvent.json"[i])
                     nombre.append("eventos_PullRequestEvent.json"[i])
                     nombre.append("eventos_PullRequestEvent.json"[i])
                     nombre.append("eventos_PullRequestEvent.json"[i])

            #"tipo 3
            if tipoEvento == "PushEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (22):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ",PushEvent[q]['id'])
                    print("Tipo:",PushEvent[q]['type'])
                    print("Actor:")
                    print("------- ID:",PushEvent[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_PushEvent.json":
                     "PushEvent".append("eventos_PushEvent.json"[i])
                     nombre.append("eventos_PushEvent.json"[i])
                     nombre.append("eventos_PushEvent.json"[i])
                     nombre.append("eventos_PushEvent.json"[i])
            ##tipo 4
            if tipoEvento == "WatchEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (23):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ",WatchEvent[q]['id'])
                    print("Tipo:",WatchEvent[q]['type'])
                    print("Actor:")
                    print("------- ID:",WatchEvent[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_WatchEvent.json":
                     "WatchEvent".append("eventos_WatchEvent.json"[i])
                     nombre.append("eventos_WatchEvent.json"[i])
                     nombre.append("eventos_WatchEvent.json"[i])
                     nombre.append("WatchEvent.json"[i])
            ##tipo 5
            if tipoEvento == "IssueCommentEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (30):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ",IssueCommentEvent[q]['id'])
                    print("Tipo:",IssueCommentEvent[q]['type'])
                    print("Actor:")
                    print("------- ID:",IssueCommentEvent[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_createEvent.json":
                     "IssueCommentEvent".append("eventos_IssueCommentEvent.json"[i])
                     nombre.append("eventos_IssueCommentEvent.json"[i])
                     nombre.append("eventos_IssueCommentEvent.json"[i])
                     nombre.append("eventos_IssueCommentEvent.json"[i])
            ##tipo 6
            if tipoEvento == "IssuesEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (24):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ",IssuesEvent[q]['id'])
                    print("Tipo:",IssuesEvent[q]['type'])
                    print("Actor:")
                    print("------- ID:",IssuesEvent[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_IssuesEvent.json":
                     "IssuesEvent".append("eventos_IssuesEvent.json"[i])
                     nombre.append("eventos_IssuesEvent.json"[i])
                     nombre.append("eventos_IssuesEvent.json"[i])
                     nombre.append("eventos_IssuesEvent.json"[i])
            ##tipo 7
            if tipoEvento == "ReleaseEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                 for q in range (25):
                    print("#######################")
                    print("#### Evento # ",q+1 ,"##")
                    print("#######################")
                    print("ID: ",ReleaseEvent[q]['id'])
                    print("Tipo:",ReleaseEvent[q]['type'])
                    print("Actor:")
                    print("------- ID:",ReleaseEvent[q]['actor']['id'])
                    print("#######################")
                    print("#######################")
                    print("")
                id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                print("##############################")
                nombre=input("\nque nombre le pondra al evento :")
                login=input("ingrese el login del evento :")
                avatar=input("ingrese el avatar_url :")
                print("##############################")
                id_repo=input("ingrese el id que le dara al repositorio :")
                nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                public=input("el public desea que sea true o false :")

                for i in "eventos_ReleaseEvent.json":
                     "ReleaseEvent".append("eventos_createEvent.json"[i])
                     nombre.append("eventos_ReleaseEvent.json"[i])
                     nombre.append("eventos_ReleaseEvent.json"[i])
                     nombre.append("eventos_ReleaseEvent.json"[i])
            ##tipo 8

            if tipoEvento == "PullRequestReviewCommentEvent":
                quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                if quiere == "si":
                    for q in range (42):
                        print("#######################")
                        print("#### Evento # ",q+1 ,"##")
                        print("#######################")
                        print("ID: ",PullRequestReviewCommentEvent[q]['id'])
                        print("Tipo:",PullRequestReviewCommentEvent[q]['type'])
                        print("Actor:")
                        print("------- ID:",PullRequestReviewCommentEvent[q]['actor']['id'])
                        print("#######################")
                        print("#######################")
                        print("")
                    id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                    print("##############################")
                    nombre=input("\nque nombre le pondra al evento :")
                    login=input("ingrese el login del evento :")
                    avatar=input("ingrese el avatar_url :")
                    print("##############################")
                    id_repo=input("ingrese el id que le dara al repositorio :")
                    nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                    public=input("el public desea que sea true o false :")

                    for i in "eventos_PullRequestReviewCommentEvent.json":
                            "PullRequestReviewCommentEvent".append("eventos_PullRequestReviewCommentEvent.json"[i])
                            nombre.append("eventos_PullRequestReviewCommentEvent.json"[i])
                            nombre.append("eventos_PullRequestReviewCommentEvent.json"[i])
                            nombre.append("eventos_PullRequestReviewCommentEvent.json"[i])

                    ##tipo 9    

                if tipoEvento == "CommitCommentEvent":
                    quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                    if quiere == "si":
                        for q in range (31):
                            print("#######################")
                            print("#### Evento # ",q+1 ,"##")
                            print("#######################")
                            print("ID: ",CommitCommentEvent[q]['id'])
                            print("Tipo:",CommitCommentEvent[q]['type'])
                            print("Actor:")
                            print("------- ID:",CommitCommentEvent[q]['actor']['id'])
                            print("#######################")
                            print("#######################")
                            print("")
                        id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                        print("##############################")
                        nombre=input("\nque nombre le pondra al evento :")
                        login=input("ingrese el login del evento :")
                        avatar=input("ingrese el avatar_url :")
                        print("##############################")
                        id_repo=input("ingrese el id que le dara al repositorio :")
                        nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                        public=input("el public desea que sea true o false :")

                        for i in "eventos_CommitCommentEvent.json":
                                "CommitCommentEvent".append("eventos_CommitCommentEvent.json"[i])
                                nombre.append("eventos_CommitCommentEvent.json"[i])
                                nombre.append("eventos_CommitCommentEventt.json"[i])
                                nombre.append("eventos_CommitCommentEvent.json"[i])
                                ##tipo 10

                if tipoEvento == "MemberEvents":
                    quiere=input("quieres ver todos los eventos de crearEventos si/no :")
                    if quiere == "si":
                        for q in range (25):
                            print("#######################")
                            print("#### Evento # ",q+1 ,"##")
                            print("#######################")
                            print("ID: ",MemberEvents[q]['id'])
                            print("Tipo:",MemberEvents[q]['type'])
                            print("Actor:")
                            print("------- ID:",MemberEvents[q]['actor']['id'])
                            print("#######################")
                            print("#######################")
                            print("")
                        id_crearEventos=input("ingrese el ID que le asignara al evento : ")
                        print("##############################")
                        nombre=input("\nque nombre le pondra al evento :")
                        login=input("ingrese el login del evento :")
                        avatar=input("ingrese el avatar_url :")
                        print("##############################")
                        id_repo=input("ingrese el id que le dara al repositorio :")
                        nombre_repo=input("ingrese el nombre que le dara al repositorio :")
                        public=input("el public desea que sea true o false :")

                        for i in "eventos_MemberEventst.json":
                                "MemberEvents".append("eventos_MemberEvents.json"[i])
                                nombre.append("eventos_MemberEvents.json"[i])
                                nombre.append("eventos_MemberEvents.json"[i])
                                nombre.append("eventos_MemberEvents.json"[i])

            elif opcio == "2":
                print("hola")

                ##realizado por jean franco guerrero acero -1093909111