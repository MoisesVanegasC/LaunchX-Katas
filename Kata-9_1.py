def informe(tanke_prin, tanke_ext, tanke_hidro):
    prom=(tanke_prin+tanke_ext+tanke_hidro)/3
    return f"""Informe de Combustible:
    Promedio: {prom}%
    Tanque Principal: {tanke_prin}%
    Tanque Externo: {tanke_ext}%
    Tanque de Hidrogeno: {tanke_hidro}%
    """
print(informe(90,50,65))

def promedio(valores):
    total = sum(valores)
    numero = len(valores)
    return total / numero

promedio([60, 45, 62])

def informe(tanke_prin, tanke_ext, tanke_hidro):    
    return f"""Informe de combustible:
    Promedio: {promedio([tanke_prin,tanke_ext,tanke_hidro])}%
    Tanque Principal: {tanke_prin}%
    Tanque Externo: {tanke_ext}%
    Tanque de Hidrogeno: {tanke_hidro}%
    """

print(informe(90, 50, 65))