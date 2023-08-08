#numero=input("ingresa el numero: ")

def narcissistic(value):
    # Convertimos el número en una cadena para obtener la cantidad de dígitos (expo)
    expo = len(str(value))
    # Convertimos el número en una lista de dígitos como cadenas
    numarray = list(str(value))
    
    # Inicializamos el exponente y la suma a 0
    exponente, suma = 0, 0
    
    for i in range(len(numarray)):
        # Convertimos cada dígito de vuelta a número y elevamos a la potencia expo
        exponente = int(numarray[i]) ** expo
        # Acumulamos la suma de las potencias de los dígitos
        suma += exponente
    
    # Comprobamos si la suma de las potencias es igual al número original
    if suma == value:
        return True
    else:
        return False

# Prueba de la función con un valor
print(narcissistic(7))  # Output: True
