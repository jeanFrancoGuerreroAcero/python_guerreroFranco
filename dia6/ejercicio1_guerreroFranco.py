print("escribe los numero con espacios")
number=input().split()##creo la lista

fran=len(number)##pongo el len para que me devuelva la lista


jjj=list(set(number))##list para que me lo muestre en lista, y set para que me elimine los duplicados

jjj.sort()##para que me lo muestre de forma ordenada
print(jjj)##inprimo la lista de forma ordenada