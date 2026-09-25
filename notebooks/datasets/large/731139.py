def producto_escalar(casos):
    resultados = []
    for _ in range(casos):
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        resultado = sum(a * b for a, b in zip(A, B))
        resultados.append(resultado)
    
    for res in resultados:
        print(res)

num_casos = int(input())
producto_escalar(num_casos)
