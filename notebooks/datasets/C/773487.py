anio = int(input())
if 1800 <= anio <= 9999:
    if anio % 4 == 0 and anio % 100 != 0 or anio % 100 ==0 and anio % 400 == 0:
        print("si")
    else:
        print("no")