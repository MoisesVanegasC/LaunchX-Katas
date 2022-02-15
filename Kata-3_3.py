VelAs=int(input("Ingresa la velocidad del asteroide: "))
TamAs=int(input("Ingresa el tamaño del asteroide: "))

if(VelAs>25) and (TamAs>=25):
    print("ADVERTENCIA: Asteroide se acerca a la Tierra a una alta velocidad y de dimensiones grandes TOMAR PRECAUCIONES.")
    if(VelAs>=20):
        print("El asteroide entrante generara rayos de Luz.")
elif(VelAs<20) and (TamAs<25):
    print("El asteroide se acerca a la Tierra y no generara rayos de Luz.")
    print("El asteroide no genera niguna alerta para la Tierra.")
elif(VelAs<20) and (TamAs>25):
    print("ALERTA: El asteroide entrante genera un peligro para la Tierra TOMAR PRECAUCIONES.")
    print("El asteroide se acerca a la Tierra y no generara rayos de Luz.")