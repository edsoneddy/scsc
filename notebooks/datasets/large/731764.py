casos = int(input())
p_escalar=[]
for _ in range(casos):
    tamaño_vector = int(input())  
    vector1 = list(map(int, input().split())) 
    vector2 = list(map(int, input().split()))
    for i in range(tamaño_vector):
        f=vector1[i]*vector2[i]
        p_escalar.append(f)
    print(sum(p_escalar))
    p_escalar=[]