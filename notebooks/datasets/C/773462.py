def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return "si"
            else:
                return "no"
        else:
            return "si"
    else:
        return "no"

año = int(input())
resultado = es_bisiesto(año)
print(resultado)