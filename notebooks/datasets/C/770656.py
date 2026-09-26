numero = int(input())
if (numero % 4 == 0  and numero % 100 != 0 or numero % 400 == 0):
 print("si")
else:
 print("no")