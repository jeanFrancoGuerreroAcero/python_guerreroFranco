def twoSum(target,nums):##creo ka funcion
    for i in range(len(nums)):##creo el bucle desde i hasta los numeros
        for j in range(i+1, len(nums)):##creo un bucle j y lo pongo un posicion mas adelante que el i
            if (nums[i] + nums [j]==target):##si los nums de la posicion 1 mas los nums de la posicion 2 son iguales a target entonces
                print(i,j)##imprimo para que me muestre la posicion 1 y 2
            
nums= [2, 4, 3]##parametros que estan dentro de la lista que al sumarlos me den el objetivo
target= 6##objetivo a llegar
twoSum(target,nums)##llamo la funcion