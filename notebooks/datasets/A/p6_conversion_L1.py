# Pasa un entero no negativo a otra base (2 a 16)
# armando el resultado digito por digito
def convertir(numero, base):
  digitos = "0123456789ABCDEF"
  if numero == 0:
    return "0"
  resultado = ""
  while numero > 0:
    resto = numero%base
    resultado = digitos[resto] + resultado
    numero = numero // base
  return resultado


# Verificacion: reconstruye el valor desde la cadena
def verificar(cadena, base):
  valor = 0
  for c in cadena:
    valor = valor*base+"0123456789ABCDEF".index(c)
  return valor

n = int(input())
negativo = n < 0
if negativo:
  n = -n
binario = convertir(n, 2)
hexa = convertir(n, 16)
signo = "-" if negativo else ""
print("Decimal:", signo + str(n))
print("Binario:", signo + binario)
print("Hexadecimal:", signo + hexa)
# Agrupa el binario de 4 en 4 bits
relleno = binario.zfill((len(binario) + 3) // 4 * 4)
grupos = []
for k in range(0, len(relleno), 4):
  grupos.append(relleno[k:k + 4])
print("Grupos:", " ".join(grupos))
if verificar(binario, 2) == n and \
    verificar(hexa, 16) == n:
  print("Verificado")
