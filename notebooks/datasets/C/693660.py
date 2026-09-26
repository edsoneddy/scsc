anio = int(input())

if anio % 4 == 0:
    if anio % 100 != 0:
        print ("si")
    else:
        if anio % 400 == 0:
            print ("si")
        else:
            print ("no")
else:
    print("no")