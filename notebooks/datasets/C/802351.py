n = int(input())
if 1800 <= n <= 9999:
    es_bisiesto = (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)
    if es_bisiesto:
        print("si")
    else:
        print("no")