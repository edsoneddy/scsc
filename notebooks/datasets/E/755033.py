#Segundo Diccionario
import re
def segundoDic():
    P = set()
    palabraActual = ""
    try:
        while True:
            l = input().strip()
            if l.endswith('-'):
                palabraActual += l[:-1]
            else:
                palabraActual += l
                P_en_l = re.findall(r'[a-zA-Z\-]+', palabraActual)
                for palabra in P_en_l:
                    P.add(palabra.lower())
                palabraActual = ""
    except EOFError:
        pass 
    for palabra in sorted(P):
        print(palabra)
segundoDic()
