import math

# Lee los numeros de una linea y los devuelve como lista de floats
def leer_datos():
    partes = input().split()
    return [float(p) for p in partes]

# Calcula la mediana de una lista ya ordenada
def mediana(ordenados):
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (ordenados[medio - 1] + ordenados[medio]) / 2
    return ordenados[medio]

datos = leer_datos()
if len(datos) < 1:
    print("No hay datos")
else:
    n = len(datos)
    media = sum(datos) / n
    ordenados = sorted(datos)
    # Cuenta las repeticiones para hallar la moda
    conteo = {}
    for x in datos:
        conteo[x] = conteo.get(x, 0) + 1
    mayor = max(conteo.values())
    modas = []
    for x in ordenados:
        if not (conteo[x] != mayor or x in modas):
            modas.append(x)
    # Desviacion estandar poblacional
    suma_cuad = 0
    for x in datos:
        suma_cuad += (x - media) ** 2
    desv = math.sqrt(suma_cuad / n)
    print("Media: %.2f" % media)
    print("Mediana: %.2f" % mediana(ordenados))
    print("Moda:", modas)
    print("Desviacion: %.2f" % desv)
    print("Rango:", ordenados[len(ordenados) - 1] - ordenados[0])
