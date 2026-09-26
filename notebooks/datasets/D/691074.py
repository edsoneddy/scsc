def nov_bai(cad):
    bai = ""
    cont = 0
    for i in cad:
        if i.isalpha():
            if cont % 2 == 0:
                bai += i.upper()
            else:
                bai += i.lower()
            cont += 1
        else:
            bai += i
    return(bai)
n = int(input())
while n:
    m = input()
    print(nov_bai(m))
    n-=1
 