planets = []
newplanet = ''
while newplanet.lower() != "hecho":
    if newplanet:
        planets.append(newplanet)
    newplanet = input("Ingresa el nombre del planeta:")
for planet in planets:
    print(planet)