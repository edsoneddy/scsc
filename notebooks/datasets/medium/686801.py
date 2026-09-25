n = int(input())
for i in range(n):
    x = input()
    X = ''
    C = 0
    for item in x:
        var = ' '
        if(item != ' '):
            if(C % 2 ==0):
                var = item.upper()
            else:
                var = item.lower()
            C += 1
        X = X + var
    print(X)