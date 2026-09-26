import math

# True cuando n es primo, False en otro caso
def es_primo(n):
  if n < 2:
    return False
  for d in range(2, int(math.sqrt(n))+1):
    if n%d == 0:
      return False
  return True


# Divide n entre el menor divisor posible
# hasta llegar a 1
def factorizar(n):
  factores = []
  divisor = 2
  while n > 1:
    if n%divisor == 0:
      factores.append(divisor)
      n = n // divisor
    else:
      divisor += 1
  return factores

numero = int(input())
if es_primo(numero):
  print(numero, "es primo")
else:
  print(numero, "no es primo")
  if numero > 1:
    fs = factorizar(numero)
    print("Factores:", fs)
    # Formato con exponentes
    partes = []
    for p in sorted(set(fs)):
      partes.append("{}^{}".format(p, fs.count(p)))
    print("Forma:",
      " * ".join(partes))
