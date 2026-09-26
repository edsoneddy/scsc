def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            return anio % 400 == 0
        else:
            return True
    else:
        return False

anio = int(input())

if es_bisiesto(anio):
    print("si")
else:
    print("no")
