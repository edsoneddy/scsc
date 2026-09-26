casos = int(input())
for x in range(casos):
    n = int(input())
    c = 0
    while n>=10:
        c = c + 1
        s = 1
        while n>0:
            d = n%10
            s = d*s
            n = n//10
        n=s
    print(str(c) + " pasos" )