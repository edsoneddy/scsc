for t in range(int(input())):
    n = input()
    pa = 0

    while len(n) > 1:
        p = int(n[0])
        for i in range(1, len(n)):
            p *= int(n[i])
        n = str(p)
        pa += 1
    print(pa, 'pasos')