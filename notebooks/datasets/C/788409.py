# Leer el año
year = int(input().strip())

# Verificar si es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("si")
else:
    print("no")
