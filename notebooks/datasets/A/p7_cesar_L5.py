import string

# Desplaza una letra conservando mayuscula o minuscula
def desplazar(letra, clave):
    if letra in string.ascii_lowercase:
        base = ord("a")
    elif letra in string.ascii_uppercase:
        base = ord("A")
    else:
        return letra
    posicion = (ord(letra) - base + clave) % 26
    return chr(base + posicion)

# Cifra o descifra todo el mensaje
def cifrar(mensaje, clave):
    salida = ""
    i = 0
    while i < len(mensaje):
        salida = salida + desplazar(mensaje[i], clave)
        i += 1
    return salida

texto = input()
clave = int(input())
cifrado = cifrar(texto, clave)
print("Cifrado:", cifrado)
print("Descifrado:", cifrar(cifrado, -clave))
# Cuenta mayusculas y minusculas del original
may = 0
minus = 0
for ch in texto:
    if ch.isupper():
        may = may + 1
    elif ch.islower():
        minus = minus + 1
print("Mayusculas:", may, "Minusculas:", minus)
if clave % 26 == 0:
    print("Aviso: la clave no cambia el mensaje")
