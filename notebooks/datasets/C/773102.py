def es_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return "si"
    else:
        return "no"

anio = int(input())
print(es_bisiesto(anio))