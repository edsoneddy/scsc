# Convierte un entero positivo a la base indicada construyendo la cadena a mano
def convertir(numero, base):
    digitos = "0123456789ABCDEF"
    if numero == 0:
        return "0"
    resultado = ""
    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero //= base
    return resultado

# Comprueba el resultado leyendo la cadena de vuelta
def verificar(cadena, base):
    valor = 0
    i = 0
    while i < len(cadena):
        valor = valor * base + "0123456789ABCDEF".index(cadena[i])
        i += 1
    return valor

n = int(input())
negativo = n < 0
if negativo:
    n = -n
binario = convertir(n, 2)
hexa = convertir(n, 16)
signo = ""
if negativo:
    signo = "-"
print("Decimal:", signo + str(n))
print("Binario:", signo + binario)
print("Hexadecimal:", signo + hexa)
# Agrupa el binario de 4 en 4 bits
relleno = binario.zfill((len(binario) + 3) // 4 * 4)
grupos = []
k = 0
while k < len(relleno):
    grupos.append(relleno[k:k + 4])
    k += 4
print("Grupos:", " ".join(grupos))
if verificar(binario, 2) == n and verificar(hexa, 16) == n:
    print("Verificado")
