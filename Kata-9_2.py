def informe_mision(hora_pre, tiempo_vuelo, destino,tanke_ext, tanke_prin):
    return f""" Mision a {destino}
    Tiempo de vuelo: {hora_pre + tiempo_vuelo} minutos
    Combustible total restante: {tanke_prin + tanke_ext} galones
    """
print(informe_mision(17, 40, "Luna", 150000, 200000))

def informe_mision(destino, *minutos ,**comb_reservas):
    return f""" Mision a {destino}
    Tiempo de vuelo: {sum(minutos)} minutos
    Combustible total restante: {sum(comb_reservas.values())} galones
    """
print(informe_mision("Luna", 17, 40, main=200000, ext=150000))

def informe_mision(destino, *minutos, **comb_reservas):
    informe_prin = f"""
    Mision a {destino}
    Tiempo de vuelo: {sum(minutos)} minutos
    Combustible total restante: {sum(comb_reservas.values())}
    """
    for tank_nombre, galones in comb_reservas.items():
        informe_prin += f"{tank_nombre} tanque --> {galones} galones restantes\n"
    return informe_prin

print(informe_mision("Luna", 17, 40, principal=200000, externo=150000))