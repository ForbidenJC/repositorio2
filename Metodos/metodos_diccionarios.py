#keys() devuelve las claves / tambien sirve para iterar
#get() devuelve el valor de una clave
#clear() elimina todos los elementos 
#pop() elimina un elemento 
#items() para iterar el dict

diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs" : 1000000
}

claves = diccionario.keys()

valor_elemento = diccionario.get("nombre")

print(valor_elemento)

diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
 
