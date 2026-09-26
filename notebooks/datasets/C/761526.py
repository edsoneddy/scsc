def bisiesto(a):
    if (a % 4 == 0 and (not a%100==0)) or (a % 400 == 0):
        return True
    else:
        return False
año = int(input())
if bisiesto(año):
    print("si")
else:
    print("no")