import string

# Desplaza una letra conservando mayuscula o minuscula
def desplazar(letra, clave):
    if letra not in string.ascii_letters:
        return letra
    if "A" <= letra <= "Z":
        base = ord("A")
    else:
        base = ord("a")
    posicion = (clave + ord(letra) - base) % 26
    return chr(base + posicion)

# Cifra o descifra todo el mensaje
def cifrar(mensaje, clave):
    salida = ""
    for caracter in mensaje:
        salida += desplazar(caracter, clave)
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
        may += 1
    elif ch.islower():
        minus += 1
print("Mayusculas:", may, "Minusculas:", minus)
if not clave % 26:
    print("Aviso: la clave no cambia el mensaje")
