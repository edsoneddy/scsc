año = int(input())

es_bisiesto = False

if año % 4 == 0:
    es_bisiesto = True
    if año % 100 == 0:
        es_bisiesto = False
        if año % 400 == 0:
            es_bisiesto = True

if es_bisiesto:
    print("si")
else:
    print("no")
