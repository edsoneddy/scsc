casos=int(input())

for i in range(casos):

    cad=input()

    t=True

    ans=""

    for j in range(len(cad)):

        aux=(cad[j]+"")

        if(aux!=" "):

            if(t):

                aux=aux.upper()

                t=False

            else:

                aux=aux.lower()

                t=True

        ans+=aux

    print(ans)

 