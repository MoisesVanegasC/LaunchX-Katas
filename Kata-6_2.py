planets = ['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Uranio','Neptuno']
planetaN = input("Dame el nombre del planeta:")
planetaS=planets.index(planetaN)
print("El planeta",planetaN, "es el", planetaS + 1 ,"planeta desde el Sol.")
print("Los planetas mas cercanos al sol desde:",planetaN,"son",planets[0:planetaS])
print("Los planetas mas lejanos al sol dessde:",planetaN,"son",planets[planetaS + 1:])