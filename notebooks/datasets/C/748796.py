def gen_secuencia(n, sec="", o=0, c=0):
    if len(sec) == 2*n:
        print(sec)
        return
    if o < n:
        gen_secuencia(n, sec + "(", o+1, c)
    if c < o:
        gen_secuencia(n, sec + ")", o, c+1)

#Main
try:
    while True:
        n = int(input())
        if not n:
            break
        gen_secuencia(n)
except:
    pass