#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('python_guerreroFranco/python_guerreroFranco/dia13/info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("python_guerreroFranco/python_guerreroFranco/dia13/info.json","w") as outfile:
        json.dump(miData,outfile)


print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
voleybol=True

while voleybol :
    queGrupo=input("que grupo desea hacer la gestion t2/p1 :")
    if queGrupo=="t2":
        print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.eliminar datos\n4.crear nuevo estudiante")
        x=int(input("Cual opción escoges:"))
        miInfo=[]
        if(x==1):
            miInfo=abrirArchivo()
            for i in miInfo[0]["estudiantes"]:
                print("################")
                print("#### MOSTRAR LISTA DE USUARIOS ###")
                print("################")
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
        elif(x==2):
            miInfo=abrirArchivo()
            contador = 0
            for i in miInfo[0]["estudiantes"]:
                contador = contador +1
                print("################")
                print(" ESTUDIANTE #",contador)
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
            contador = 0
            estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
            datoCambiar=int(input("Que te gustaría cambiar del estudiante, escogue una opcion :\n1.Apellido: \n2.nombre: \n3.edad: \n4.cedula: \n5.email: \n6.GitHub:"))
            
            if (datoCambiar==1):
                nuevoApellido = input("Ingresa el nuevo apellido:")
                miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                guardarArchivo(miInfo)
                print("Cambio realizado!")
                contador = 0

            if (datoCambiar==2):
                nuevoNombre=input("ingrese el nuevo nombre que le pondra :")
                miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
                guardarArchivo(miInfo)
                print("Cambio realizado!")
                contador=0

            if(datoCambiar==3):
                nuevaEdad= input("ingrese la nueva edad que tendra :")
                miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
                guardarArchivo(miInfo)
                nuevaFecha= input("ingrese la nueva fecha de nacimiento que tendra :")
                miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFecha
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                contador=0

            if(datoCambiar==4):
                nuevaCedula= input("ingrese la nnueva cedula que tendra :")
                miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
                guardarArchivo(miInfo)
                print("se ha relizado el cambio")
                contador=0

            if(datoCambiar==5):
                nuevoEmail= input("ingrese el nuevo email :")
                miInfo[0]["estudiantes"][estudiante-1]["email"]=nuevoEmail
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                print("")
                contador=0

            if(datoCambiar==6):
                nuevoGit= input("ingrese el nuevo GitHub :")
                miInfo[0]["estudiantes"][estudiante-1]["GitHub"] = nuevoGit
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                contador=0

            miInfo=abrirArchivo()
            for i in miInfo[0]["estudiantes"]:
                contador = contador +1
                print("################")
                print(" ESTUDIANTE #",contador)
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
            contador = 0

        elif (x==4):
            miInfo=abrirArchivo()
            miInfo=print("los parametros a crear son\n")
            idNuevo=input("ingrese el nuevo id :")
            nombreCrear=input("ingrese el nombre del estudiante :")
            apellidoCrear=input("ingrese el apellido :")
            edadCrear=input("ingrese la edad :")
            fechaCrear=input("ingrese la fevha de naciminento :")
            cedulaCrear=input("ingrese la cedula :")
            emailCrear=input("ingrese el email :")
            githubCrear=input("ingrese el github :")

            libro={
                    "id": 3,
                    "grupo": "t2",
                    "estudiantes": [
                        {
                            "id": idNuevo,
                            "nombre": nombreCrear,
                            "apellido": apellidoCrear,
                            "edad": edadCrear,
                            "fechaNacimiento": fechaCrear,
                            "cedula": cedulaCrear,
                            "email": emailCrear,
                            "github": githubCrear
                        }
                    ]
                }
            miInfo[0]["estudiantes"][estudiante-1] = libro
            guardarArchivo(miInfo)
            print("usuario creado")
            print("")


    ##el grupo p1######################################################
    if queGrupo=="p1":
        print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.eliminar datos\n4.crear nuevo estudiante")
        x=int(input("Cual opción escoges:"))
        miInfo=[]
        if(x==1):
            miInfo=abrirArchivo()
            for i in miInfo[1]["estudiantes"]:
                print("################")
                print("#### MOSTRAR LISTA DE USUARIOS ###")
                print("################")
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
        elif(x==2):
            miInfo=abrirArchivo()
            contador = 0
            for i in miInfo[1]["estudiantes"]:
                contador = contador +1
                print("################")
                print(" ESTUDIANTE #",contador)
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
            contador = 0
            estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
            datoCambiar=int(input("Que te gustaría cambiar del estudiante, escogue una opcion :\n1.Apellido: \n2.nombre: \n3.edad: \n4.cedula: \n5.email: \n6.GitHub:"))
            
            if (datoCambiar==1):
                nuevoApellido = input("Ingresa el nuevo apellido:")
                miInfo[1]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
                guardarArchivo(miInfo)
                print("Cambio realizado!")
                contador = 0

            if (datoCambiar==2):
                nuevoNombre=input("ingrese el nuevo nombre que le pondra :")
                miInfo[1]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
                guardarArchivo(miInfo)
                print("Cambio realizado!")
                contador=0

            if(datoCambiar==3):
                nuevaEdad= input("ingrese la nueva edad que tendra :")
                miInfo[1]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
                guardarArchivo(miInfo)
                nuevaFecha= input("ingrese la nueva fecha de nacimiento que tendra :")
                miInfo[1]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFecha
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                contador=0

            if(datoCambiar==4):
                nuevaCedula= input("ingrese la nnueva cedula que tendra :")
                miInfo[1]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
                guardarArchivo(miInfo)
                print("se ha relizado el cambio")
                contador=0

            if(datoCambiar==5):
                nuevoEmail= input("ingrese el nuevo email :")
                miInfo[1]["estudiantes"][estudiante-1]["email"]=nuevoEmail
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                print("")
                contador=0

            if(datoCambiar==6):
                nuevoGit= input("ingrese el nuevo GitHub :")
                miInfo[1]["estudiantes"][estudiante-1]["GitHub"] = nuevoGit
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                contador=0

            miInfo=abrirArchivo()
            for i in miInfo[1]["estudiantes"]:
                contador = contador +1
                print("################")
                print(" ESTUDIANTE #",contador)
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
            contador = 0
         ##para borrar lo elementos del archivo########################################
         
        elif (x==3):
            miInfo=abrirArchivo()
            contador = 0
            for i in miInfo[1]["estudiantes"]:
                contador = contador +1
                print("################")
                print(" ESTUDIANTE #",contador)
                print("ID:",i["id"])
                print("Nombre:",i["nombre"])
                print("Apellido:",i["apellido"])
                print("Edad",i["edad"])
                print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
                print("Cédula:",i["cedula"])
                print("E-mail:",i["email"])
                print("GitHub:",i["github"])
                print("################")
                print("")
            contador = 0
            estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
            datoEliminar=int(input("Que te gustaría eliminar del estudiante, escogue una opcion :\n1.Apellido: \n2.nombre: \n3.edad: \n4.cedula: \n5.email: \n6.GitHub:"))
            if (datoEliminar==1):
                    borrarApellido = input("borrando apellido")
                    miInfo[1]["estudiantes"][estudiante-1]["apellido"] = borrarApellido
                    guardarArchivo(miInfo)
                    print("Cambio realizado!")
                    contador = 0
            voleybol=False
        elif (x==4):
            miInfo=abrirArchivo()
            miInfo=print("los parametros a crear son\n")
            idNuevo=input("ingrese el nuevo id :")
            nombreCrear=input("ingrese el nombre del estudiante :")
            apellidoCrear=input("ingrese el apellido :")
            edadCrear=input("ingrese la edad :")
            fechaCrear=input("ingrese la fecha de naciminento :")
            cedulaCrear=input("ingrese la cedula :")
            emailCrear=input("ingrese el email :")
            githubCrear=input("ingrese el github :")

            libro={
                        {
                            "id": idNuevo,
                            "nombre": nombreCrear,
                            "apellido": apellidoCrear,
                            "edad": edadCrear,
                            "fechaNacimiento": fechaCrear,
                            "cedula": cedulaCrear,
                            "email": emailCrear,
                            "github": githubCrear
                        }
                }
            miInfo[1]["estudiantes"][estudiante-1]["cedula"]  = miInfo
            guardarArchivo(miInfo)
            print("usuario creado")
            print("")   

##realizado por jean franco guerrero acero -1093909111
                            
                            
                    



