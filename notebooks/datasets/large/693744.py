N = int(input())

for i in range(0, N):
    M = int(input())
    entradaA = input()
    numerosA = entradaA.split()
    entradaB = input()
    numerosB = entradaB.split()
    A = [int(num) for num in numerosA]
    B = [int(num) for num in numerosB]
    sumatoria = 0
    for i in range(len(A)):
        multp = A[i] * B[i]
        sumatoria = sumatoria + multp
    print(sumatoria)
