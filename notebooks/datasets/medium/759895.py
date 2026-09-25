n = int(input())
for i in range(n):
    x = input()
    palFinal = ''
    cont = 0
    for item in x:
        var = ' '
        if(item != ' '):
            if(cont % 2 ==0):
                var = item.upper()
            else:
                var = item.lower()
            cont += 1
        palFinal = palFinal + var
    print(palFinal)