casos=int (input ())
for i in range (casos):
    elem=int (input ())
    nros1=list(map(int,input().split()))
    nros2=list(map(int,input().split()))
    suma=0
    for j in range (elem):
        suma=(nros1[j]*nros2[j])+suma
    print (suma)