def contarPasos(n):
    count = 0
    aux = 1
    while int(n) > 9:
        for i in n:
            aux *= int(i)
        n = str(aux); aux = 1
        count += 1
    return count


for n in range(int(input())):
    print(f"{contarPasos(input().strip())} pasos")