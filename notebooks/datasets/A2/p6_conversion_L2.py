# Convierte un entero positivo a la base indicada construyendo la cadena a mano
def a_base(entero, b):
    simbolos = "0123456789ABCDEF"
    if entero == 0:
        return "0"
    salida = ""
    while entero > 0:
        r = entero % b
        salida = simbolos[r] + salida
        entero = entero // b
    return salida

# Comprueba el resultado leyendo la cadena de vuelta
def comprobar(texto, b):
    acumulado = 0
    for ch in texto:
        acumulado = acumulado * b + "0123456789ABCDEF".index(ch)
    return acumulado

x = int(input())
es_neg = x < 0
if es_neg:
    x = -x
bin_str = a_base(x, 2)
hex_str = a_base(x, 16)
sg = "-" if es_neg else ""
print("Decimal:", sg + str(x))
print("Binario:", sg + bin_str)
print("Hexadecimal:", sg + hex_str)
# Agrupa el binario de 4 en 4 bits
padded = bin_str.zfill((len(bin_str) + 3) // 4 * 4)
bloques = []
for pos in range(0, len(padded), 4):
    bloques.append(padded[pos:pos + 4])
print("Grupos:", " ".join(bloques))
if comprobar(bin_str, 2) == x and comprobar(hex_str, 16) == x:
    print("Verificado")
