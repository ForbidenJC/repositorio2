frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"dalto tardaria {cantidad_de_palabras/2 - cantidad_de_palabras/2*0.30 } segundos en decirlo")
if cantidad_de_palabras>10:
    print("mucho texto")



