planeta = {
    'nombre' : 'Marte',
    'lunas' : 2
}
print(planeta['nombre'],"tiene", planeta['lunas'],"lunas")

planeta['circunferencia (km)'] = {
    'polar': 6752,
    'ecuatorial': 6792
}

print(planeta['nombre'],"tiene la circunferencia polar de", planeta['circunferencia (km)']['polar'], "km")