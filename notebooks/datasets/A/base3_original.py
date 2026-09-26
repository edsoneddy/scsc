t=int(input())
for i in range (t):
    n=int(input())
    vec=list(map(int, input().split()))
    ##burbuja
    cont=0
    for i in range (n-1):
        for j in range(i+1,n):
            if(vec[i]>vec[j]):
                aux=vec[i]
                vec[i]=vec[j]
                vec[j]=aux
                cont+=1
    print(cont)
