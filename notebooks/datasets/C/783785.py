def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input())
if es_bisiesto(año):
    print("si")
else:
    print("no")
