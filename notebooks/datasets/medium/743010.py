N = int(input())
for i in range(N + 1):
    C = input().lower()
    S = ''
    cont = 0
    for j in range(len(C)):
        if C[j] == ' ': 
            S = S + C[j]
        else:
            if cont % 2 == 0:
                S = S + C[j].upper() 
                cont = cont + 1
            else:
                S = S + C[j]
                cont = cont + 1
    print(S)