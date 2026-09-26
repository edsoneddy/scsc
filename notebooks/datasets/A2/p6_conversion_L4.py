# Convierte un entero positivo a la base indicada construyendo la cadena a mano
def convertir(numero, base):
    digitos = "0123456789ABCDEF"
    if numero == 0:
        return "0"
    resultado = ""
    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero = numero // base
    return resultado

# Comprueba el resultado leyendo la cadena de vuelta
def verificar(cadena, base):
    valor = 0
    for c in cadena:
        valor = valor * base + "0123456789ABCDEF".index(c)
    return valor

def agrupar_bits(binario):
    relleno = binario.zfill((len(binario) + 3) // 4 * 4)
    grupos = []
    for k in range(0, len(relleno), 4):
        grupos.append(relleno[k:k + 4])
    return grupos

def mostrar(signo, n, binario, hexa):
    print("Decimal:", signo + str(n))
    print("Binario:", signo + binario)
    print("Hexadecimal:", signo + hexa)

n = int(input())
negativo = n < 0
if negativo:
    n = -n
binario = convertir(n, 2)
hexa = convertir(n, 16)
signo = "-" if negativo else ""
mostrar(signo, n, binario, hexa)
# Agrupa el binario de 4 en 4 bits
grupos = agrupar_bits(binario)
print("Grupos:", " ".join(grupos))
if verificar(binario, 2) == n and verificar(hexa, 16) == n:
    print("Verificado")
