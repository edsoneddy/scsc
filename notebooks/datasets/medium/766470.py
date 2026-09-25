def volverCadenaBailarina(palabra):
    final = ''
    c = 0
    for caracter in palabra:
        var = ' '
        if caracter != ' ':
            if c % 2 == 0:
                var = caracter.upper()
            else:
                var = caracter.lower()
            c += 1        
        final = final + var 
    return final     

resultados = []
N = int(input())
for i in range(N):
    palabra = str(input())
    resultados.append(volverCadenaBailarina(palabra))  

for resultado in resultados:
    print(resultado) 