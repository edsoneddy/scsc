import string

# Desplaza una letra conservando mayuscula o minuscula
def rotar(c, k):
    if c in string.ascii_uppercase:
        origen = ord("A")
    elif c in string.ascii_lowercase:
        origen = ord("a")
    else:
        return c
    pos = (ord(c) - origen + k) % 26
    return chr(origen + pos)

# Cifra o descifra todo el mensaje
def transformar(msg, k):
    out = ""
    for car in msg:
        out += rotar(car, k)
    return out

frase = input()
k = int(input())
codificado = transformar(frase, k)
print("Cifrado:", codificado)
print("Descifrado:", transformar(codificado, -k))
# Cuenta mayusculas y minusculas del original
n_may = 0
n_min = 0
for x in frase:
    if x.isupper():
        n_may += 1
    elif x.islower():
        n_min += 1
print("Mayusculas:", n_may, "Minusculas:", n_min)
if k % 26 == 0:
    print("Aviso: la clave no cambia el mensaje")
