year =int(input())
if 1800<=year<=9999:
    def es_bisiesto(year):

        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            return True
        else:
            return False

    if es_bisiesto(year):
        print(f"si")
    else:
        print(f"no")