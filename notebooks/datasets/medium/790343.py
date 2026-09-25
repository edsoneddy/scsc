n=int(input())
lista_bailarinas=[]
for i in range(n):
    lista_bailarinas.append(input())

for i in range(n):
    aux_cad=lista_bailarinas[i]
    aux_cad2=''
    cont=0
    n_aux=len(aux_cad)
    for j in range(n_aux):
        cont+=1
        if aux_cad[j]==' ':
            cont-=1
        if aux_cad[j]!=' ' and cont%2==0:
            min=aux_cad[j].lower()
            aux_cad2+=min
        else:
            max=aux_cad[j].upper()
            aux_cad2+=max
    lista_bailarinas[i]=aux_cad2

for i in range(n):
    print(lista_bailarinas[i])