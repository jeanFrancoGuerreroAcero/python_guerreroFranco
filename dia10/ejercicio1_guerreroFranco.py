def targ(nums, target):##creo la funcion targ 
    anterior, despues = 0, len(nums) - 1##antes y despues los asigno en 0 para que al pasar por nums 
    while anterior <= despues:##mientras anterior sea menor o igual a despues 
        entre = (despues + anterior) // 2##entonces entre es la suma de anterior con despues dividido entre 2
        if nums[entre] < target:##si entre en la lista nums es menor al objetivo
            anterior = entre + 1##entonces anterior se le suma 1 con la variable entre
        if nums[entre] > target:##si entre en la lista es mayor a el objetivo
            despues = entre - 1##entonces en la variable despues se le restaria 1 a la variable entre
        else:##si no
            return entre##vuelv a entre
    return anterior##vvuelvo a anterior
nums=[1,3,5,6]##creo la lista 
print(nums)##muestro la lista al usuario
target=len(input("objetivo: "))##le pido al usuario que ingrese el objetivo
print(targ(nums,target))
##realizado por jean franco guerrero acero