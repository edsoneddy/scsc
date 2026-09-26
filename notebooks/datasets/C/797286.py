dato = int(input())

if (1800<=dato<=9999):
    if(dato%400==0):
        print("si")
    elif(dato%100==0):
        print("no")
    elif(dato%4==0):
        print("si")
    else:
        print("no")