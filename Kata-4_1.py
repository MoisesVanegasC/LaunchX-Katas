tex = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest The highest daylight temperature of the Moon is 127 C."""
texD = tex.split('. ')
texD
palcl = ['average', 'temperature', 'distance']

for oracion in texD:
    for letras in palcl:
        if letras in oracion:
            print(oracion)
            break
        
for oracion in texD:
    for letras in palcl:
        if letras in oracion:
            print(oracion.replace(' C', ' Celsius'))
            break