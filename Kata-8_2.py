planet_luna = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
lunas = planet_luna.values()
planets = len(planet_luna.keys())
tot_lun = 0
for lunas in lunas:
    tot_lun = tot_lun + lunas
    
prom = tot_lun / planets
print("El promedio es:",prom)