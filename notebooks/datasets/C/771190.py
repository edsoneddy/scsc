anio = int(input())
if anio%4 == 0 and anio%100 != 0:
    print('si')
elif anio%400 == 0:
    print('si')
else:
    print('no')