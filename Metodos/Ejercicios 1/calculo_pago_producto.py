
costoArt=float(input( "Ingrese el costo del articulo:"))
pago=float(input("Ingrese la Cantidad pagada:"))

if pago>costoArt:
    print("Su Cambio es: ",pago-costoArt)
elif pago == costoArt:
    print("Gracias por su compra")
elif pago<costoArt:
    print("aun debe: ",costoArt-pago)
    

    