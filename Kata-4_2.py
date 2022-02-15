planet = "Marte "
grave  = 0.00143
name = "Ganímedes"

title = f"Gravedad {name}"

plantilla = f"""{'*'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {grave * 1000} m/s2 """

union = f"""{title.title()} 
{plantilla} 
""" 
print(plantilla)

planeta = "Marte "
gravedad  = 0.00143
nombre = "Ganímedes"

print(plantilla)

unionN = """
Gravedad de: {name}
*************************************
Nombre del planeta: {planet}
Gravedad en {name}: {grave} m/s2
"""
print(unionN.format(name=name, planet=planet, grave=grave))