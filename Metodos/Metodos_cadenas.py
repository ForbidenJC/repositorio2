cadena1 = "hola soy juan carlos"
cadena2 = "bienvenido maquinola"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula solo la primera letra.
primer_letra_mayus = cadena1.capitalize()

print(primer_letra_mayus)

buscar_cadena = cadena1.find("carlos")

print(buscar_cadena)

contar_coincidencia = cadena1.count("la so")

print(contar_coincidencia)

contar_caracteres = len(cadena1)

print(contar_caracteres)

empieza_con = cadena1.startswith("h")

print(empieza_con)

termina_con = cadena1.endswith("los")

print(termina_con)

#reemplaza un pedazo de la cadena dada, por otra dada.

cadena_nueva = cadena1.replace("carlos", "pablo")

print(cadena_nueva)

#separar cadenas con la cadena que le pasemos 

cadena3 = "Hola,como,estas"

cadena_separada = cadena3.split(",")

print(cadena_separada)
