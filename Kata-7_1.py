planets = []
newplanet = ''
while newplanet.lower() != "Fin":
    if newplanet:
        planets.append(newplanet)
    newplanet = input("Ingresa el nombre del planeta:")