import math

# Lee los numeros de una linea y los devuelve como lista de floats
def cargar_numeros():
    trozos = input().split()
    return [float(t) for t in trozos]

# Calcula la mediana de una lista ya ordenada
def calcular_mediana(lista_ord):
    cant = len(lista_ord)
    mitad = cant // 2
    if cant % 2 == 1:
        return lista_ord[mitad]
    return (lista_ord[mitad - 1] + lista_ord[mitad]) / 2

valores = cargar_numeros()
if len(valores) == 0:
    print("No hay datos")
else:
    cant = len(valores)
    promedio = sum(valores) / cant
    lista_ord = sorted(valores)
    # Cuenta las repeticiones para hallar la moda
    frecs = {}
    for v in valores:
        frecs[v] = frecs.get(v, 0) + 1
    maxfrec = max(frecs.values())
    lista_modas = []
    for v in lista_ord:
        if frecs[v] == maxfrec and v not in lista_modas:
            lista_modas.append(v)
    # Desviacion estandar poblacional
    acum = 0
    for v in valores:
        acum += (v - promedio) ** 2
    sigma = math.sqrt(acum / cant)
    print("Media: %.2f" % promedio)
    print("Mediana: %.2f" % calcular_mediana(lista_ord))
    print("Moda:", lista_modas)
    print("Desviacion: %.2f" % sigma)
    print("Rango:", lista_ord[-1] - lista_ord[0])
