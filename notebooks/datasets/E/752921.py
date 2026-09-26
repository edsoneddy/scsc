palabras = set()
tmp = ""

while True:
    try:
        linea = input()
        words = linea.split()
        
        for i, p in enumerate(words):
            if tmp:
                p = tmp + p
                tmp = ""
            
            # Si termina en guión y es última palabra
            if p.endswith('-') and i == len(words) - 1:
                tmp = p[:-1]
            else:
                # Limpiar palabra y agregar
                p = p.strip('.-,')
                if p:
                    palabras.add(p.lower())
    except:
        break

for p in sorted(palabras):
    print(p)