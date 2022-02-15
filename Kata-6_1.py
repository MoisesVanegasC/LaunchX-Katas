planets = ['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Uranio','Neptuno']

print("El primer planeta es:",planets[0])
print("El segundo planeta es:",planets[1])
print("El tercer planeta es:",planets[2])
print("El cuarto planeta es:",planets[3])
print("El quinto planeta es:",planets[4])
print("El sexto planeta es:",planets[5])
print("El septimo planeta es:",planets[6])
print("El octavo planeta es:",planets[7])

planets.append("Pluton")
np=len(planets)
print("En nuestro sistema solar hay",np)
print("El ultimo planeta es:",planets[-1])