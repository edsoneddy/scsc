import math

# Lectura: una linea de numeros -> lista de floats
def leer_datos():
  partes = input().split()
  return [float(p) for p in partes]

# Mediana (la lista debe llegar ordenada)
def mediana(ordenados):
  n = len(ordenados)
  medio = n // 2
  if n % 2 == 1:
    return ordenados[medio]
  return (ordenados[medio-1] + ordenados[medio]) / 2


datos = leer_datos()
if len(datos) == 0:
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
    if conteo[x] == mayor and x not in modas:
      modas.append(x)
  # Desviacion estandar poblacional (divide entre n)
  suma_cuad = 0
  for x in datos:
    suma_cuad += (x-media)**2
  desv = math.sqrt(suma_cuad / n)
  print("Media: %.2f" % media)
  print("Mediana: %.2f" %
    mediana(ordenados))
  print("Moda:", modas)
  print("Desviacion: %.2f" % desv)
  print("Rango:", ordenados[-1]-ordenados[0])
