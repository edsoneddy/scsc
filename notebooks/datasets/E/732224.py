from sys import stdin
def producto(A, B):
    return sum(a * b for a, b in zip(A, B))
num_casos = int(input().strip())
for _ in range(num_casos):
    n = int(input().strip())
    vector_A = list(map(int, input().strip().split()))
    vector_B = list(map(int, input().strip().split()))
    res = producto(vector_A, vector_B)
    print(res)
