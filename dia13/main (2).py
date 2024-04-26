#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('dia13/info (1).json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("dia13/info (1).json","w") as outfile:
        json.dump(miData,outfile)

def eliminarArchivo(miData,grupo):
    with open("dia13/info (1).json","w") as outfile:
        json.dump(miData,outfile)


print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
voleybol=True

while voleybol :
    queGrupo=input("que grupo desea hacer la gestion t2/p1 :")
    if queGrupo=="t2":
        print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.eliminar datos\n4.crear nuevo estudiante\n5.salir del programa")
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

            if(datoCambiar==4):##si escoge la opcion 4 va a cambiar la cedula
                nuevaCedula= input("ingrese la nnueva cedula que tendra :")
                miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
                guardarArchivo(miInfo)
                print("se ha relizado el cambio")
                contador=0

            if(datoCambiar==5):##si escoge la opcion 5 va a cambiar el email
                nuevoEmail= input("ingrese el nuevo email :")
                miInfo[0]["estudiantes"][estudiante-1]["email"]=nuevoEmail
                guardarArchivo(miInfo)
                print("se ha realizado el cambio")
                print("")
                contador=0

            if(datoCambiar==6):##si escoge la opcion 6 cambiara el git
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

        elif (x==3):##eliminar un estudiante
            miInfo=abrirArchivo()
            estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
            miInfo["estudiantes"].remove(estudiante)
            print("se ha eliminado el estudiante")
            guardarArchivo()

        elif (x==4):##crear u nuevo estudiante

            miInfo=abrirArchivo()

            crearEstudiante={}
            crearEstudiante["id"]=len (miInfo[0]["estudiantes"])+1
            print("los parametros a crear son\n")
            crearEstudiante["nombre"]=input("ingrese el nuevo nombre :")
            crearEstudiante["apellido"]=input("ingrese el nuevo apellido :")
            crearEstudiante["edad"]=input("ingrese la edad :")
            crearEstudiante["fechaNacimiento"]=input("ingrese la edad de nacimiento :")
            crearEstudiante["cedula"]=input("ingrese la cedula :")
            crearEstudiante["email"]=input("ingrese el email :")
            crearEstudiante["github"]=input("ingrese el github :")

            miInfo[0]["estudiantes"].append(crearEstudiante)
            guardarArchivo(miInfo)
            print("")
            print("se creo el nuevo estudiante")

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
            estudiante = int(input("Cual numero de identificacion vas a cambiar?"))
            miInfo["estudiantes"].remove(estudiante)
            print("se ha eliminado el estudiante")
            guardarArchivo()


        elif (x==4):
            miInfo=abrirArchivo()

            crearEstudiante={}
            crearEstudiante["id"]=len (miInfo[1]["estudiantes"])+1
            print("los parametros a crear son\n")
            crearEstudiante["nombre"]=input("ingrese el nuevo nombre :")
            crearEstudiante["apellido"]=input("ingrese el nuevo apellido :")
            crearEstudiante["edad"]=input("ingrese la edad :")
            crearEstudiante["fechaNacimiento"]=input("ingrese la edad de nacimiento :")
            crearEstudiante["cedula"]=input("ingrese la cedula :")
            crearEstudiante["email"]=input("ingrese el email :")
            crearEstudiante["github"]=input("ingrese el github :")

            miInfo[1]["estudiantes"].append(crearEstudiante)
            guardarArchivo(miInfo)
            print("")
            print("se creo el nuevo estudiante")

        elif(x==5):
            print("hasta luego")
            voleybol=False
            exit()
         
##realizado por jean franco guerrero acero -1093909111
                            
                            
                    



