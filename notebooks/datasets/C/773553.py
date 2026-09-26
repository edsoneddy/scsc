def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "si"
    return "no"

year = int(input())
print(es_bisiesto(year))