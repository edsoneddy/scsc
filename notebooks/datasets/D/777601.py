#inicio
n=int(input())
resultados=[]
for _ in range(n):
    cad=input()
    baile = ""
    sw = 0
    for char in cad:
        if char==" ":
            baile+=char
        else:
            if sw==0:
                baile+=char.upper()
                sw=1
            else:
                baile+=char.lower()
                sw=0
    resultados.append(baile)
for resultado in resultados:
    print(resultado)
#fin