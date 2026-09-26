n = int(input())
if n%400==0:
    print('si')
elif n%4 == 0 and n%100!=0:
    print('si')
else:
    print('no')