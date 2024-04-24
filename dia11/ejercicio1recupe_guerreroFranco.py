import json

with open('dia11/large-file.json', encoding= "utf-8") as openfile:
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
    if(miJSON[i]['type']=="opened"):
        opened.append(miJSON[i])

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
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])
        
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])


#print(crearEventos[5]['actor']['id'])

for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])

with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)



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
            tipoEvento=input("que tipo de evento quiere crear")
            








        
