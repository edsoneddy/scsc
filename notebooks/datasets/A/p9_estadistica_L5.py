import math

# Lee los numeros de una linea y los devuelve como lista de floats
def leer_datos():
    partes = input().split()
    return list(map(float, partes))

# Calcula la mediana de una lista ya ordenada
def mediana(ordenados):
    medio = len(ordenados) // 2
    n = len(ordenados)
    if n % 2 == 1:
        return ordenados[medio]
    return (ordenados[medio - 1] + ordenados[medio]) / 2

datos = leer_datos()
if len(datos) == 0:
    print("No hay datos")
else:
    n = len(datos)
    ordenados = sorted(datos)
    media = sum(datos) / n
    # Cuenta las repeticiones para hallar la moda
    conteo = {}
    for x in datos:
        conteo[x] = conteo.get(x, 0) + 1
    mayor = max(conteo.values())
    modas = []
    for x in ordenados:
        if conteo[x] == mayor and x not in modas:
            modas.append(x)
    # Desviacion estandar poblacional
    suma_cuad = 0
    indice = 0
    while indice < len(datos):
        suma_cuad = suma_cuad + (datos[indice] - media) ** 2
        indice += 1
    desv = math.sqrt(suma_cuad / n)
    print("Media: %.2f" % media)
    print("Mediana: %.2f" % mediana(ordenados))
    print("Moda:", modas)
    print("Desviacion: %.2f" % desv)
    print("Rango:", ordenados[-1] - ordenados[0])
