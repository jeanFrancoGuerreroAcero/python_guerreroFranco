import collections

print("bienveniso a la fruteria")
frutas = {'manzana':[0.45, 10],'pera':[0.30, 20],'uvas': [0.55, 9]}##creo el diccionario

mayus = {fruta.upper(): info for fruta, info in frutas.items()}##cambio a mayuscula el diccionario
print(mayus)

##inprimo las frutas que tengan un valor menor a 0.50
print("Frutas con precio inferior a 0.50:")
for fruta, (precio, cantidad) in frutas.items():
    if precio < 0.50:
        print(fruta)


hola=collections.orderedDict(sorted(cantidad.items()))##inprimo la lista de forma ascendente de acuerdo a la cantidad
print(hola)

frutas_ordenadas = sorted(frutas.items(), key=lambda x: x[1][0] * x[1][1], reverse=True)##imprimo de forma descendente de acuerdo a la cantidad y el precio

##realizado por jean franco guerrero acero --1093909111