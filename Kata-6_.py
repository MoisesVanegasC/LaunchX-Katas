planets = ['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Uranio','Neptuno']

print("El primer planeta es:",planets[0])
print("El segundo planeta es:",planets[1])
print("El tercer planeta es:",planets[2])
print("El cuarto planeta es:",planets[3])

planets[3] = "Planeta Rojo"
print("Marte es conocido tambien como: ",planets[3])

np = len(planets)
print("Hay", np, "planetas en el sistema solar.")

planets.append("Pluto")
np = len(planets)
print("Hay", np, "planetas en el sistema solar.")

planets.pop()
np = len(planets)
print("No, definitivamente hay", np, "planetas en el sistema solar.")

print("El ultimo planeta es:", planets[-1])
print("El penultimo planeta es:", planets[-2])

jupiterid=planets.index("Jupiter")
print("Jupiter es el", jupiterid+1,"planeta desde el Sol.")

gravedadT = 1.0
gravedadL = 0.166
gravedadP= [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

pesobus=12650 #KG
print("En la Tierra, un autobus de dos pisos pesa",pesobus,"kg")
print("En Mercurio, un autobus de dos pisos pesa",pesobus*gravedadP[0],"kg")