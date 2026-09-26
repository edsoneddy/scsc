def prodesc(vec1,vec2):
    suma=0
    for i in range(len(vec1)):
        prod=vec1[i]*vec2[i]
        suma+=prod
    return suma

casos=int(input())
for j in range(casos):
    num=int(input())
    vec1=list(map(int,input().split()))
    vec2=list(map(int,input().split()))
    print(prodesc(vec1,vec2))