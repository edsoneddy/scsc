def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    elif (year % 400 == 0):
        return True
    else:
        return False

year = int(input())

if es_bisiesto(year):
    print("si")
else:
    print("no")