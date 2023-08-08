#creando una lista se puede modificar
lista = ["Juan Carlos Reyes", "forbidenjc", True, 1.85]
#creando una tupla no se puede modificar
tupla = ("Juan Carlos Reyes", "forbidenjc", True, 1.85)


lista[3] ="Maquinola"

#print(lista[3])

#creando un conjunto (set)
conjunto = {"Juan Reyes", "forbidenjc", True, 1.85} #conjunto no puede haber datos duplicados, no se accede a elementos por indices. 
#print(conjunto) 

#creando un diccionario dict

diccionario = {
    'nombre' : "juan reyes", 
    'canal' : "forbidenjc" , 
    'emocionado' : True , 
    'altura' : 1.85 , 
    'duplicado' : "forbidenjc"
}

print(diccionario["altura"])

