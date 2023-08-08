
#creando una lista con list()
lista = list(["hola", "Juan", 34, 56, 23, True])

#devuelve la cantidad de
cantidad_elementos = len(lista)

print(cantidad_elementos)

#agregando un elemento a la lista

lista.append("LOL")

#agregando un elemento a lista en un indice especifico
lista.insert(2, "dale vieja")

#agregando varios elementos a la lista, se tiene que anexar una lista
lista.extend([False, 2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(0) # -1 para eliminar el ultimo -2 para eliminar el ante ultimo y asi sucesivamente.

#removiendo un elemento de la lista por su valor
lista.remove(56)

#eliminando todos los elementos de la lista
#lista.clear()

#ordernar elementos de la lista, de forma ascendente si se agrega reverse=True invierte el orden de la lista.
lista2 = list([15,30,45,2, 19, 1])
lista2.sort()

#invirtiendo el elemento de una lista
lista2.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista2.index(2)


print(elemento_encontrado)





